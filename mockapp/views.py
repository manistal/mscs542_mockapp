
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for
from sqlalchemy import not_, or_, and_
from datetime import datetime, timedelta, date
import json
import os

from mockapp.models import Guest, Reservation, Room, Resort, Building, SkiPass
from mockapp.extensions import db

bp = Blueprint('dashboard', __name__, template_folder='templates')

@bp.route('/')
@bp.route('/new_reservation', methods=['GET'])
def new_reservation():
    resort_query = Resort.query
    print("RESORT QUERRY\n", resort_query)
    return render_template(
        'new_reservation.html', 
        resorts=resort_query.all()
    )

@bp.route('/new_reservation', methods=['POST'])
def post_reservation():
    # Add or get Guest ID 
    guest = Guest.query.filter(
        Guest.guest_fname == request.form.get('guest-fname'),
        Guest.guest_lname == request.form.get('guest-lname'),
        Guest.guest_email == request.form.get('guest-email'),
    )
    print("GUEST QUERY\n", guest)
    guest = guest.first()
    if guest is None:
        guest = Guest(
            guest_fname = request.form.get('guest-fname'),
            guest_lname = request.form.get('guest-lname'),
            guest_email = request.form.get('guest-email'),
        )
        db.session.add(guest)
    
    # Get Resort ID 
    resort = Resort.query.filter(
        Resort.resort_name == request.form.get('resort-name')
    )
    print("RESORT QUERY\n", resort)
    resort = resort.first()

    # Parse room type 
    room_type = request.form.get('room-type')
    room_type = room_type if room_type != 'Room Type' else 'Basic'

    # Parse date info 
    from_date = datetime.strptime(request.form.get('from-date'), '%m/%d/%Y').date()
    to_date = datetime.strptime(request.form.get('to-date'), '%m/%d/%Y').date()
    resv_days = (to_date - from_date).days

    # Find a room
    new_room = Room.query.join(Building).filter(
        ~Room.reservations.any(and_(
            Reservation.resv_date <= to_date,
            Reservation.resv_days + Reservation.resv_date >= from_date
        )),
        Room.room_type == room_type, 
        Building.resort == resort
    )
    print("NEW ROOM QUERY (SO COOL): \n",new_room)
    new_room = new_room.first()

    print(guest, room_type, from_date, resv_days, resort, new_room)

    # Create Reservation
    if guest and new_room and from_date and resv_days:
        new_reservation = Reservation(
            resv_date = from_date,
            resv_days = resv_days,
            guest = guest,
            room = new_room,
        )
        print(new_reservation)

        db.session.add(new_reservation)
        db.session.commit()
    else:
        print(guest, new_room)
        return redirect(url_for('dashboard.new_reservation'))

    # Get them some passes!
    adultskipasses = int(request.form.get('skipasses-adult', 0) or 0)
    halfskipasses = int(request.form.get('skipasses-half', 0) or 0)
    childskipasses = int(request.form.get('skipasses-child', 0) or 0)

    for day_index in range(0,resv_days):
        for adults in range(0, adultskipasses):
            new_pass = SkiPass(
                resort = resort,
                reservation = new_reservation,
                skipass_type = 'FullDay',
                skipass_day = from_date + timedelta(days=day_index)
            )
            db.session.add(new_pass)
            
        for halfs in range(0, halfskipasses):
            new_pass = SkiPass(
                resort = resort,
                reservation = new_reservation,
                skipass_type = 'HalfDay',
                skipass_day = from_date + timedelta(days=day_index)
            )
            db.session.add(new_pass)

        for child in range(0, childskipasses):
            new_pass = SkiPass(
                resort = resort,
                reservation = new_reservation,
                skipass_type = 'Child',
                skipass_day = from_date + timedelta(days=day_index)
            )
            db.session.add(new_pass)
    db.session.commit()
    return redirect(url_for('dashboard.new_reservation'))

@bp.route('/rooms')
def rooms():
    available_rooms = Room.query.filter(
        ~Room.reservations.any(and_(
            Reservation.resv_date <= date.today(),
            Reservation.resv_days + Reservation.resv_date >= date.today()
        )),
    )

    unavailable_rooms = Room.query.filter(
        Room.reservations.any(and_(
            Reservation.resv_date <= date.today(),
            Reservation.resv_days + Reservation.resv_date >= date.today()
        )),
    )

    print("\nAVAILABLEROOMS\n", available_rooms, "\n\n")
    print("\nUNAVAILABLEROOMS\n", unavailable_rooms, "\n\n")

    return render_template(
        'rooms.html',
        available_rooms=available_rooms.all(),
        unavailable_rooms=unavailable_rooms.all()
    )    

@bp.route('/reservations')
def reservations():
    reservation_query = Reservation.query.join(Room, Building, Resort)
    print(reservation_query)
    return render_template(
        'reservations.html',
        reservations=reservation_query.all()
    )    

@bp.route('/guests')
def guests():
    return render_template(
        'guests.html',
        guests=Guest.query.all()
    )    


@bp.route('/rentals')
def rentals():

    rental_data = [
        ('Guest1', 'John', 'Doe', 'Addr'),
        ('Guest2', 'Jane', 'Doe', 'Addr')
    ]
    return render_template(
        'rentals.html',
        rental_data=rental_data
    )    

@bp.route('/skipasses')
def skipasses():
    print(SkiPass.query.all())
    return render_template(
        'skipasses.html',
        skipasses=SkiPass.query.all()
    )    

@bp.route('/teetimes')
def teetimes():

    teetime_data = [
        ('Guest1', 'John', 'Doe', 'Addr'),
        ('Guest2', 'Jane', 'Doe', 'Addr')
    ]
    return render_template(
        'teetimes.html',
        teetime_data=teetime_data
    )    

