from sqlite3 import connect

from flask import Flask, render_template, g


app = Flask(__name__)

DATABASE = '/var/www/qotd/qotd.db'
SCHEMA = '/var/www/qotd/schema.sql'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db


def connect_db():
    return connect(DATABASE)


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    quote, username = None, None
    return render_template('index.html', quote=quote, username=username)


if __name__ == '__main__':
    app.run(debug=True)
