from flask import Flask, request,render_template
# import tensorflow as tf
# import numpy as np

app = Flask(__name__)
# model = tf.keras.models.load_model('path/to/model.h5')

# @app.route('/predict', methods=['POST'])
# def predict():
#     print('')
#     # get image data from request
#     image_data = request.files['image'].read()

#     # preprocess image data
#     # ...   

#     # make prediction
#     prediction = model.predict(preprocessed_image)

#     # format prediction result
#     # ...

#     # return prediction result
#     return prediction_result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    print('predicting')
    return 'function executed'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run()
