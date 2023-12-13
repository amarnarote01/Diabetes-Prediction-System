from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv('D:\diabetes.csv')
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)

    val1 = float(request.GET['Pregnancies'])
    val2 = float(request.GET['Glucose'])
    val3 = float(request.GET['Blood_Pressure'])
    val4 = float(request.GET['Skin_Thickness'])
    val5 = float(request.GET['Insulin'])
    val6 = float(request.GET['BMI'])
    val7 = float(request.GET['Diabetes_Pedigree_Function'])
    val8 = float(request.GET['Age'])

    pred = forest.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"
    return render(request, 'predict.html', {"result2":result1}) 