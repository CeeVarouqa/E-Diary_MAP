import datetime
from typing import List


def add_post(posts: List[dict], id: int, title: str, content: str, date_posted: datetime.datetime.date):
    posts.append({'id': id, 'title': title, 'content': content, 'date_posted': date_posted})
    return posts
