import os
import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing, model_selection
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv(
    'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')

# Data Pre-processing
proc = preprocessing.LabelEncoder()
sepal_length = proc.fit_transform(list(data["sepal_length"]))
sepal_width = proc.fit_transform(list(data["sepal_width"]))
petal_length = proc.fit_transform(list(data["petal_length"]))
petal_width = proc.fit_transform(list(data["petal_width"]))
variety = proc.fit_transform(list(data["species"]))

# Prediction
predict = "species"
x = list(zip(sepal_length, sepal_width, petal_length, petal_width))
y = list(variety)

var = ['Setosa', 'Virginica', 'Versicolor']
best = 0
worst = 100

for i in range(100):
    x_train, x_test, y_train, y_test = model_selection.train_test_split(
        x, y, test_size=0.9)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    if accuracy > best:
        best = accuracy
    elif accuracy < worst:
        worst = accuracy
    prediction = model.predict(x_test)
    print(f"Prediction:\t{var[prediction[i]].ljust(10)}\tActual: {var[y_test[i]].ljust(10)}\tAccuracy: {str(round(accuracy*100, 2)).ljust(5)} % \t Data: {x_test[i]}")

print(f"\nHighest Accuracy: {round((100*best), 2)}%")
print(f"\nLowest Accuracy: {round((100*worst), 2)}%")
