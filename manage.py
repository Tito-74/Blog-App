from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
from app.models import Like, Quotes,Comment,Post,User


# creating app instance
app = create_app('production')
# app = create_app('production')


migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)


@manager.command



def test():

    """
    Run the unit tests.

    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Quotes=Quotes,Comment=Comment, Post=Post, User=User,Like=Like) 

if __name__ == '__main__':
    manager.run()