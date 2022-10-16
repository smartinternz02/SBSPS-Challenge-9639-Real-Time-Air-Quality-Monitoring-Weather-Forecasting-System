from flask import Flask, render_template

app = Flask(__name__,template_folder="/Templates")
@app.route('/')
def Home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=False)
