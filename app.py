import os
from flask import Flask, render_template
from company_api import company_api
from contacts_api import contacts_api, orders_api
from sql_models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    "sqlite:///tem_lms_temp.db"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(company_api)
app.register_blueprint(contacts_api)
app.register_blueprint(orders_api)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/companies")
def companies():
    return render_template("engineer/companies.html")

@app.route("/contacts")
def company_contacts():
    return render_template("engineer/contacts.html")

@app.route("/new_order")
def new_order():
    return render_template("engineer/new_order.html")


@app.route("/customer/dashboard")
def customer_portal():
    return render_template("customer/dashboard.html")


@app.route("/orders")
def orders():
    return render_template("engineer/orders.html")

@app.route("/engineer_portal")
def engineer_portal():
    return render_template("engineer/orders.html")

@app.route("/training")
def training():
    return render_template("engineer/engineer_training.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)
