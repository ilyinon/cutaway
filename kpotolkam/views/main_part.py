from flask import *
from werkzeug.utils import secure_filename
#from ..models import engine, Model, District, Image

#from sqlalchemy.engine import Engine
#from sqlalchemy.orm import sessionmaker, class_mapper
#from sqlalchemy.sql.expression import func

#Session = sessionmaker(bind=engine)

#db_session = Session()
from flask_mail import Mail, Message



import uuid
import os

from kpotolkam import app



UPLOAD_FOLDER = '/tmp/web_file'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():

#  userList = db_session.query(Model.id, Model.name, Model.age, District.name, Image.filename).\
#             join(District, Model.district ==  District.id).\
#             join(Image, Model.id == Image.model_id).group_by(Model.id).limit(5).all()

  return render_template('index.html')

@app.route('/contact', methods=('GET', 'POST'))
def contact():
  return render_template('contact.html')

@app.route('/ceiling')
def ceiling():
  return render_template('ceiling.html')

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

@app.route('/price')
def price():
  return render_template('price.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/options')
def options():
  return render_template('options.html')

@app.route('/spot')
def spot():
  return render_template('spot.html')

@app.errorhandler(404)
def page_not_found(e):
  return redirect(url_for('index'))

