
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for
from sqlalchemy import not_, or_, and_
from datetime import datetime, timedelta, date
import json
import os

from mockapp.models import Guest, Reservation, Room, Resort, Building

bp = Blueprint('dashboard', __name__, template_folder='templates')

@bp.route('/')
@bp.route('/new_reservation', methods=['GET'])
def new_reservation():
    return render_template(
        'new_reservation.html', 
        resorts=Resort.query.all()
    )

@bp.route('/new_reservation', methods=['POST'])
def post_reservation():
    print(request.form)

    # Add or get Guest ID 
    guest = Guest.query.filter(
        Guest.guest_fname == request.form.get('guest-fname'),
        Guest.guest_lname == request.form.get('guest-lname'),
        Guest.guest_email == request.form.get('guest-email'),
    )
    if guest is None:
        guest = Guest(
            guest_fname = request.form.get('guest-fname'),
            guest_lname = request.form.get('guest-lname'),
            guest_email = request.form.get('guest-email'),
        )

    room_type = request.form.get('room-type')
    room_type = room_type if room_type != 'Room Type' else 'Basic'
    from_date = datetime.strptime(request.form.get('from-date'), '%m/%d/%Y').date()
    to_date = datetime.strptime(request.form.get('to-date'), '%m/%d/%Y').date()
    find_available_room = Room.query.join(Reservation).filter(
        Room.room_type == room_type,
        or_(
            and_(
                Reservation.resv_date < from_date,
                Reservation.resv_date > to_date,
            ),
            not_(Room.reservations.any())
        )
    )

    return render_template(
        'new_reservation.html'
    )

@bp.route('/rooms')
def rooms():
    #available_rooms = Room.query.join(Reservation, Building).filter(
    #    or_(
    #        and_(
    #            Reservation.resv_date < date.today(),
    #            Reservation.resv_date > date.today(),
    #        ),
    #        not_(Room.reservations.any())
    #    )
    #).all()
    available_rooms = Room.query.filter(
        ~Room.reservations.any(),
    ).all()

    unavailable_rooms = Room.query.join(Reservation).filter(
        Reservation.resv_date > date.today(),
        Reservation.resv_date < date.today(),
    ).all()

    all_rooms = Room.query.join(Building).all()

    return render_template(
        'rooms.html',
        all_rooms=all_rooms, 
        available_rooms=available_rooms,
        unavailable_rooms=unavailable_rooms
    )    

@bp.route('/reservations')
def reservations():
    return render_template(
        'reservations.html',
        reservations=Reservation.query.all()
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

    skipass_data = [
        ('Guest1', 'John', 'Doe', 'Addr'),
        ('Guest2', 'Jane', 'Doe', 'Addr')
    ]
    return render_template(
        'skipasses.html',
        skipass_data=skipass_data
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

