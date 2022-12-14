from fileinput import filename
from traceback import print_exception
from unicodedata import category
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from datetime import datetime, date
from forms import Productform, Signup, Signin
from model import User, Product, Todo, db, app, admin_list 
import os

app.config['SECRET_KEY'] = 'sdfhsfhdafsafdweadwesadafnisufncisak68498resf'
bcrypt=Bcrypt(app)


@app.route('/')
def index():
    product_list = Product.query.all()
    return render_template('products.html', product_list=product_list)


@app.route('/addproducts', methods=['POST' , 'GET'])
def addproducts():
    # if session['role'] == 'admin':
        form= Productform()
        if form.validate_on_submit():
            pic = request.files["prod_picture"]
            filename = secure_filename(pic.filename)
            new_filename = filename
            save_location = os.path.join('static/files', new_filename)
            pic.save(save_location)
            new_product=Product(name=form.name.data,
                                description=form.description.data,
                                category=form.name.data,
                                price=form.price.data,
                                quantity=form.quantity.data,
                                availability=form.availability.data,
                                img_path="static/files/" + filename
                                )
            db.session.add(new_product)
            db.session.commit()
    # else:
    #     flash("You don't have the permission to add new items") 
    #     return redirect(url_for('products'))       
        product_list = Product.query.all()                        
        return render_template('addproducts.html', product_list=product_list, form=form)

@app.route('/deleteproduct/<int:id>')
def deleteproducts(id):
    delete=Product.query.filter_by(id=id).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for("addproducts"))        


@app.route('/products')
def products():
    product_list = Product.query.all()
    return render_template('products.html', product_list=product_list)       


@app.route('/signup', methods=['POST' , 'GET'])
def signup():
    registerForm = Signup() 
    if registerForm.validate_on_submit():
        if registerForm.email.data in admin_list:
            user_role='admin'
        else:
            user_role='user'
        # #name = registerForm.name.data
        session['name'] = registerForm.name.data
        # session['lastname'] = registerForm.surname.data
        # #session['email'] = registerForm.email.data
        # session['position'] = 'User'
        # session['age'] = registerForm.dob.data
        session['role'] = user_role
        password=registerForm.password.data
        password_2 = bcrypt.generate_password_hash(password)
        new_user=User(username=registerForm.email.data, 
                    name=registerForm.name.data,
                    last_name=registerForm.surname.data,
                    #   phone=registerForm.tel.data,
                    #   dateofbirthday=registerForm.dob.data,
                    #   position='User',
                    role=user_role,
                    password=password_2)            
        db.session.add(new_user)
        db.session.commit()
        #send_mail(registerForm.email.data, 'MagnusPitch Registration','mail', name= registerForm.name.data, username=registerForm.email.data, password=registerForm.password.data)
        return redirect(url_for('profile'))
    user_list=User.query.all()    
    return render_template('signup.html', registerForm=registerForm, user_list=user_list)


@app.route('/signin', methods=['GET', 'POST'])
def login():
    if session.get('name'):
        return redirect(url_for('profile'))
    else:
        login_form = Signin()
        if login_form.validate_on_submit():
            user_info = User.query.filter_by(username=login_form.username.data).first()
            if user_info and bcrypt.check_password_hash(user_info.password, login_form.password.data):
                session['user_id'] = user_info.id
                session['name'] = user_info.name
                session['lastname'] = user_info.last_name
                session['email'] = user_info.username
                session['role'] = user_info.role
                #session['age'] = user_info.dateofbirthday
                #session['position'] = user_info.position
                return redirect(url_for('profile'))
            flash('Invalid email or password')
        return render_template('signin.html', login_form=login_form,)

@app.route('/profile')
def profile():
    user=session.get('name')
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))
  

@app.route('/todo')
def todo():
    #show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('form.html', todo_list=todo_list)


@app.route('/db')
def database():   
    return send_from_directory('instance', 'db.sqlite')    


@app.route('/paypal')
def paypal():
    return redirect("https://paypal.me/marcopruiti?country.x=IT&locale.x=it_IT")


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