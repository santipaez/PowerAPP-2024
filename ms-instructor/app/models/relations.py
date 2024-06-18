from app import db

instructor_roles = db.Table(
    "instructor_roles",
    db.Column("instructor_id", db.Integer, db.ForeignKey("instructors.id"), primary_key=True),
    db.Column("roles_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)
