from flask import Flask, jsonify, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("Cafe location on google Map(URL)", validators=[DataRequired(), URL()])
    img_url = StringField("Picture of the cafe (URL)", validators=[DataRequired(), URL()])
    location = StringField('Location name', validators=[DataRequired()])
    seats = StringField('Number of seat', validators=[DataRequired()])
    has_toilet = RadioField('Toilet Available?', choices=[(1,'Yes'),(0,'No')], coerce=int)
    has_sockets = RadioField('Plugs Available?', choices=[(1,'Yes'),(0,'No')], coerce=int)
    has_wifi = RadioField('Wifi Available?', choices=[(1,'Yes'),(0,'No')], coerce=int)
    can_take_calls = RadioField('Can make Call?', choices=[(1,'Yes'),(0,'No')], coerce=int)
    coffee_price = StringField('Average Coffee price', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    print([cafe.to_dict() for cafe in all_cafes])
    return render_template('cafes.html', cafes=[cafe.to_dict() for cafe in all_cafes])


# @app.route("/search")
# def get_cafe_at_location():
#     query_location = request.args.get("loc")
#     result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
#     # Note, this may get more than one cafe per location
#     all_cafes = result.scalars().all()
#     if all_cafes:
#         return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
#     else:
#         return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# Test this inside Postman. Request type: Post ->  Body ->  x-www-form-urlencoded
@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=bool(form.has_sockets.data),
            has_toilet=bool(form.has_toilet.data),
            has_wifi=bool(form.has_wifi.data),
            can_take_calls=bool(form.can_take_calls.data),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect('cafes')
    return render_template('add.html', form=form)


# # Updating the price of a cafe based on a particular id:
# # http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
# @app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
# def patch_new_price(cafe_id):
#     new_price = request.args.get("new_price")
#     cafe = db.get_or_404(Cafe, cafe_id)
#     if cafe:
#         cafe.coffee_price = new_price
#         db.session.commit()
#         return jsonify(response={"success": "Successfully updated the price."}), 200
#     else:
#         return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# # Deletes a cafe with a particular id. Change the request type to "Delete" in Postman
@app.route("/report-closed/<int:cafe_id>", methods=["POST"])
def delete_cafe(cafe_id):
        cafe_to_delete = int(cafe_id)
        cafe = db.get_or_404(Cafe, cafe_to_delete)
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for('cafes'))



if __name__ == '__main__':
    app.run(debug=True)
