from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/download")
def downloads():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty part without a filename
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Save the uploaded file to the server
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return 'File uploaded successfully'
    return render_template('download.html')

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)