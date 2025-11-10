from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# <----------- Company Accounts Models ------------>

class CompanyAccounts(db.Model):
    # DB Table data will map to
    __tablename__ = 'company_accounts'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    name   = db.Column(db.String(100),  unique=True, nullable=False)
    email  = db.Column(db.String(100),               nullable=False)
    phone  = db.Column(db.String(20),                nullable=False)
    
    # Foreign Keys
    status_id = db.Column(db.Integer, db.ForeignKey('account_status.id'), nullable=False)
    
    # links to FK Tables
    status = db.relationship('AccountStatus', backref='company_accounts')
    

    def to_dict(self):
        return {
            'id':        self.id,
            'name':      self.name,
            'status':    self.status.status,
            'status_id': self.status_id,
            'email':     self.email,
            'phone':     self.phone,
            'addresses': [address.to_dict() for address in self.addresses]
        }

    def __repr__(self):
        return f'<CompanyAccount {self.name}>'

class AccountStatus(db.Model):
    # DB Table data will map to
    __tablename__ = 'account_status'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    status = db.Column(db.String(100), nullable=False)

class Addresses(db.Model):
    # DB Table data will map to
    __tablename__ = 'addresses'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    street = db.Column(db.String(100), nullable=False)
    city   = db.Column(db.String(100), nullable=False)
    state  = db.Column(db.String(100), nullable=False)
    zip    = db.Column(db.String(20),  nullable=False)
    
    # Foreign Keys
    company_id = db.Column(db.Integer, db.ForeignKey('company_accounts.id'), nullable=False)
    
    # Links to FK tables
    company = db.relationship('CompanyAccounts', backref='addresses')

    def to_dict(self):
        return {
            'id':         self.id,
            'company_id': self.company_id,
            'street':     self.street,
            'city':       self.city,
            'state':      self.state,
            'zip':        self.zip
        }


# <----------- Company Contact Models ------------>
class CompanyContacts(db.Model):
    # DB Tables data will map to
    __tablename__ = 'company_contacts'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    first_name = db.Column(db.String(75),   nullable=False)
    last_name  = db.Column(db.String(75),   nullable=False)
    email      = db.Column(db.String(200),  nullable=False)
    phone      = db.Column(db.String(20),   nullable=False)
    
    # Foreign Keys
    team_id     = db.Column(db.Integer, db.ForeignKey('Teams.id'),              nullable=False)
    company_id  = db.Column(db.Integer, db.ForeignKey('company_accounts.id'),   nullable=False)
    status_id   = db.Column(db.Integer, db.ForeignKey('account_status.id'),     nullable=False)
    job_role_id = db.Column(db.Integer, db.ForeignKey('job_roles.id'),          nullable=False)

    # Links to FK tables
    company  = db.relationship('CompanyAccounts',   backref='company_contacts')
    status   = db.relationship('AccountStatus',     backref='company_contacts')
    job_role = db.relationship('Job_Roles',         backref='company_contacts')
    teams    = db.relationship('Teams',             backref='company_contacts')

    def to_dict(self):
        return {
            'id':            self.id,
            'first_name':    self.first_name,
            'last_name':     self.last_name,
            'status':        self.status.status,
            'status_id':     self.status_id,
            'email':         self.email,
            'phone':         self.phone,
            'company_id':    self.company_id,
            'company':       self.company.name,
            'job_role_id':   self.job_role_id,
            'job_role_name': self.job_role.name,
            'team_id':       self.team_id,
            'team_name':     self.teams.name
        }

class Job_Roles(db.Model):
    # DB Table data will map to
    __tablename__ = 'job_roles'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id':   self.id,
            'name': self.name,
        }

class Teams(db.Model):
    # DB Table data will map to
    __tablename__ = 'Teams'
    
    # Primary Key
    id = db.Column(db.Integer,  primary_key=True)
    
    # Keys
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id':   self.id,
            'name': self.name,
        }


# <----------- Order Models ------------>

class OrderStatus(db.Model):
    # DB Table data will map to
    __tablename__ = 'order_status'
    
    # Primary Key
    id = db.Column(db.Integer,  primary_key=True)
    
    # Keys
    name  = db.Column(db.String(50),    nullable=False)
    tat   = db.Column(db.Integer,       nullable=False)
    price = db.Column(db.Float,         nullable=False)

class OrderPriority(db.Model):
    # Db Table data will map to
    __tablename__ = 'order_priority'
    
    # Primary Key
    id = db.Column(db.Integer,    primary_key=True)
    
    # Keys
    name = db.Column(db.String(50),  nullable=False)

class Orders(db.Model):
    # Db Table data will map to
    __tablename__ = 'orders'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
        
    # Keys
    submission_date = db.Column(db.DateTime, nullable=False)
    start_date      = db.Column(db.DateTime, nullable=True)
    end_date        = db.Column(db.DateTime, nullable=True)
    due_date        = db.Column(db.DateTime, nullable=True)

    # Foreign Keys
    status_id   = db.Column(db.Integer, db.ForeignKey('order_status.id'),       nullable=False)
    contact_id  = db.Column(db.Integer, db.ForeignKey('company_contacts.id'),   nullable=False)
    priority_id = db.Column(db.Integer, db.ForeignKey('order_priority.id'),     nullable=False)

    # Links to FK tables
    contact    = db.relationship('CompanyContacts', backref='orders')
    priority   = db.relationship('OrderPriority',   backref='orders')
    status     = db.relationship('OrderStatus',     backref='orders')

