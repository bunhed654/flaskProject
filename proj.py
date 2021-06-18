from flask import Flask

app = Flask(__name__)

@app.route("/")
def message():
    return "<p style='text-align:center'>Hello! I’m Flask server and this is my website!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
