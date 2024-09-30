from flask import render_template, flash, redirect, url_for
from app import app
from .forms import *
from .models import Property
from app import db

# The main webpage
@app.route('/')
def index():
    user = {'name': 'Homer Simpson'}
    return render_template('index.html',
                           title='Simple template example',
                           user=user)
    
@app.route('/fruit')
def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruit.html",fruits=fruits)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash('Succesfully received form data. %s + %s  = %s'%(form.number1.data, form.number2.data, form.number1.data+form.number2.data))
    return render_template('calculator.html',
                           title='Calculator',
                           form=form)
 
  
    
@app.route('/property', methods=['GET', 'POST'])
def property():
    form = PropertyForm()
    if form.validate_on_submit():
        # Create a new Property instance from form data
        new_property = Property(
            address=form.address.data,
            start_date=form.start_date.data,  # Assuming this is a DateField
            duration=form.duration.data,
            rent=form.rent.data
        )
        
        # Add the new property to the database
        db.session.add(new_property)
        db.session.commit()  # Save the changes to the database
        
        flash('Successfully received and saved form data.')
        return redirect(url_for('property'))  # Redirect after successful submission
    
    return render_template('property.html', title='Property', form=form)