from flask import Blueprint, request, jsonify
from sql_models import db, CompanyAccounts, Addresses

company_api = Blueprint('company_api', __name__)


# <---------Create Company Accounts------->


@company_api.route("/new_company_account", methods=["POST"])
def new_company_account():
    # Extract data from the request
    data = request.get_json()

    # Process company data first
    new_company = CompanyAccounts(
        name=data.get("name"),
        status_id=int(data.get("status")),
        email=data.get("email"),
        phone=data.get("phone")
    )
    # Add and commit the new company to get its ID
    db.session.add(new_company)
    db.session.commit()

    # Process address data
    new_address = Addresses(
        company_id=new_company.id,
        street=data.get("street"),
        city=data.get("city"),
        state=data.get("state"),
        zip=data.get("zip")
    )

    db.session.add(new_address)
    db.session.commit()
    return jsonify({"message": "New company account created successfully."}), 201


# <---------Read Company Accounts------->


@company_api.route('/company_accounts', methods=['GET'])
def get_company_accounts():

    companies = (CompanyAccounts.query.all())
    return jsonify([company.to_dict() for company in companies])


# <---------Update Company Accounts------->

@company_api.route("/update_company_account", methods=['POST'])
def update_company_account():
    data = request.get_json()

    company = CompanyAccounts.query.get_or_404(data.get("id"))
    company.name = data.get("name")
    company.status_id = int(data.get("status"))
    company.email = data.get("email")
    company.phone = data.get("phone")

    address = Addresses.query.filter_by(company_id=company.id).first()
    address.street = data.get("street")
    address.city = data.get("city")
    address.state = data.get("state")
    address.zip = data.get("zip")

    db.session.commit()

    return jsonify({"message": "Company account updated successfully."}), 200


# <---------Delete Company Accounts------->

@company_api.route("/delete_company_account", methods=['POST'])
def delete_company_account():
    data = request.get_json()

    company = CompanyAccounts.query.get_or_404(data.get("id"))
    address = Addresses.query.filter_by(company_id=company.id).first()
    db.session.delete(company)
    db.session.delete(address)
    db.session.commit()
    return jsonify({"message": "Company account deleted successfully."}), 200
