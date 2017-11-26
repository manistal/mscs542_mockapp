from mockapp import create_app

from flask import current_app as app
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
from werkzeug.contrib.profiler import ProfilerMiddleware

manager = Manager(create_app)

# Running Application Context
# ===========================
@manager.option('-p', '--port', help='The port to run the server on.', required=False, dest='port', default=5000)
def runserver(port):
    app.run('127.0.0.1', port=int(port))

@manager.shell
def make_shell_context():
    return dict(app=app)#,db=db,models=models)

if __name__ == '__main__':
    manager.run()

