# TODOs
This is a list of TODOs for the next years, mostly for internal purposes of the teachers.

Karel:

Ondra:

- Pripravit cviceni na GAN
- Ukazat hyperparam opti pro NN
- https://masters.donntu.ru/2012/fknt/umiarov/library/lecun.pdf

HW 1
- do zadání rozepsat, co má úloha všechno mít
  - data exploration
  - predictor definition
  - variable encoding
  - hyperparameter selection
  - model score validation
  - SHAP value interpretation

Next year
(Karel) 
- TODO random forest, doplnit nazev promenne do ktere ulozit model do zadani
- opravit popis u Random Forest sekce (The task is to predict if tomorrow is going to rain) - neni pravda predikujeme teplotu
- random forest paramaters add random_state
- XGBoost better code for permutation importance

```python
res = []
for pred in tqdm(cols_pred):
    pi, iqr95, iqr05 = permutation_importance(
        dt=data[test_mask][cols_pred + [col_target]], 
        predictor=pred,
        target=col_target,
        model=booster,
        n_iters=10
    )
    res.append((pred, pi, iqr05, iqr95))
res = pd.DataFrame(res, columns = ['predictor', 'permutation_importance', 'iqr05', 'iqr95'])
res = res.sort_values('permutation_importance', ascending=False).reset_index(drop=True)
res
```