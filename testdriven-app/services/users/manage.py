from flask.cli import FlaskGroup
from project.app import app, db

cli = FlaskGroup(app)

@cli.command()
def recreatedb():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def hello():
    print("Hello world")

if __name__ == '__main__':
    cli()
