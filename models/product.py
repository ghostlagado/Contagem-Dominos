from utils.db import db
from datetime import datetime, timezone

class Product(db.Model):
    id = db.Column(
        db.Integer, 
        primary_key=True, 
        nullable=False
    )
    name = db.Column(
        db.String(120),
        nullable=False
    )
    old_quantity = db.Column(
        db.Float,
        nullable=True
    )
    now_quantity = db.Column(
        db.Float,
        nullable=True
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=db.func.now(lambda: datetime.now(timezone.utc)),
        onupdate=db.func.now(lambda: datetime.now(timezone.utc)),
        nullable=False
    )
    on_system = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    @classmethod
    def get_all(cls):
        return cls.query.all()
