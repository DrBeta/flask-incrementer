from flask import Flask, render_template
app = Flask(__name__)
scorecount = 0
@app.route("/")
def main():
    return render_template('index.html', score=scorecount)
@app.route("/<action>")
def change(action):
    global scorecount
    if action == "increment":
        scorecount += 1
    if action == "decrement":
        scorecount -= 1
    if action == "reset":
        scorecount = 0
    return render_template("index.html", score=scorecount)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)