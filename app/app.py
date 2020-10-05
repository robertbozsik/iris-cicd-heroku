from flask import Flask, render_template, request
import numpy as np
# import only the function from the ml_model.py
from ml_model import iris_prediction
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 8000))


@app.route('/', methods=['POST', 'GET'])
def ml_model_function():
    '''This function receives 4 parameters from the front end
    makes a prediction based on them, and sends the result back to the frontend.'''

    if request.method == 'POST':

        # save the inputs from the front end
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # call the ml function to make a prediction
        prediction = iris_prediction(
            sepal_length, sepal_width, petal_length, petal_width)

        # send the prediction back to the front end
        return render_template('main.html', output=prediction)

    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=8000)
    #app.run(debug=True, host='0.0.0.0')
