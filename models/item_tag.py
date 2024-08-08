from db import db

class ItemTag(db.Model):
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_key= True)
    items_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tags_id = db.Column(db.Integer, db.ForeignKey("tags.id"))