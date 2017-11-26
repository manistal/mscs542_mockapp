
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for
from datetime import datetime, timedelta
import json
import os

bp = Blueprint('dashboard', __name__, template_folder='templates')

@bp.route('/')
@bp.route('/reservations')
def reservations():

    resv_data = [
        ('Guest1', 'June 27 2017', '3 days'),
        ('Guest2', 'June 27 2017', '3 days')
    ]
    return render_template(
        'reservations.html',
        resv_data=resv_data
    )    

@bp.route('/guests')
def guests():

    guest_data = [
        ('guest1', 'john', 'doe', 'addr'),
        ('guest2', 'jane', 'doe', 'addr')
    ]
    return render_template(
        'guests.html',
        guest_data=guest_data
    )    

@bp.route('/rooms')
def rooms():

    room_data = [
        ('room1', 'john', 'doe', 'addr'),
        ('room2', 'jane', 'doe', 'addr')
    ]
    return render_template(
        'rooms.html',
        room_data=room_data
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

