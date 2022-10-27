from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40))
    email = db.Column(db.String(100))


@app.route('/todo')
def todo():
    #show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('form.html', todo_list=todo_list)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/db')
def database():   
    return send_from_directory('instance', 'db.sqlite')    


@app.route('/paypal')
def paypal():
    return redirect("https://paypal.me/marcopruiti?country.x=IT&locale.x=it_IT")


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route("/add", methods=["POST"])
def add():
    #add new items
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    #update the item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("todo"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    #delete the item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo"))    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
