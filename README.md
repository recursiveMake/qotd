# Quote-of-the-Day
Quote of the day provides inspiring, beautiful quotes from a world-wide community.
Loosely based on [Quote-of-the-Day](https://github.com/der-Daniel/Quote-of-the-Day)
Anyone can post new quotes. This should be restricted.


### Requirement
-  [Flask](http://flask.pocoo.org/)
-  [SQLAlchemy](http://www.sqlalchemy.org/)
-  [Apache](https://httpd.apache.org/)


### Installation
```
python setup.py install
a2ensite qotd_host
a2dissite default  # Optional
service apache2 reload
```

### Usage
```
curl -H "Content-Type: application/json" -X POST -d '{"author": "me", "insight": "A brilliant quote"}' http://localhost/
```
