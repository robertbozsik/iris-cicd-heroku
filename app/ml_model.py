import pickle
import numpy as np


def iris_prediction(sepal_length, sepal_width, petal_length, petal_width):

    # import the classifier pickle object
    with open('iris_classifier_ml_model.pkl', 'rb') as file:
        model = pickle.load(file)

    X_new = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(X_new)

    species = ['Setosa', 'Versicolor', 'Virginica']

    result = species[int(prediction)]

    return result


if __name__ == '__main__':
    print(iris_prediction(5.9, 3, 4.2, 1.5))
