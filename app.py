from flask import Flask, render_template

app = Flask(__name__)

#Route to Home Page
@app.route("/files")
def files():
    return render_template('files.html')

@app.route("/download")
def downloads():
    return render_template('download.html')

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)