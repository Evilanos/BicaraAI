from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Evilanos:Galileo123@localhost/userdata'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{ 'email': user.email, 'firstname': user.firstname, 'lastname': user.lastname } for user in users])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    email = data['email']
    firstname = data['firstname']
    lastname = data['lastname']

    new_user = User(email=email, firstname=firstname, lastname=lastname)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added successfully!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

