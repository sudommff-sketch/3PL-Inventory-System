from sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

"""Stock table in database holds 3 rows"""
class Stock(Base):
    __tablename__ = 'stock'
    stock_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)

"""Product table in database holds 4 rows"""
class Product(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    description = Column(String)
    client_id = Column(Integer, ForeignKey('client.client_id'))

#Relationships
    stock = relationship("Stock", backref="product")    #Relationships make it easier to call other tables"""
    orders = relationship("Order", backref="product")
    order_items = relationship("OrderItem", backref="product")
    shipment_items = relationship("ShipmentItem", backref="product")

"""Client table in database holds 4 rows"""
class Client(Base):
    __tablename__ = 'client'
    client_id = Column(Integer, primary_key=True)
    client_name = Column(String)
    client_address = Column(String)
    contact_info = Column(String)

#Relationships
    products = relationship("Product", backref="client")

"""Shipment table in database holds 3 rows"""
class Shipment(Base):
    __tablename__ = 'shipment'
    shipment_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.order_id'))
    shipment_status = Column(String)

#Relationships
    items = relationship("ShipmentItem", backref="shipment")

"""Order table in database holds 3 rows"""
class Order(Base):
    __tablename__ = 'order'
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    order_status = Column(String)

#Relationships
    items = relationship("OrderItem", backref="order")
    shipment = relationship("Shipment", backref="order", uselist=False)

"""OrderItem table in database holds 4 rows"""
class OrderItem(Base):
    __tablename__ = 'order_item'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.order_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)

"""Shipment table in database holds 3 rows"""
class ShipmentItem(Base):
    __tablename__ = 'shipment_item'
    shipment_item_id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipment.shipment_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)

Base.metadata.create_all(engine)