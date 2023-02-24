import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

def valuate1(list1):    
    with open('valuate/module.pickle', 'rb') as f:
        module_name = pickle.load(f)
    y_pred = module_name.predict(list1)
    return y_pred
    """data = pd.read_csv("../datas/valuate.csv")
    cleaned_data = data.drop(['Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 23','720','$720 '],axis=1)
    X = cleaned_data.drop(['Brand','Model','OS','Front_cam','Back_cam','Selling_price','Battery','Ram','Internal Storage'],axis=1)
    y = cleaned_data['Selling_price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    rf = RandomForestRegressor(n_estimators=100, random_state=1)
    rf.fit(X_train, y_train) """
