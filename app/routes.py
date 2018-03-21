from app import app, db
from flask import render_template, flash, redirect, request, url_for
from app.forms import EditProfileForm, LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from datetime import datetime
from functools import wraps
from flask_login import LoginManager

def login_required(role):
	def wrapper(fn):
		@wraps(fn)
		def decorated_view(*args, **kwargs):
			if not current_user.is_authenticated:
				return redirect(url_for('login',next=request.url))	
			urole = current_user.get_urole()
			if  (urole < role) :
				return current_app.login_manager.unauthorized()
			return fn(*args, **kwargs)
		return decorated_view
	return wrapper

@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html',title ='Home')
	
@app.route('/manager')
@login_required(4)
def manager():

	return render_template('managers/manager.html',title = 'Manager')

@app.route('/cook')
@login_required(3)
def cook():

	return render_template('cooks/cook.html',title = 'Cook')

@app.route('/delivery')
@login_required(2)
def delivery():

	return render_template('deliveries/delivery.html',title = 'Delivery')

@app.route('/map')
@login_required(2)
def map():
	
	return render_template('deliveries/map.html')


@app.route('/prices')
@login_required(3)
def prices():
	
	return render_template('cooks/prices.html')

@app.route('/cookcustorder')
@login_required(3)
def cookcustorder():

	return render_template('cooks/cookcustorder.html')

@app.route('/complaints')
@login_required(4)
def complaints():
	
	return render_template('managers/complaints.html')

@app.route('/payroll')
@login_required(4)
def payroll():
	
	return render_template('managers/payroll.html')

@app.route('/login', methods = ['GET','POST'])
def login():
	if current_user.is_authenticated:
		if current_user.urole == 4:
			return redirect(url_for('manager'))
		if current_user.urole == 3:
			return redirect(url_for('cook'))
		if current_user.urole == 2:
			return redirect(url_for('delivery'))
		else:
			return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			if current_user.urole == 4:
				next_page = url_for('manager')
			elif current_user.urole == 3:
				next_page = url_for('cook')
			elif current_user.urole == 2:
				next_page = url_for('delivery')
			else:
				next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html',title='Sign In', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register',methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		if current_user.urole == 4:
			return redirect(url_for('manager'))
		if current_user.urole == 3:
			return redirect(url_for('cook'))
		if current_user.urole == 2:
			return redirect(url_for('delivery'))
		else:
			return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data, urole = 1)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)
		
		
@app.route('/user/<username>')
@login_required(role=1)
def user(username):
	user = User.query.filter_by(username=username).first_or_404()

	return render_template('user.html', user=user)

@app.route('/menu')
def menu():
	
	return render_template('menu.html',title ='Menu')

@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@app.route('/edit_profile', methods=['GET','POST'])
@login_required(role=1)
def edit_profile():
	form = EditProfileForm(current_user.username)
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash('Your changes have been saved')
		return redirect(url_for('edit_profile'))

	elif request.method == 'GET':
		form.username.data = current_user.username
		form.about_me.data = current_user.about_me

	return render_template('edit_profile.html', title='Edit Profile', form=form)