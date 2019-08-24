from flask import Flask,render_template,request,redirect,url_for,session
from model  import check_user,add_user_Todb

app = Flask(__name__)

app.secret_key = 'hello'

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html',title = 'home')

@app.route('/about')
def about():
	return render_template('about.html',title='about')	

@app.route('/contact')
def contact():
	return render_template('contact.html',title='contact')


@app.route('/signup',methods=['GET','POST'])
def signup():
	
	if request.method == 'POST':

		userinfo = {}

		userinfo['username'] = request.form['username']
		userinfo['fullname'] = request.form['fullname']
		userinfo['password'] = request.form['password1']
		password2 = request.form['password2']
		userinfo['email'] = request.form['email']
		userinfo['type'] = request.form['type']

		if userinfo['password'] != password2:
			return "Password fields dint mantch"

		if bool(check_user(userinfo['username'])) is True:
			return "user already exists.try logging in"


		add_user_Todb(userinfo)
		return redirect(url_for('home'))

	return redirect(url_for('home'))


			



@app.route('/login',methods = ['GET','POST'])
def login():

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if bool(check_user(username)) and (check_user(username)['password']==password):
		# if bool(check_user(username)) and (check_user(username)['password']==password):
			session['username'] = username
			session['type'] = check_user(username)['type']
			return redirect(url_for('about'))
		return "username or password is in correct"

	return redirect(url_for('home'))


# @app.route('/login',methods =['GET','POST'])
# def login():
	
# 	if request.method =='POST':

# 		db = {'newuser' :'12345','Testuser':'12345'}


# 		username = request.form['username']
# 		password = request.form['password']

# 		if username in db and db[username] == password:

# 			return redirect(url_for('about'))
# 		return "username and password is incorrect"


if __name__ == '__main__':
	app.run(debug = True)