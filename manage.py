from app import app, db
from app.models import Game
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Game=Game)

if __name__ == '__main__':
    manager.run()
