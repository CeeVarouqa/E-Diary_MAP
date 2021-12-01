import base64

from flask_restful import Api
from flask_jwt_extended import JWTManager
from app import app, resources, models, db
import os
from flask import flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from app.models import FileContent

api = Api(app)

# map urls with functions
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.Note, '/posts')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SoftwareArchitecture'

app.config['JWT_SECRET_KEY'] = 'kjgh234jht4h5hgkh'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

# work with tokens
jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/api/docs')
def get_docs():
    return render_template('swaggerui.html')


def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    data = file.read()
    render_file = render_picture(data)
    user_name = request.form['username']

    newFile = FileContent(name=file.filename, data=data, rendered_data=render_file, user_name=user_name)
    db.session.add(newFile)
    db.session.commit()

    flash(f'Pic {newFile.name}')

    return render_template('upload.html', data=list, image=base64.b64encode(newFile.data).decode('ascii'))


# Index It routes to index.html where the upload forms is
@app.route('/index', methods=['GET', 'POST'])
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get', methods=['GET', 'POST'])
def get():
    return render_template('get.html')


@app.route('/image', methods=['GET', 'POST'] )
def image():
    file_data = FileContent.query.filter_by(user_name='test1').first()
    image = base64.b64encode(file_data.data).decode('ascii')
    return render_template('upload.html', data=list, image=image)


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
