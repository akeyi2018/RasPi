from __future__ import print_function
from flask_script import Manager
from flaskr import app, db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug=True)
    manager.run()


