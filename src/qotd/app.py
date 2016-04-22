from flask import Flask, render_template, g, request
from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker

from models import Base, Quote

app = Flask(__name__)

DATABASE = '/var/www/qotd/qotd.db'


def get_engine():
    engine = getattr(g, '_engine', None)
    if engine is None:
        engine = g._engine = create_engine('sqlite+pysqlite:///%s' % DATABASE, module=sqlite)
    return engine


def init_db():
    with app.app_context():
        engine = get_engine()
        Base.metadata.create_all(engine)


def get_session():
    Session = getattr(g, '_Session', None)
    if Session is None:
        Session = g._Session = sessionmaker(bind=get_engine())
    return Session()


def query_db():
    session = get_session()
    quote = session.query(Quote).order_by(func.random()).first()
    session.close()
    return quote


def add_db(author, insight):
    session = get_session()
    quote = Quote(author=author, insight=insight)
    session.add(quote)
    session.commit()
    return quote


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        pass
        # db.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        quote = query_db()
        if not quote:
            quote = Quote(author='QOTD', insight='POST here to add your quote')
        return render_template('index.html', quote=quote.insight, username=quote.author)
    else:
        try:
            data = request.get_json()
            if data is None or 'author' not in data or 'insight' not in data:
                raise ValueError('POST application/json data with author and insight')
            quote = add_db(author=data['author'], insight=data['insight'])
        except Exception as e:
            quote = Quote(author='QOTD', insight=str(e))
        return render_template('index.html', quote=quote.insight, username=quote.author)


init_db()

if __name__ == '__main__':
    app.run(debug=True)
