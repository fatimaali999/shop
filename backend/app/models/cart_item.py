from app import db

class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref='cart_items')

    def __repr__(self):
        return f"<CartItem {self.id}>"
