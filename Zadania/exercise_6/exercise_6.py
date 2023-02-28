from flask import Flask, request, render_template
from movies import movie

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/movies", methods=['GET', 'POST'])
def movies():

    if request.method == 'GET':

        return render_template('movies.html')

    elif request.method == 'POST':
        title = request.form.get("title")
        print(title)
        message = movie(title)[0]
        return render_template('movies.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)

