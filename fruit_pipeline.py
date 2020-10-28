import pandas as pd 
import numpy as np 
from sklearn.compose import ColumnTranformer
from sklearn.base import TransformerMixin


fruit = pd.read_csv('fruit_data.csv', index_col = False)

ct = ColumnTranformer(
    []
)