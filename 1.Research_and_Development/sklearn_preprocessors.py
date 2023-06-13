import numpy as np
import pandas as pd
from datetime import datetime

from sklearn.base import BaseEstimator, TransformerMixin


class ElapsedYearsTransformer(BaseEstimator, TransformerMixin):
    """Calculate Elapsed Years From Reference Years"""
    
    def __init__(self, vars: list, ref_var = None):
        
        self.vars = None
        self.ref_var = None
        
        if not isinstance(vars, list):
            raise ValueError(f'{vars} must be a list')
        if ref_var is None:
            pass
        else:
            if not isinstance(ref_var, str): #ref_var is a column name in the dataframe
                raise ValueError(f'{ref_var} must be a string')
            
        self.vars = vars
        self.ref_var = ref_var
    
    def fit(self, X, y = None):
        
        # we need this step to fit the sklearn pipeline
        return self
   

    def transform(self, X, y = None):
        
        # so that we do not over-write the original dataframe
        X = X.copy()
        
        if not isinstance(self.ref_var, str): 
            self.ref_var = datetime.now().year
            X[str(self.ref_var)] = self.ref_var
            for var in self.vars:
                X['diff_from_' + str(self.ref_var) + '-' + var] = X[str(self.ref_var)] - X[var]
            
            X.drop(str(self.ref_var), axis = 1, inplace = True)
            return X
        
        else:
            if self.ref_var in X.columns:
                for var in self.vars:
                    X['diff_from_' + str(self.ref_var) + '-' + var] = X[str(self.ref_var)] - X[var]
                
                return X
            
            else:
                print(f'{self.ref_var} is not in dataframe columns: {X.columns.values}')
                
                return None



class DataTypeConverter(BaseEstimator, TransformerMixin):
    """ Custom Transformer to convert columns to int32 """
    
    def __init__(self, vars: list, data_type: str):
        
        self.vars = None
        self.data_type = None
        
        if not isinstance(vars, list):
            raise ValueError(f'{vars} must be a list')
        
        if not isinstance(data_type, str): #ref_var is a column name in the dataframe
            raise ValueError(f'{data_type} must be a string')
        
        self.vars = vars
        self.data_type = data_type
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):
        for var in self.vars:
            X[var] = X[var].astype(self.data_type)
        return X
    
    

class Mapper(BaseEstimator, TransformerMixin):
    """String to numbers Mapper."""
    
    def __init__(self, variables: list, mappings: dict): #vars must be list of columns to be mapped, mappings must be 
        
        self.variables = None
        self.mappings = None
        
        if not isinstance(variables, list):
            raise ValueError(f'{variables} must be a list')
            
        self.variables = variables
        self.mappings = mappings
    
    def fit(self, X, y = None):
        
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X):
        
        # so that we do not over-write the original dataframe
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)

        return X
    


class MeanImputer(BaseEstimator, TransformerMixin):
    """Numerical missing value imputer (with Mean)."""

    def __init__(self, variables):
        
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables
        self.imputer_dict_ = {}  # Initialize imputer_dict_ as an empty dictionary

    def fit(self, X, y = None):
        
        # persist mean values in a dictionary
        #self.imputer_dict_ = {}
        self.imputer_dict_ = X[self.variables].mean().to_dict()
        return self

    def transform(self, X):
        
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace = True)
        return X
    


class ModeImputer(BaseEstimator, TransformerMixin):
    """Numerical missing value imputer (with Mode)."""

    def __init__(self, variables):
        
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables
        self.imputer_dict_ = {}  # Initialize imputer_dict_ as an empty dictionary

    def fit(self, X, y = None):
        
        # persist mean values in a dictionary
        #self.imputer_dict_ = {}
        self.imputer_dict_ = X[self.variables].mode().to_dict()
        return self

    def transform(self, X):
        
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace = True)
        return X



class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """Groups infrequent categories into a single string"""

    def __init__(self, variables,  tol = 0.05):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        
        self.tol = tol
        self.variables = variables

    def fit(self, X, y = None):
        # persist frequent labels in dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            # the encoder will learn the most frequent categories
            t = pd.Series(X[var]).value_counts(normalize = True) 
            # frequent labels:
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(
                X[feature].isin(self.encoder_dict_[feature]), X[feature], "Rare")

        return X



class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """String to numbers categorical encoder."""

    def __init__(self, variables):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        
        self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis = 1)
        temp.columns = list(X.columns) + ["target"]

        # persist transforming dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            t = temp.groupby([var])["target"].mean().sort_values(ascending = True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t, 0)}

        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])

        return X