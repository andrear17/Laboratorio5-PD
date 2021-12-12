import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

class PlusOneVariableTransformer(BaseEstimator, TransformerMixin):
    # Constructor
    def __init__(self, variables):
        # Debe ser una lista por requisito del la libreria
        if not isinstance(variables, list):
            raise ValueError('La variable debe ser incluida en una lista.')
        
        self.variables = variables

    # Método FIT para habilitar método transform
    def fit(self, X, y=None):
        return self

    # Método para transformar variables temporales. 
    def transform(self, X):
        X=X.copy()
        for feature in self.variables:
            X[feature] = X[feature] + 1
        return X