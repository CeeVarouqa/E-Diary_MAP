import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_pyfile('config.py')

posts = [
    {
        'title': 'Note 1',
        'content': 'First note',
        'date_posted': '5 November, 2021'
    },
    {
        'title': 'Note 2',
        'content': 'Second note',
        'date_posted': '7 November, 2021'
    }
]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/add_note', methods=["POST", "GET"])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content, 'date_posted': datetime.datetime.now().date()})
        return render_template('home.html', posts=posts)
    return render_template('note.html')

