from app import db

user_roles = db.Table(
    "user_roles",
    db.Column("users_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("roles_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)