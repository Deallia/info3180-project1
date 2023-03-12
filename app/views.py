"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for,send_from_directory, flash
from werkzeug.utils import secure_filename
from .form import *
from .model import *


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Deallia Dunbar")


@app.route('/properties/create', methods=['POST', 'GET'])
def addproperty():
    """Render the website's new property form page."""
    form=PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title=form.title.data
            bedroomNo=form.bedroom.data
            bathroomNo=form.bathroom.data
            location=form.location.data
            price=form.price.data
            type=form.type.data
            description=form.description.data
            photo=form.photo.data
            filename = secure_filename(photo.filename) 
            photo.save(os.path.join(app.config['IMG_FOLDER'], filename))
            property = Property(title,bedroomNo,bathroomNo,location,price,type,description,filename)
            db.session.add(property)
            db.session.commit()
            flash("Property added Successfully", 'success')
            return redirect(url_for("displayproperties"))
    else:
        print("failed")
        return render_template('addproperty.html', form=form)
                           

@app.route('/properties')
def displayproperties():
    """Render the website's view properties page."""
    properties = db.session.execute(db.select(Property)).scalars()
    return render_template('properties.html', properties=properties)


@app.route('/<filename>')
def get_img(filename):
    # property=db.session.execute(db.select(Property).filter_by(id=propertyid)).scalar_one()
    # filename=property.photo
    return send_from_directory(os.path.join(os.getcwd(), app.config['IMG_FOLDER']), filename)
    

@app.route('/properties/<propertyid>') 
def viewproperty(propertyid):
    """Render the view property page."""
    property=db.session.execute(db.select(Property).filter_by(id=propertyid)).scalar_one()
    # property = db.get_or_404(Property, propertyid)
    return render_template('viewproperty.html', property=property)


    
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
