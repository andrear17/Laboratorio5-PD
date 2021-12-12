import joblib
import pandas as pd
import numpy as np

#Cargamos modelo y pipeline
titanic_model = joblib.load('survivedTitanic_pipeline.pkl')
#X_test = pd.read_csv('test.csv')

#Funcion para hacer predicciones.
def predict(X):
    predicts = titanic_model.predict(X)
    return predicts[0]

#X_test = pd.json_normalize({"PassengerId":1,"Pclass":1,"Name": "Mike Dallas","Sex": "male","Age": 22,"SibSp": 0,"Parch": 0,"Ticket": 649,"Fare": 7.25,"Cabin": "B14","Embarked":"S"})
#print('Resultado', predict(X_test))