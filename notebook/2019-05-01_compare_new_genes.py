# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.3
#   kernelspec:
#     display_name: Python [conda env:dmel_pacbio]
#     language: python
#     name: conda-env-dmel_pacbio-py
# ---

# %% {"pycharm": {"is_executing": false}}
import pandas as pd
pd.options.display.max_columns = 100


# %% {"pycharm": {"is_executing": false, "metadata": false, "name": "#%%\n"}}
def parse(fname):
    df = pd.read_csv(fname, sep='\t', index_col=0)
    #slice = (df.associated_gene.str.contains('novel') & ~df.associated_gene.str.contains('FBgn')).values
    slice = df.associated_gene.str.contains('novel').values
    return df[slice]


# %% {"pycharm": {"is_executing": false, "metadata": false, "name": "#%%\n"}}
testis = parse('../output/pacbio-wf/w1118_testi1/sqanti/w1118_testi1.collapsed_classification.txt').dropna(axis=1, how='all')


# %% {"pycharm": {"is_executing": false, "metadata": false, "name": "#%%\n"}}
male = parse('../output/pacbio-wf/w1118_wmal1/sqanti/w1118_wmal1.collapsed_classification.txt').dropna(axis=1, how='all')


# %% {"pycharm": {"is_executing": false, "metadata": false, "name": "#%%\n"}}
testis.shape, male.shape

# %%
testis

# %% {"pycharm": {"is_executing": false, "metadata": false, "name": "#%%\n"}}
print('\n'.join(sorted(testis.index.values.tolist())))

# %% {"pycharm": {"metadata": false, "name": "#%%\n"}}


