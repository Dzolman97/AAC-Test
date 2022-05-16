from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
   return render_template("home.html")

@views.route('/about-us')
def aboutUs():
   return render_template("aboutUs.html")

@views.route('/special-offers')
def specialOffers():
   return render_template("specialOffers.html")

@views.route('/gallery')
def gallery():
   return render_template("gallery.html")

@views.route('/location')
def location():
   return render_template("location.html")

@views.route('/contact-us')
def contact():
   return render_template("contact.html")

@views.route('/testimonials')
def testimonials():
   return render_template("testimonials.html")