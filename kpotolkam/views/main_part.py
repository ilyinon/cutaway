from flask import *
from werkzeug.utils import secure_filename
#from ..models import engine, Model, District, Image

#from sqlalchemy.engine import Engine
#from sqlalchemy.orm import sessionmaker, class_mapper
#from sqlalchemy.sql.expression import func

#Session = sessionmaker(bind=engine)

#db_session = Session()


import uuid
import os

from cutaway import app



UPLOAD_FOLDER = '/tmp/web_file'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def show_models():

#  userList = db_session.query(Model.id, Model.name, Model.age, District.name, Image.filename).\
#             join(District, Model.district ==  District.id).\
#             join(Image, Model.id == Image.model_id).group_by(Model.id).limit(5).all()

  return render_template('main_page.html')

#@app.route('/add', methods=['POST'])
#def add_model():
#  if not session.get('logged_in'):
#    abort(401)

#  new_model = Model(name     = request.form['name'], 
#                    age      = request.form['age'],
#                    district = request.form['district'] 
#  )
#  db_session.add(new_model)
#  db_session.commit()
#
#  flash('New model was successfully posted')
#  return redirect(url_for('show_models'))


