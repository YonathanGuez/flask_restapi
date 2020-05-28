
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

DBUSER = 'test'
DBPASS = 'test'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'testdb'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'test'


db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))

    def __init__(self, name, city, addr):
        self.name = name
        self.city = city
        self.addr = addr


def database_initialization_sequence():
    db.create_all()
    test_rec = users(
            'John Doe',
            'Los Angeles',
            '123 Foobar Ave')

    db.session.add(test_rec)
    db.session.rollback()
    db.session.commit()

@app.route('/user', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            user = users(
                    request.form['name'],
                    request.form['city'],
                    request.form['addr'])

            db.session.add(user)
            db.session.commit()
            flash('Record was succesfully added')
            return redirect(url_for('home'))
    return render_template('show_all.html', users=users.query.all())

# Rooting
@app.route('/')
def hello_world():
    return 'Hello, World!'