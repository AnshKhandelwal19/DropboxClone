from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)

#Route to Home Page
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/files")
def files():
    return render_template('files.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('upload.html', update_string = 'No File Part') 
    file = request.files['file']
    if file.filename == '':
        return render_template('upload.html', update_string = 'No File Selected')
    if file:
        upload_path = 'Files/' + file.filename.rsplit('.', 1)[1].lower() + "/" + file.filename
        file.save(upload_path)  # Save the uploaded file to the server
        return render_template('upload.html', update_string = 'File Upload Successful')


@app.route('/upload', methods=['GET'])  # Add a "GET" route for the /upload endpoint
def show_upload_form():
    return render_template('upload.html', update_string = '')

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)