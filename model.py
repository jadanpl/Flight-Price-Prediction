# load libraries
from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
import pickle

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/jadanpl/Flight-Price-Prediction/main/Clean_Flight_Price_Dataset.csv")
df = df.drop(['Unnamed: 0', 'flight'], axis=1)

# determine inputs and output
X = df.drop('price', axis =1)
Y = df['price']
num_cols = list(X.select_dtypes([np.number]).columns)
cat_cols = list(X.select_dtypes(include='object').columns)

# model building
trans = ColumnTransformer(transformers=[('num', MinMaxScaler(), num_cols),
                                        ('cat', OneHotEncoder(sparse=False, handle_unknown='ignore'), cat_cols)],
                          remainder='passthrough')
final_model = Pipeline(steps=[('transformer',trans),
                              ('ridge', Ridge(alpha=5.0, random_state=42))])
final_model.fit(X,Y)

# save model
pickle.dump(final_model, open('ridge_reg.pkl','wb'))