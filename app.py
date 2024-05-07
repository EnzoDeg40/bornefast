from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    image = request.files['image']

    # Get the GPS location from the request
    gps_location = request.form['gps_location']

    # Save the image file to the uploads folder
    image.save('uploads/' + image.filename)


    return 'Image uploaded successfully'

if __name__ == '__main__':
    app.run()