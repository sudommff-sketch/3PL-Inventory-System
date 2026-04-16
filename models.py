from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    client_name = Column(String, nullable=False)
    client_address = Column(String)
    contact_info = Column(String)
    
    orders = relationship("Order", back_populates="client")

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    description = Column(String)
    sku = Column(String, unique=True)
    
    stock_entries = relationship("Stock", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")
    shipment_items = relationship("ShipmentItem", back_populates="product")

class Stock(Base):
    __tablename__ = 'stocks'
    stock_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, default=0)
    location = Column(String)
    
    product = relationship("Product", back_populates="stock_entries")

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    order_status = Column(String, default="Pending")
    
    client = relationship("Client", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    shipment = relationship("Shipment", back_populates="order", uselist=False)

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")

class Shipment(Base):
    __tablename__ = 'shipments'
    shipment_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    shipment_status = Column(String, default="Processing")
    
    order = relationship("Order", back_populates="shipment")
    items = relationship("ShipmentItem", back_populates="shipment")

class ShipmentItem(Base):
    __tablename__ = 'shipment_items'
    shipment_item_id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.shipment_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    
    shipment = relationship("Shipment", back_populates="items")
    product = relationship("Product", back_populates="shipment_items")

