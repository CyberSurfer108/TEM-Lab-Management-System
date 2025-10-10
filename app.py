from flask import Flask, render_template
from company_api import company_api
from contacts_api import contacts_api
from sql_models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Anthony:@localhost/FIB Lab Management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(company_api)
app.register_blueprint(contacts_api)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/admin/companies")
def admin_companies():
    return render_template("admin/companies.html")


@app.route("/customer/new_order")
def customer_portal():
    return render_template("customer/new_order.html")


@app.route("/engineer_portal")
def engineer_portal():
    return render_template("engineer/engineer_operations.html")


@app.route("/admin/contacts")
def company_contacts():
    return render_template("admin/contacts.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)
