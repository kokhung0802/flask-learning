from flask import Flask, render_template, url_for

# __name__ is a special variable, __name__ is __main__ if run with python directly
app = Flask(__name__)

posts = [{
    'author': 'ckh',
    'date_posted': '21 Jan',
    'title': 'good news',
    'content': 'there is a new movie'
},
    {
    'author': 'thj',
    'date_posted': '26 Dec',
    'title': 'bad news',
    'content': 'Japan is fun'
}]


@app.route("/")  # decorators: add extra functionalities to functions
def hello():
    return render_template('home.html', posts=posts)  # posts: created variable


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
