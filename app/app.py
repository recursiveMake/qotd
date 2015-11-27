from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
sys.path.insert(0,"/var/www/html/qotd")

from app import quote as q


app = Flask(__name__)

@app.route('/')
def home():
	(quote, username) = q.get_quote()
	return render_template('index.html', quote=quote, username=username)





if __name__ == '__main__':
    app.run(debug=True)
