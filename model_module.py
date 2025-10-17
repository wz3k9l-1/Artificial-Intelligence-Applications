# model_module.py - Module for loading and predicting with the model
import tensorflow as tf
import numpy as np

# Class names for Iris
CLASS_NAMES = ['Setosa', 'Versicolor', 'Virginica']

# Load the saved model
model = tf.keras.models.load_model('iris_model.h5')


def predict_iris(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> str:
    # Prepare input
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Predict
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)

    return CLASS_NAMES[predicted_class]
