

from random import randint
import inflect
iengine = inflect.engine()

from mockapp.models import Guest, CreditCard, Reservation, Resort, Building, Room, GolfCourse, SkiPass, GolfReservation, Rental

def gen_Guest():
    lname = iengine.number_to_words(randint(0, 999))
    lname = lname.replace(' ', '-')
    email = lname + '@gmail.com'
    fake_guest = Guest(
        guest_fname='guest',
        guest_lname=lname,
        guest_email=email
    )
    return fake_guest


def generate_data():
    for i in range(0,10):
        g = gen_Guest()
        print(g.guest_fname, g.guest_lname, g.guest_email, len(g.guest_email))


if __name__ == "__main__":
    generate_data()