# <----------- Lamella Models ------------>

class Grids(db.Model):
    # DB Table
    __tablename__ = 'grids'
    
    # Primary Keys
    id    = db.Column(db.Integer, primary_key=True)
    
    # Keys
    name  = db.Column(db.String(50), nullable=False)

class Coating(db.Model):
    # DB Table
    __tablename__ = 'coating'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    name = db.Column(db.String(100), nullable=False)

class Wafers(db.Model):
    # DB Table
    __tablename__ = 'wafers'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # keys
    name = db.Column(db.String(50), nullable=False)
    
    # Foreign Keys
    contact_id = db.Column(db.Integer, db.ForeignKey('company_contacts.id'), nullable=False)

    # Relationships
    contact = db.relationship('CompanyContacts', backref='wafers')

    def to_dict(self):
        return {
            'id':            self.id,
            'name':          self.name,
            'contact_id':    self.contact_id,
            'contact_fname': self.contact.first_name,
            'contact_lname': self.contact.last_name
        }

class Chips(db.Model):
    # DB Table
    __tablename__ = 'chips'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    name = db.Column(db.String(50), nullable=False)
    
    # Foreign Keys
    wafer_id = db.Column(db.Integer, db.ForeignKey('wafers.id'), nullable=False)

    # Relationships
    wafer = db.relationship('Wafers', backref='chips')

    def to_dict(self):
        return {
            'id':       self.id,
            'name':     self.name,
            'wafer_id': self.wafer_id
        }

class Lamellas(db.Model):

    # Db Table data will map to
    __tablename__ = 'lamellas'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Keys
    name            = db.Column(db.String(50),  nullable=False)
    completion_date = db.Column(db.DateTime,    nullable=True)
    start_date      = db.Column(db.DateTime,    nullable=True)

    # Foreign Keys
    chip_id     = db.Column(db.Integer, db.ForeignKey('chips.id'),           nullable=False)
    coating_id  = db.Column(db.Integer, db.ForeignKey('coating.id'),         nullable=True)
    grid_id     = db.Column(db.Integer, db.ForeignKey('grids.id'),           nullable=True)
    status_id   = db.Column(db.Integer, db.ForeignKey('order_status.id'),    nullable=False)

    # Links to FK tables
    chip    = db.relationship('Chips',          backref='lamellas')
    status  = db.relationship('OrderStatus',    backref='lamellas')
    grid    = db.relationship('Grids',          backref='lamellas')
    coating = db.relationship('Coating',        backref='lamellas')

    def to_dict(self):

        return {
            'id':               self.id,
            'name':             self.name,
            'chip_id':          self.chip_id,
            'wafer_name':       self.chip.wafer.name,
            'coating_id':       self.coating_id,
            'coating_name':     self.coating.name if self.coating else None,
            'completion_date':  self.completion_date,
            'start_date':       self.start_date,
            'grid_id':          self.grid_id,
            'grid_name':        self.grid.name if self.grid else None,
            'status':           self.status.name

        }


# <----------- Order-Lamella Models ------------>

class OrderLamella(db.Model):

    # Db Table 
    __tablename__ = 'order_lamella'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys
    order_id    = db.Column(db.Integer, db.ForeignKey('orders.id'),     nullable=False)
    lamella_id  = db.Column(db.Integer, db.ForeignKey('lamellas.id'),   nullable=False)

    # Relationships
    orders   = db.relationship('Orders',    backref='order_lamella')
    lamellas = db.relationship('Lamellas',  backref='order_lamella')

class OLT(db.Model):

    # Db Table 
    __tablename__ = 'order_lamella_techniques'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Keys
    start_date  = db.Column(db.DateTime,    nullable=True)
    end_date    = db.Column(db.DateTime,    nullable=True)
    run_no      = db.Column(db.Integer,     nullable=True)

    # Foreign Keys
    ol_id        = db.Column(db.Integer, db.ForeignKey('order_lamella.id'),           nullable=False)
    technique_id = db.Column(db.Integer, db.ForeignKey('techniques.id'),         nullable=False)
    status_id    = db.Column(db.Integer, db.ForeignKey('order_status.id'),     nullable=False)

    # Relationships
    ol        = db.relationship('OrderLamella',  backref='order_lamella_techniques')
    technique = db.relationship('Techniques',  backref='order_lamella_techniques')
    status    = db.relationship('OrderStatus',   backref='order_lamella_techniques')

  # <----------- Technique Static Models ------------>

class Techniques(db.Model):

    # Db Table data will map to
    __tablename__ = 'techniques'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Keys
    name = db.Column(db.String(50), nullable=False)

class TechniqueSteps(db.Model):

    # Db Table data will map to
    __tablename__ = 'technique_steps'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Keys
    step_order        = db.Column(db.Integer,    nullable=False)
    step_name         = db.Column(db.String(50), nullable=False)
    expected_duration = db.Column(db.Integer,    nullable=False)
    
    # Foreign Keys
    technique_id = db.Column(db.Integer, db.ForeignKey('techniques.id'), nullable=False)

    # Relationships
    techniques = db.relationship('Techniques', backref='technique_steps')
