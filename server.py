from flask import Flask, request,render_template

import os;

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        image_data = request.files["imgInp"]
        if(not image_data):
            return render_template('index.html',output="Please Choose Image")
        
        directory = os.path.join('static/uploads/',image_data.filename);

        print(directory);

        # output=
        return render_template('index.html',output=output)
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run()
