import json
from datetime import datetime

from flask import jsonify
from passlib.hash import pbkdf2_sha256 as sha256
from app import db


class UserModel(db.Model):
    """
    Model for User
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
        """
        saves user to db
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """
        finds user by specified username
        :param username: login/username of a user to find
        :return: object of User model
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        """
        function to get all users from db
        :return:
        """

        def to_json(x):
            """
            transfers User to json format
            :param x: User
            :return: json object with User's username and password
            """
            return {
                'username': x.username,
                'password': x.password
            }

        return {'users': list(
            map(lambda x: to_json(x), UserModel.query.all()))}

    @staticmethod
    def generate_hash(password):
        """
        generates has from the password
        :param password: password that will be hashed
        :return: hash
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """
        checks if hash is correspond to the password
        :param password: password to check
        :param hash: hash to check
        :return: boolean
        """
        return sha256.verify(password, hash)


class RevokedTokenModel(db.Model):
    """
    Model for revoked tokens
    """
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        """
        adds token to the db
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)


class NoteModel(db.Model):
    """
    Model for Notes
    """
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, name='user_id')
    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    datetime = db.Column(db.String(30), nullable=True)
    edited = db.Column(db.Boolean, nullable=False)

    def add(self):
        """
        Adds note to the db
        :return:
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_ids(cls, id):
        """
        Find note by id
        :param id: note id
        :return: Note object
        """
        return db.session.query(cls).filter(cls.id == id).first()

    @classmethod
    def find_by_date(cls, date, username):
        """
        Find notes by date for specified user
        :param date: note date
        :param username: username of the user
        :return: Notes objects
        """

        def to_json(x):
            return {
                'id': x.id,
                'title': x.title,
                'body': x.body,
                'datetime': x.datetime,
                'edited': x.edited
            }

        user_id = UserModel.find_by_username(username).id
        return {
            "{}'s notes for {}".format(username, date): list(
                map(lambda x: to_json(x),
                    db.session.query(cls).filter(cls.datetime.contains(date), cls.user_id == user_id).all())
            )
        }
      
    @classmethod
    def return_all(cls, username):
        """
        get all notes of the user
        :param username: username of the user
        :return: Notes objects
        """

        def to_json(x):
            return {
                'id': x.id,
                'title': x.title,
                'body': x.body,
                'datetime': x.datetime,
                'edited': x.edited
            }

        user_id = UserModel.find_by_username(username).id

        return {"{}'s notes".format(username): list(map(lambda x: to_json(
            x), db.session.query(cls).filter(cls.user_id == user_id).all()))}

    @classmethod
    def delete_note(cls, id):
        """
        Deletes note with specified id
        :param id: note id
        :return: message
        """
        note = db.session.query(cls).filter(cls.id == id).first()
        db.session.delete(note)
        db.session.commit()
        return {'message': 'Note was successfully deleted'}

    @classmethod
    def edit_note(cls, id, title, text):
        """
        Method to edit note with specified id
        :param id: note id
        :param title: if new note title is specified then the old one will be replaced by it
        :param text: if new note text is specified then the old one will be replaced by it
        :return: message
        """
        db.session.query(cls).filter(cls.id == id). \
            update({'title': title, 'body': text, 'edited': 1})
        db.session.commit()
        return {'message': 'Note was successfully edited'}

# Picture table. By default the table name is filecontent


class FileContent(db.Model):
    """
    The first time the app runs you need to create the table. In Python
    terminal import db, Then run db.create_all()
    """
    """ ___tablename__ = 'yourchoice' """  # You can override the default table name

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)  # Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)  # Data to render the pic in browser
    pic_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Pic Name: {self.name} Data: {self.data} '


class HabitModel(db.Model):
    __tablename__ = 'habits'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, name='user_id')
    title = db.Column(db.String(30), nullable=False)
    datetime = db.Column(db.String(30), nullable=False)
    completed = db.Column(db.Text, nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_creation_date(cls, date, username):
        def to_json(x):
            return {
                'id': x.id,
                'title': x.title,
                'datetime': x.datetime,
                'completed': x.completed
            }

        user_id = UserModel.find_by_username(username).id
        return {
            "{}'s created habits for {}".format(username, date): list(
                map(lambda x: to_json(x),
                    db.session.query(cls).filter(cls.datetime.contains(date), cls.user_id == user_id).all())
            )
        }

    @classmethod
    def find_by_completion_date(cls, date, username):
        def to_json(x):
            return {
                'id': x.id,
                'title': x.title,
                'datetime': x.datetime,
                'completed': x.completed
            }

        user_id = UserModel.find_by_username(username).id
        habits = []
        for habit in db.session.query(cls).filter(cls.user_id == user_id).all():
            completed = json.loads(habit.completed)
            if date in completed:
                habits.append(to_json(habit))

        jsonify(habits)

        return {
            "{}'s completed habits for {}".format(username, date): habits
        }

    @classmethod
    def find_by_ids(cls, habit_id):
        return db.session.query(cls).filter(cls.id == habit_id).first()

    @classmethod
    def return_all(cls, username):
        def to_json(x):
            return {
                'id': x.id,
                'title': x.title,
                'datetime': x.datetime,
                'completed': x.completed
            }

        user_id = UserModel.find_by_username(username).id

        return {
            "{}'s habits".format(username): list(
                map(lambda x: to_json(x), db.session.query(cls).filter(cls.user_id == user_id).all())
            )
        }

    @classmethod
    def add_completed_date(cls, habit_id, date):
        db.session.query(cls).filter(cls.id == habit_id).update({'completed': date})
        db.session.commit()
        return {'message': 'Habit was completed'}

    @classmethod
    def delete_habit(cls, habit_id):
        habit = db.session.query(cls).filter(cls.id == habit_id).first()
        db.session.delete(habit)
        db.session.commit()
        return {'message': 'Habit was successfully deleted'}
