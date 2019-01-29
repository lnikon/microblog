from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bach'}
    posts = [
        {
            'author': 'Coil',
            'title': 'System Viewer',
            'type': {'album': 'EP'}
        },
        {
            'author': 'Metallica',
            'title': 'Black Album',
            'type': {'album': 'Full'}
        }
    ]
    return render_template('index.html', title='Home', user=user,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect(url_form('index'))
    return render_template('login.html', title='Login Page', form=login_form)
