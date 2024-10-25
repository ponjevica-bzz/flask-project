from flask import Flask, render_template, redirect, url_for

from dao.car_dao import CarDao
from forms import CarForm
from models.car import Car

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
car_dao = CarDao('cars.db')


@app.route('/')
def list_cars():
    # B1G: Simple algorithm to list all cars from the database
    cars = car_dao.get_all_cars()
    return render_template('list_cars.html', cars=cars)


@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    form = CarForm()
    if form.validate_on_submit():
        # A1G: Demonstrates a pure function to construct the car object
        car = Car(None, form.make.data, form.model.data, form.year.data)
        car_dao.add_car(car)
        return redirect(url_for('list_cars'))

    return render_template('add_car.html', form=form)  # Pass form object to template


@app.route('/delete/<int:car_id>')
def delete_car(car_id):
    car_dao.delete_car(car_id)
    return redirect(url_for('list_cars'))


if __name__ == '__main__':
    car_dao.create_table()
    app.run(debug=True)
