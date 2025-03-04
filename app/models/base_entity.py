from app import db
from uuid import uuid4

class BaseEntity(db.Model):
  __abstract__ = True

  id = db.Column(db.String(36), primary_key=True, default=uuid4())
  created_at = db.Column(db.DateTime, default=db.func.now())
  updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())