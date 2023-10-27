from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)

#Set up folder for file uploads
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#check for allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif', 'pdf', 'txt'}

#Route to Home Page
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/files")
def files():
    return render_template('files.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    update = 'N/A'
    if 'file' not in request.files:
        return render_template('upload.html', update_string = 'No File Part') 
    file = request.files['file']
    if file.filename == '':
        return render_template('upload.html', update_string = 'No File Selected')
    if file:
        file.save(file.filename)  # Save the uploaded file to the server
        return render_template('upload.html', update_string = 'File Upload Successful')


@app.route('/upload', methods=['GET'])  # Add a "GET" route for the /upload endpoint
def show_upload_form():
    return render_template('upload.html', update_string = '')

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)