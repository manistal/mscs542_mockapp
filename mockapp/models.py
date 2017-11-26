from mockapp.extensions import db

from sqlalchemy import BigInteger, and_, func, Enum
from datetime import date, datetime


class Guest(db.Model):
    guest_id = db.Column(db.Integer, db.Sequence('guest_id'), primary_key=True)

    guest_fname = db.Column(db.String(100))
    guest_lname = db.Column(db.String(100))
    guest_email = db.Column(db.String(100))

    reservations = db.relationship('Reservation', backref='guest')
    credit_cards = db.relationship('CreditCard', backref='guest')


class CreditCard(db.Model):
    cc_id = db.Column(db.Integer, db.Sequence('cc_id'), primary_key=True)

    cc_number = db.Column(db.String(16))
    cc_provider = db.Column(Enum('Visa', 'MasterCard', 'AmericanExpress', name='accepted_cc_providers'), default='Visa')
    cc_address = db.Column(db.String)
    cc_expiration = db.Column(db.Date, default=date.today)

    guest_id = db.Column(db.Integer, db.ForeignKey('guest.guest_id'))
    
    reservations = db.relationship('Reservation', backref='credit_card')


class Reservation(db.Model):
    resv_id = db.Column(db.Integer, db.Sequence('resv_id'), primary_key=True)

    resv_date = db.Column(db.Date, default=date.today)
    resv_days = db.Column(db.Integer)

    guest_id = db.Column(db.Integer, db.ForeignKey('guest.guest_id'))
    cc_id = db.Column(db.Integer, db.ForeignKey('credit_card.cc_id'))

    rooms = db.relationship('Room', backref='reservation', nullable=False)
    ski_passes = db.relationship('SkiPass', backref='reservation')
    rentals = db.relationship('Rental', backref='reservation')
    golf_reservations = db.relationship('GolfReservation', backref='reservation')


class Building(db.Model):
    building_id = db.Column(db.Integer, db.Sequence('building_id'), primary_key=True)

    building_name = db.Column(db.String(100))
    building_address = db.Column(db.String)
    
    resort_id = db.Column(db.Integer, db.ForeignKey('resort.resort_id'))

    rooms = db.relationship('Room', backref='building', nullable=False)


class Room(db.Model):
    room_id = db.Column(db.Integer, db.Sequence('room_id'), primary_key=True)
    
    room_floor = db.Column(db.Integer)
    room_number = db.Column(db.Integer)
    room_type = db.Column(Enum('Basic', 'Suite', 'Deluxe', 'Special', name='available_room_types'), default='Basic')

    building_id = db.Column(db.Integer, db.ForeignKey('building.building_id'))
    resv_id = db.Column(db.Integer, db.ForeignKey('reservation.resv_id'))


class SkiPass(db.Model):
    skipass_id = db.Column(db.Integer, db.Sequence('skipass_id'), primary_key=True)

    skipass_day = db.Column(db.Date, default=date.today)
    skipass_type = db.Column(Enum('Child', 'HalfDay', 'FullDay', name='available_skipass_types'), default='FullDay')

    resv_id = db.Column(db.Integer, db.ForeignKey('reservation.resv_id'))
    resort_id = db.Column(db.Integer, db.ForeignKey('resort.resort_id'))


class Rental(db.Model):
    rental_id = db.Column(db.Integer, db.Sequence('rental_id'), primary_key=True)

    rental_type = db.Column(Enum('Skis', 'Snowboard', 'GolfClubs', name='available_rental_types'), default='Skis')
    rental_day = db.Column(db.Date, default=date.today)

    resv_id = db.Column(db.Integer, db.ForeignKey('reservation.resv_id'))
    resort_id = db.Column(db.Integer, db.ForeignKey('resort.resort_id'))


class GolfReservation(db.Model):
    golfresv_id = db.Column(db.Integer, db.Sequence('golfresv_id'), primary_key=True)

    golfresv_time = db.Column(db.Datetime, default=datetime.now)

    golf_course_id = db.Column(db.Integer, db.ForeignKey('golf_course.golf_course_id'))
    resv_id = db.Column(db.Integer, db.ForeignKey('reservation.resv_id'))


class GolfCourse(db.Model):
    golf_course_id = db.Column(db.Integer, db.Sequence('golf_course_id'), primary_key=True)

    golf_course_name = db.Column(db.String(100))
    golf_course_holes = db.Column(db.Integer)

    resort_id = db.Column(db.Integer, db.ForeignKey('resort.resort_id'))


class Resort(db.Model):
    resort_id = db.Column(db.Integer, db.Sequence('resort_id'), primary_key=True)

    resort_name = db.Column(db.String(100))

    buildings = db.relationship('Building', backref='resort')
    skipasses = db.relationship('SkiPass', backref='resort')
    rentals = db.relationship('Rental', backref='resort')
    golf_courses = db.relationship('GolfCourse', backref='resort')












