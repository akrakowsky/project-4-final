import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine



def predictions(age_type, gender_type):
      
    engine = create_engine("postgresql://postgres:<enter password>@localhost:5432/capstone")
    model_df = pd.read_sql("SELECT * FROM final_project;", engine)
        
    # model_df = pd.read_csv("./db.csv")

    X = model_df[["age_type", "gender_type"]]
    y = model_df["degree_type"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1)
    scaler = StandardScaler().fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    clf = RandomForestClassifier(random_state=1, n_estimators=500).fit(X_train_scaled, y_train)
    print(f'Training Score: {clf.score(X_train_scaled, y_train)}')
    print(f'Testing Score: {clf.score(X_test_scaled, y_test)}')

    return clf.predict([[age_type,gender_type]])