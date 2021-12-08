import json
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)


def test_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username and password fields are defined correctly
    """
    new_user = models.UserModel(
        username='alina',
        password=models.UserModel.generate_hash('12345')
    )
    assert new_user.username == 'alina'
    assert new_user.password != '12345'
    assert models.UserModel.verify_hash('12345', new_user.password)


def test_add_note():
    """
    GIVEN a Note model
    WHEN a new Note is created
    THEN check the title, body, user, edited, and datetime fields are defined correctly
    """
    user = models.UserModel(
        username='alina',
        password=models.UserModel.generate_hash('12345')
    )
    new_note = models.NoteModel(
        user_id=user.id,
        title="My title",
        body="My body",
        datetime=datetime.now(),
        edited=False
    )
    assert new_note.title == "My title"
    assert new_note.body == "My body"
    assert new_note.user_id == user.id
    assert datetime.now() > new_note.datetime > datetime.now() - timedelta(seconds=10)
    assert not new_note.edited


def test_add_Habit():
    """
    GIVEN a Habit model
    WHEN a new Habhit is created
    THEN check the title, user, datetime, and completed fields are defined correctly
    """
    user = models.UserModel(
        username='alina',
        password=models.UserModel.generate_hash('12345')
    )
    new_habit = models.HabitModel(
        user_id=user.id,
        title="My title",
        datetime=datetime.now(),
        completed=json.dumps([])
    )

    assert new_habit.title == "My title"
    assert new_habit.user_id == user.id
    assert datetime.now() > new_habit.datetime > datetime.now() - timedelta(seconds=10)
    assert new_habit.completed == json.dumps([])
