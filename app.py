import os
from flask import Flask, render_template
from company_api import company_api
from contacts_api import contacts_api
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


@app.route("/create-tables")
def create_tables():
    db.create_all()
    return "Tables created!"

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/admin/companies")
def admin_companies():
    return render_template("admin/companies.html")


@app.route("/customer/new_order")
def customer_new_order():
    return render_template("customer/new_order.html")


@app.route("/customer/dashboard")
def customer_portal():
    return render_template("customer/dashboard.html")


@app.route("/engineer_portal")
def engineer_portal():
    return render_template("engineer/engineer_dashboard.html")


@app.route("/engineer/dashboard")
def engineer_dashboard():
    return render_template("engineer/engineer_dashboard.html")


@app.route("/engineer/training")
def engineer_training():
    return render_template("engineer/engineer_training.html")


@app.route("/engineer/resources")
def engineer_resources():
    return render_template("engineer/engineer_training.html")


@app.route("/admin/contacts")
def company_contacts():
    return render_template("admin/contacts.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)
