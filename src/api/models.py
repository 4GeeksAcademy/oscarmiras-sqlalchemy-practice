from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name =  db.Column(db.String(120),unique=True, nullable=False)
    homepage = db.Column(db.String(120))

    def __repr__(self):
        return f'<Supplier {self.company_name}'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name =  db.Column(db.String(120), nullable=False)
    list_price =  db.Column(db.Float, nullable=False)

    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=True)
    supplier = relationship('Supplier', backref='products')

    def __repr__(self):
        return f'<Product {self.product_name} - costs: {self.list_price}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }