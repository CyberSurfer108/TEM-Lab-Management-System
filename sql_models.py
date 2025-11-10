from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# <----------- Company Accounts Models ------------>


class CompanyAccounts(db.Model):
    __tablename__ = 'company_accounts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'account_status.id'), nullable=False)
    status = db.relationship('AccountStatus', backref='company_accounts')
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status.status,
            'status_id': self.status_id,
            'email': self.email,
            'phone': self.phone,
            'addresses': [
                address.to_dict() for address in self.addresses
            ]
        }

    def __repr__(self):
        return f'<CompanyAccount {self.name}>'


class AccountStatus(db.Model):
    __tablename__ = 'account_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<AccountStatus {self.status}>'


class Addresses(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company_accounts.id'), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip = db.Column(db.String(20), nullable=False)
    company = db.relationship('CompanyAccounts', backref='addresses')

    def to_dict(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip': self.zip
        }

    def __repr__(self):
        return f'<Address {self.street}, {self.city}, {self.state}, {self.zip}>'


# <----------- Company Contact Models ------------>
class CompanyContacts(db.Model):
    __tablename__ = 'company_contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(75), nullable=False)
    last_name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('Teams.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company_accounts.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'account_status.id'), nullable=False)
    job_role_id = db.Column(db.Integer, db.ForeignKey(
        'job_roles.id'), nullable=False)

    company = db.relationship('CompanyAccounts', backref='company_contacts')
    status = db.relationship('AccountStatus', backref='company_contacts')
    job_role = db.relationship('Job_Roles', backref='company_contacts')
    teams = db.relationship('Teams', backref='company_contacts')

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'status': self.status.status,
            'status_id': self.status_id,
            'email': self.email,
            'phone': self.phone,
            'company_id': self.company_id,
            'company': self.company.name,
            'job_role_id': self.job_role_id,
            'job_role_name': self.job_role.name,
            'team_id': self.team_id,
            'team_name': self.teams.name
        }


class Job_Roles(db.Model):
    __tablename__ = 'job_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Teams(db.Model):
    __tablename__ = 'Teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,

        }


# <----------- Sample Models ------------>

class OrderStatus(db.Model):
    __tablename__ = 'order_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Grids(db.Model):
    __tablename__ = 'grids'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Coating(db.Model):
    __tablename__ = 'coating'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Wafers(db.Model):
    __tablename__ = 'wafers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey(
        'contact_accounts.id'), nullable=False)

    contact = db.relationship('ContactAccounts', backref='wafers')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact_id': self.contact_id,
            'contact_fname': self.contact.first_name,
            'contact_lname': self.contact.last_name
        }


class Chips(db.Model):
    __tablename__ = 'chips'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    wafer_id = db.Column(db.Integer, db.ForeignKey(
        'wafers.id'), nullable=False)

    wafer = db.relationship('Wafers', backref='chips')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'wafer_id': self.wafer_id
        }


class Lamellas(db.Model):
    __tablename__ = 'lamellas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chips.id'), nullable=False)
    coating_id = db.Column(
        db.Integer, db.ForeignKey('coating.id'), nullable=True)
    completion_date = db.Column(db.DateTime, nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    grid_id = db.Column(db.Integer, db.ForeignKey('grids.id'), nullable=True)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'order_status.id'), nullable=False)

    chip = db.relationship('Chips', backref='lamellas')
    status = db.relationship('OrderStatus', backref='lamellas')
    grid = db.relationship('Grids', backref='lamellas')
    coating = db.relationship('Coating', backref='lamellas')

    def to_dict(self):

        return {
            'id': self.id,
            'name': self.name,
            'chip_id': self.chip_id,
            'wafer_name': self.chip.wafer.name,
            'coating_id': self.coating_id,
            'coating_name': self.coating.name if self.coating else None,
            'completion_date': self.completion_date,
            'start_date': self.start_date,
            'grid_id': self.grid_id,
            'grid_name': self.grid.name if self.grid else None,
            'status': self.status.name

        }
