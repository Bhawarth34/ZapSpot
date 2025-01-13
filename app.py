from flask import Flask, render_template

app = Flask(__name__)


@app.get('/')
def getHome():
    return render_template("index.html")

@app.get('/locator')
def getLocate():
    return render_template("locate.html")

if __name__ == '__main__':
    app.run(debug = True)
