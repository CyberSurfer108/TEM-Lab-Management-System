from flask import Blueprint, request, jsonify
from sql_models import db, CompanyContacts, Job_Roles, Teams, CompanyAccounts, Coating

contacts_api = Blueprint('contacts_api', __name__)
lamella_api = Blueprint('lamella_api', __name__)

''' 
=========================================================
    Contact API's 
========================================================= 
'''
# <---------Create Contacts------->

@contacts_api.route("/new_contact", methods=["POST"])
def new_contact_account():
    # Extract data from the request
    data = request.get_json()

    # Process contact data first
    new_contact = CompanyContacts(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        company_id=data.get("company_id"),
        status_id=int(data.get("status")),
        email=data.get("email"),
        phone=data.get("phone"),
        job_role_id=data.get("job_role_id"),
        team_id=data.get("team_id")
    )
    # Add and commit the new company to get its ID
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": "New contact account created successfully."}), 201


# <---------Read Contact List------->

@contacts_api.route('/contact_accounts', methods=['GET'])
def get_contact_accounts():

    contacts = (CompanyContacts.query.all())
    return jsonify([contact.to_dict() for contact in contacts])


# <---------Read Job Roles------->

@contacts_api.route('/contact_accounts/job_roles', methods=['GET'])
def get_job_roles():

    job_roles = (Job_Roles.query.all())
    return jsonify([job_role.to_dict() for job_role in job_roles])


# <---------Read Teams------->

@contacts_api.route('/contact_accounts/teams', methods=['GET'])
def get_teams():

    teams = (Teams.query.all())
    return jsonify([team.to_dict() for team in teams])


# <---------Read Companies------->

@contacts_api.route('/contact_accounts/companies', methods=['GET'])
def get_companies():

    companies = (CompanyAccounts.query.all())
    return jsonify([company.to_dict() for company in companies])


# <---------Update Contact Account------->

@contacts_api.route("/update_contact", methods=['POST'])
def update_contact():
    data = request.get_json()

    # Get original contact information
    contact = CompanyContacts.query.get_or_404(data.get("id"))

    # Update contacts information
    contact.first_name = data.get("first_name")
    contact.last_name = data.get("last_name")
    contact.email = data.get("email")
    contact.phone = data.get("phone")
    contact.company_id = data.get("company_id")
    contact.status_id = int(data.get("status"))
    contact.job_role_id = data.get("job_role_id")
    contact.team_id = data.get("team_id")

    db.session.commit()

    return jsonify({"message": "Company account updated successfully."}), 200


# <---------Delete Contact Account------->

@contacts_api.route("/delete_contact", methods=['POST'])
def delete_contact():
    data = request.get_json()
    contact = CompanyContacts.query.get_or_404(data.get("id"))

    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted successfully."}), 200


''' 
=========================================================
    Lamella API's
========================================================= 
'''
# <---------Read Coatings------->

@lamella_api.route('/lamellas/coatings', methods=['GET'])
def get_coatings():

    coatings = (Coating.query.all())
    return jsonify([coating.to_dict() for coating in coatings])