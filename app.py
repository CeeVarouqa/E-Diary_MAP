import datetime
from flask import Flask, render_template, request

from posts import add_post

app = Flask(__name__)

app.config.from_pyfile('config.py')

posts = [
    {
        'title': 'Note 1',
        'content': 'This is my first note. I wrote it on 10th of October, 2021. It is a sample note. '
                   'It contains no meaning, but shows how my notes will look like. The end.',
        'date_posted': '2021-10-10'
    },
    {
        'title': 'Note 2',
        'content': 'Second note',
        'date_posted': '2021-10-15'
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
        titles = []
        for post in posts:
            titles.append(post["title"])
        if title in titles:
            return render_template('note.html', error="Note with such title already exists")
        if title == "":
            return render_template('note.html', error="You should fill the title field")
        new_posts = add_post(posts, id=len(posts), title=title, content=content, date_posted=datetime.datetime.now().date())
        return render_template('home.html', posts=new_posts)
    return render_template('note.html')


@app.route('/delete_note', methods=["POST"])
def delete_note():
    if request.method == 'POST':
        title = request.form['title']
        for post in posts:
            if post["title"] == title:
                posts.remove(post)
                break
        return render_template('home.html', posts=posts)

