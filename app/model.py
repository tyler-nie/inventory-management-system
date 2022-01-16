from app import db
class Item(db.model):
    """
    Create a Item
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(300))

    def __repr__(self):
        return f'<Item: {self.name}>'
