from flask import Flask, render_template

app = Flask(__name__)

#Route to Home Page
@app.route("/")
def hellow_world():
    return render_template('home.html')

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)