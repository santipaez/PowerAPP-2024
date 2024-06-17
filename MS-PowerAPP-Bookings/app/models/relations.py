from app import db

booking_roles = db.Table(
    "booking_roles",
    db.Column("booking_id", db.Integer, db.ForeignKey("bookings.id"), primary_key=True),
    db.Column("booking_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)
