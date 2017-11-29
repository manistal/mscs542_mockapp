

from random import randint
import inflect
iengine = inflect.engine()

from mockapp.models import Guest, CreditCard, Reservation, Resort, Building, Room, GolfCourse, SkiPass, GolfReservation, Rental


def generate_data(db):
    # Fun Mountain
    resort = Resort(resort_name="FunMountain")
    db.session.add(resort)

    golf_course = GolfCourse(golf_course_name="HRCLinks", golf_course_holes=13, resort=resort)
    db.session.add(golf_course)

    golf_course = GolfCourse(golf_course_name="BernieLinks", golf_course_holes=18, resort=resort)
    db.session.add(golf_course)

    building = Building(building_name="FunLodge", building_address="100 FunRoad, Fun, CO", resort=resort)
    db.session.add(building)

    for floor in range(1,2):
        for roomnum in range(1,10):
            room = Room(room_floor=floor, room_number=roomnum, room_type='Basic', building=building)
            db.session.add(room)

        for roomnum in range(20,25):
            room = Room(room_floor=floor, room_number=roomnum, room_type='Suite', building=building)
            db.session.add(room)

        for roomnum in range(30,31):
            room = Room(room_floor=floor, room_number=roomnum, room_type='Deluxe', building=building)
            db.session.add(room)

        room = Room(room_floor=floor, room_number=70, room_type='Special', building=building)
        db.session.add(room)


    # Cool Ranch
    resort = Resort(resort_name="CoolRanch")
    db.session.add(resort)

    golf_course = GolfCourse(golf_course_name="TrumpLinks", golf_course_holes=13, resort=resort)
    db.session.add(golf_course)

    golf_course = GolfCourse(golf_course_name="McMuffinLinks", golf_course_holes=18, resort=resort)
    db.session.add(golf_course)

    building = Building(building_name="CoolLodge", building_address="100 CoolRoad, Cool, CO", resort=resort)
    db.session.add(building)

    for floor in range(1,2):
        for roomnum in range(1,10):
            room = Room(room_floor=floor, room_number=roomnum, room_type='Basic', building=building)
            db.session.add(room)

        for roomnum in range(20,25):
            room = Room(room_floor=floor, room_number=roomnum, room_type='Suite', building=building)
            db.session.add(room)

        for roomnum in range(30,31):
            room = Room(room_floor=floor, room_number=roomnum, room_type='Deluxe', building=building)
            db.session.add(room)

        room = Room(room_floor=floor, room_number=70, room_type='Special', building=building)
        db.session.add(room)

    db.session.commit()

