import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def rec_func(list1):
    datas = pd.read_csv("../datas/mobile_prices.csv",encoding= 'unicode_escape')
    train_data_set = datas.drop(['Link','Reference'],axis=1)
    price_ratio = list1[0][0]/10
    train_data_set = train_data_set[train_data_set['Price']<(list1[0][0]+price_ratio)]
    train_data_set = train_data_set[train_data_set['Price']>(list1[0][0]-price_ratio)]
    train_data_set['Front_cam'] = train_data_set['Front_cam'].str.replace("MP","").astype(int)
    train_data_set['Primary_cam'] = train_data_set['Primary_cam'].str.replace("MP","").astype(int)
    train_data_set['OS'] = train_data_set['OS'].replace({'Android': 1, 'IOS': 0})
    encoder = LabelEncoder()
    train_data_set['brand_int'] = encoder.fit_transform(train_data_set['brand'])
    pixels = []
    for datas in train_data_set['res']:
        width,height = datas.split('x')
        pixels.append(int(width)*int(height))

    train_data_set['pixels'] = pixels
    train_data_set['Model_int'] = encoder.fit_transform(train_data_set['Model'])
    
    X = train_data_set.drop(['Model','brand','res','Model_int','display','brand_int'],axis=1)
    y = train_data_set['Model_int']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    k =len(train_data_set['brand_int'].unique())
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(list1)[0]
    distances, indices = knn.kneighbors(list1)
    label = train_data_set[y == y_pred]
    return(label[['Price','Model','brand','storage','Primary_cam','Front_cam']])
