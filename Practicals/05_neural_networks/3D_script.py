# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:53:40 2021

@author: luky
"""

import tensorflow as tf
import numpy as np
import argparse


# Functions for 3D object augmentation
def augment(image, labels):
    # remove last dimension
    image = tf.squeeze(image)

    # transpose
    image = tf.transpose(image, perm=[1, 2, 0])

    # mirror reflection
    if tf.random.uniform([]) >= 0.5:
        image = tf.image.flip_left_right(image)
    if tf.random.uniform([]) >= 0.5:
        image = tf.image.flip_up_down(image)
 
    # rotate 90, 180, 270 degrees
    p = tf.random.uniform([])
    if p < 0.25:
        image = tf.image.rot90(image, k=1)
    elif p < 0.5:
        image = tf.image.rot90(image, k=2)
    elif p < 0.75:
        image = tf.image.rot90(image, k=3)

    # give last dimension back and traspose
    image = tf.transpose(image, perm=[2, 0, 1])
    image = tf.expand_dims(image, axis=3)

    return image, labels

def label_smooth_train(image, labels):
    labels = tf.one_hot(tf.cast(labels, tf.int32), 10)
    labels = tf.cast(labels, tf.float32)
    labels *= (1 - args.smooth_alpha)
    labels += args.smooth_alpha / 10
    return image, labels

def label_smooth_dev(image, labels):
    labels = tf.one_hot(tf.cast(labels, tf.int32), 10)
    labels = tf.cast(labels, tf.float32)
    return image, labels


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch_size", default=128, type=int, help="Batch size.")
    parser.add_argument("--epochs", default=10, type=int, help="Number of epochs.")
    parser.add_argument("--seed", default=42, type=int, help="Random seed.")
    parser.add_argument("--l2", default=0.0001, type=float)
    parser.add_argument("--cnn", default='C-16-3-2-same,R-[C-16-3-1-same,C-16-3-1-same],M-3-2,F,H-100', type=str, help="CNN architecture.")
   
    parser.add_argument("--learning_rate", default=0.001, help="Initial learning rate")
    parser.add_argument("--decay_rate", default=0.92, help="Decay rate for exponential decay, if one, no decay")
    
    parser.add_argument("--augment", default=False, action='store_true')
    parser.add_argument("--smooth", default=True, action='store_true')
    parser.add_argument("--smooth_alpha", default=0.05, help="Alpha for label smoothing")
    
    parser.add_argument("--tensorboard", default=False, action='store_true')
    parser.add_argument("--logdir", default="logs", type=str, help='directory for Tensorboard logs')
    args = parser.parse_args([] if "__file__" not in globals() else None)

    # Fix seeds
    np.random.seed(args.seed)
    tf.random.set_seed(args.seed)
    
    # Load data
    df = np.load("modelnet20.npz")
    data = {}
    
    for data_name in ["train", "dev", "test"]:
        tmp = dict((key[len(data_name) + 1:], df[key]) for key in df if key.startswith(data_name))
        data[data_name] = tmp

    train = tf.data.Dataset.from_tensor_slices((data['train']['voxels'], data['train']['labels']))

    if args.augment:
        train = train.shuffle(4000, seed=args.seed)
        train = train.map(augment)
    if args.smooth:
        train = train.map(label_smooth_train)
    train = train.batch(args.batch_size)
    
    dev = tf.data.Dataset.from_tensor_slices((data['dev']['voxels'], data['dev']['labels']))
    if args.smooth:
        dev = dev.map(label_smooth_dev)
    dev = dev.batch(args.batch_size)
    
    # Model construction:
    inputs = tf.keras.layers.Input(shape=[20, 20, 20, 1])
    origin = inputs
    
    parameters = args.cnn.split(',')
    reg = tf.keras.regularizers.L1L2(l2=args.l2)
    
    for param in parameters:
        par_list = param.split(':')
    
        #4.
        if param.startswith('R:['):
            param = param[3:]
            par_list = param.split(':')
            store_inputs = inputs
    
        if param.endswith(']'):
            par_list = param[:-1].split(':')
    
        # 1.
        if param.startswith('C:'):
            inputs = tf.keras.layers.Conv3D(filters = int(par_list[1]),
                                            kernel_size = int(par_list[2]),
                                            strides = int(par_list[3]),
                                            padding = par_list[4],
                                            activation = tf.keras.activations.relu,
                                            kernel_regularizer = reg)(inputs)
        # 2.
        if param.startswith('CB:'):   
            inputs = tf.keras.layers.Conv3D(filters = int(par_list[1]), 
                                            kernel_size = int(par_list[2]),
                                            strides = int(par_list[3]),
                                            padding = par_list[4],
                                            use_bias = False,
                                            kernel_regularizer = reg)(inputs)
    
            batch_layer = tf.keras.layers.BatchNormalization()(inputs)
            inputs = tf.keras.activations.relu(batch_layer)
            
        # 3.
        if param.startswith('M:'):
            inputs = tf.keras.layers.MaxPool3D(pool_size = int(par_list[1]),
                                                strides = int(par_list[2]))(inputs)
            
        # 3.
        if param.startswith('A:'):
            inputs = tf.keras.layers.AveragePooling3D(pool_size = int(par_list[1]),
                                                strides = int(par_list[2]))(inputs)            
    
        # 4. add the inputs
        if param.endswith(']'):
            inputs += store_inputs
            
        # 5.
        if param.startswith('F'):
            inputs = tf.keras.layers.Flatten()(inputs)
            
        # 6.
        if param.startswith('H:'):  
            inputs = tf.keras.layers.Dense(int(par_list[1]),
                                            activation = tf.keras.activations.relu)(inputs)
            
        # 7.
        if param.startswith('D:'):
            inputs = tf.keras.layers.Dropout(rate = float(par_list[1]))(inputs)
    
    # Add the final output layer
    outputs = tf.keras.layers.Dense(10, activation=tf.nn.softmax)(inputs)
    model = tf.keras.Model(inputs=origin, outputs=outputs)
    
    # Define learning schedules, compile model
    steps = int(data["train"]["voxels"].shape[0] / args.batch_size) # number of updates in an epoch
    
    if args.smooth:
        loss = tf.keras.losses.CategoricalCrossentropy()
        metric = tf.keras.metrics.CategoricalAccuracy(name="accuracy")
    else:
        loss = tf.keras.losses.SparseCategoricalCrossentropy()
        metric = tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy")
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=tf.optimizers.schedules.ExponentialDecay(
                            initial_learning_rate=args.learning_rate, 
                            decay_steps=steps,
                            decay_rate=args.decay_rate)),
        loss=loss,
        metrics=[metric],
    )
   
    # Define callbacks and train the model:
    early_call = tf.keras.callbacks.EarlyStopping(
    monitor='val_accuracy', min_delta=0, patience=15, mode='max', restore_best_weights=True
    )

    if args.tensorboard:
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=args.logdir, histogram_freq=1)

        model.fit(train,
                  epochs=args.epochs,
                  validation_data=dev,
                  callbacks=[early_call, tensorboard_callback])
        
    else:
        model.fit(train,
                  epochs=args.epochs,
                  validation_data=dev,
                  callbacks=[early_call])

    acc = "{:.2f}".format(model.evaluate(dev)[1]*100)



