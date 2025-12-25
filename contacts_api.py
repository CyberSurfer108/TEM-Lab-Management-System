from flask import Blueprint, request, jsonify
from sql_models import db, CompanyContacts, Job_Roles, Teams, CompanyAccounts, Orders, Wafers, Chips, Lamellas, OrderLamella

contacts_api = Blueprint('contacts_api', __name__)
lamella_api = Blueprint('lamella_api', __name__)
orders_api = Blueprint('orders_api', __name__)

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

@orders_api.route('/order_submission', methods=['POST'])
def order_submission():
    
    data = request.get_json()
    
    # Create new order
    order = Orders(status_id=1, contact_id=data.get("customerId"))
    db.session.add(order)
    db.session.flush()
    order_id = order.id
    
    # Insert Wafer, Chip, and Lamella data
    for wafer in data["wafers"]:
        wafer_row = Wafers.query.filter_by(name=wafer["waferId"]).first()       
        if wafer_row:
            wafer_id = wafer_row.id
        else:
            wafer_row = Wafers(name=wafer["waferId"], contact_id=data.get("customerId"))          
            db.session.add(wafer_row)  
            db.session.flush()
            wafer_id = wafer_row.id
            
        for chip in wafer["chips"]:
            chip_row = Chips.query.filter_by(name=chip["chipId"], wafer_id=wafer_id).first()
            
            if chip_row:
                chip_id = chip_row.id
            else:
                chip_row = Chips(name=chip["chipId"], wafer_id=wafer_id)
                db.session.add(chip_row)
                db.session.flush()
                chip_id = chip_row.id
                
            for lamella in chip["lamellas"]:
                lamella_row = Lamellas(name=lamella["lamellaName"], chip_id=chip_id, status_id=1)
                db.session.add(lamella_row)
                db.session.flush()
                lamella_id = lamella_row.id
    
                # Assign lamellas to order in OrderLamella table
                order_lamella = OrderLamella(order_id=order_id, lamella_id=lamella_id)
                db.session.add(order_lamella)
                
    db.session.commit()
            
    return jsonify({
        "message": "Order submitted successfully.",
        "orderId": order_id,
        "waferId": wafer_id,
        "chipId": chip_id,
        "lamellaId": lamella_id})