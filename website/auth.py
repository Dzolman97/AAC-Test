from flask import Blueprint, render_template
from .forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/admin_login')
def login():
   form = LoginForm()
   return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
   return "<p>Logout</p>"