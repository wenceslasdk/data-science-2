import numpy as np
import pandas as pd

def weight_of_evidence_numeric(data, predictor, col_target, borders = None, n_bins = 7, min_woe = -3):
    dt = data.copy()
    tot_bad = dt[col_target].sum()
    tot_good = (1 - dt[col_target]).sum()
    dt['target_inverse'] = 1 - dt[col_target]
    
    if borders is None:
        borders = dt[predictor].quantile(np.arange(0, 1.01, 1/n_bins)).unique()
    borders[0] = -np.inf
    borders[-1] = np.inf
    dt[predictor] = pd.cut(dt[predictor], borders, include_lowest = True, labels = False)
    dt[predictor].fillna(-1, inplace = True)
    
    dt_grp = dt.groupby(predictor).agg(
        bad_cnt = (col_target, sum),
        good_cnt = ('target_inverse', sum)
    )
    dt_grp = np.log((dt_grp['bad_cnt'] / dt_grp['good_cnt']) / (tot_bad / tot_good))
    
    woe = dt_grp.apply(lambda x: max(x, min_woe)).to_dict()
    
    null_woe = woe[-1] if -1 in woe.keys() else 0
    woe = {(borders[i], borders[i+1]): woe[i] for i in range(len(borders)-1)}
    woe['null'] = null_woe
    
    return woe

def fill_remaining_categories(dt, predictor, categories):
    last_category_index = max(categories.values())
    for val in dt[dt[predictor].notnull()][predictor].unique():
        if val not in categories.keys():
            last_category_index += 1
            categories[val] = last_category_index
            
    return categories

def weight_of_evidence_categ(data, predictor, col_target, categories = None, min_woe = -3):
    dt = data.copy()
    tot_bad = dt[col_target].sum()
    tot_good = (1 - dt[col_target]).sum()
    dt['target_inverse'] = 1 - dt[col_target]
    
    for i in range(len(categories)):
        for val in categories[i]:
            grp_enum = {
                val: i + 1
            }
        i += 1
    
    if categories is not None:
        grp_enum = fill_remaining_categories(dt, predictor, grp_enum)
        dt[predictor] = dt[predictor].replace(grp_enum)
    dt[predictor] = dt[predictor].fillna('null')

    dt_grp = dt.groupby(predictor).agg(
        bad_cnt = (col_target, sum),
        good_cnt = ('target_inverse', sum)
    )
    dt_grp = np.log((dt_grp['bad_cnt'] / dt_grp['good_cnt']) / (tot_bad / tot_good))
    woe = dt_grp.apply(lambda x: max(x, min_woe)).to_dict()
    
    if grp_enum is not None:
        woe_null = woe['null'] if 'null' in woe.keys() else 0
        woe = {key: woe[grp_enum[key]] for key in grp_enum.keys()}
        woe['null'] = woe_null
    
    return woe