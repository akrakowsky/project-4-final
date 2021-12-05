import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine



def predictions(Latitude, Longitude):
      
    engine = create_engine("postgresql://postgres:<enter password>@localhost:5432/capstone")
    ml_df = pd.read_sql("SELECT * FROM Project_4;", engine)
        
    # model_df = pd.read_csv("./db.csv")

    X = ml_df[["LATITUDE", "LONGITUDE"]]
    y = ml_df["Shape"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1)
    scaler = StandardScaler().fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    clf = RandomForestClassifier(random_state=1, n_estimators=500).fit(X_train_scaled, y_train)
    print(f'Training Score: {clf.score(X_train_scaled, y_train)}')
    print(f'Testing Score: {clf.score(X_test_scaled, y_test)}')

    return clf.predict([[Latitude, Longitude]])