import json
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from app import models
from datetime import datetime, timedelta

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
