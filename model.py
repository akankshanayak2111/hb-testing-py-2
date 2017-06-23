from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.

    game_1 = Game(name='Ticket to Ride')
    game_2 = Game(name='Power Grid')
    game_3 = Game(name='Amazing Labyrinth')
    game_4 = Game(name='Princes of Florence')
    game_5 = Game(name='Agricola')

    db.session.add_all([game_1, game_2, game_3, game_4, game_5])
    db.session.commit()


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 