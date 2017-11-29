# MSCS542 Final Project - Ski Resort Reservation System Mockup

Author: Miguel A Nistal 
Email: nistam328@gmail.com
Copyright (C) Miguel Nistal - All Rights Reserved
Unauthorized copying of this source code, via any medium is strictly prohibited

## Install postgres with homebrew

brew install postgresql 
brew services start postgresql 

## Configure

psql postgres

postgres=# CREATE ROLE mscs542 WITH LOGIN PASSWORD 'finalproject';
CREATE ROLE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 manistal  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 mscs542   |                                                            | {}

postgres=# ALTER ROLE mscs542 CREATEDB; 
ALTER ROLE

postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 manistal  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 mscs542   | Create DB                                                  | {}



postgres=# CREATE DATABASE mscs542_project;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE mscs542_project TO mscs542;
GRANT
postgres=# \list
                                     List of databases
      Name       |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------------+----------+----------+-------------+-------------+-----------------------
 mscs542_project | manistal | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/manistal         +
                 |          |          |             |             | manistal=CTc/manistal+
                 |          |          |             |             | mscs542=CTc/manistal
 postgres        | manistal | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0       | manistal | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/manistal          +
                 |          |          |             |             | manistal=CTc/manistal
 template1       | manistal | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/manistal          +
                 |          |          |             |             | manistal=CTc/manistal
(4 rows)


## Page Queries

###  /new_reservations

```
-- For the resort dropdown
SELECT resort.resort_id AS resort_resort_id, resort.resort_name AS resort_resort_name FROM resort
```

### /post_reservations

```
-- To see if the guest already exists in the system
SELECT guest.guest_id AS guest_guest_id, guest.guest_fname AS guest_guest_fname, guest.guest_lname AS guest_guest_lname, guest.guest_email AS guest_guest_email 
FROM guest 
WHERE guest.guest_fname = %(guest_fname_1)s AND guest.guest_lname = %(guest_lname_1)s AND guest.guest_email = %(guest_email_1)s

-- To see what resort they picked from dropdown
SELECT resort.resort_id AS resort_resort_id, resort.resort_name AS resort_resort_name 
FROM resort 
WHERE resort.resort_name = %(resort_name_1)s

-- To find an available room matching their criteria
SELECT room.room_id AS room_room_id, room.room_floor AS room_room_floor, room.room_number AS room_room_number, room.room_type AS room_room_type, room.building_id AS room_building_id 
FROM room JOIN building ON building.building_id = room.building_id 
WHERE NOT (EXISTS (SELECT 1 
FROM reservation 
WHERE room.room_id = reservation.room_id AND reservation.resv_date <= %(resv_date_1)s AND reservation.resv_days + reservation.resv_date >= %(param_1)s)) AND room.room_type = %(room_type_1)s AND %(param_2)s = building.resort_id
```

### /reservations

```
-- Populate the page
SELECT * FROM reservation 
JOIN room ON room.room_id = reservation.room_id 
JOIN building ON building.building_id = room.building_id 
JOIN resort ON resort.resort_id = building.resort_id
```


### /guests

```
-- Populate the page
SELECT * FROM GUEST
```

### /rooms

```
-- Get Available rooms (on a specific day)
SELECT room.room_id AS room_room_id, room.room_floor AS room_room_floor, room.room_number AS room_room_number, room.room_type AS room_room_type, room.building_id AS room_building_id 
FROM room 
WHERE NOT (EXISTS (SELECT 1 
FROM reservation 
WHERE room.room_id = reservation.room_id AND reservation.resv_date <= %(resv_date_1)s AND reservation.resv_days + reservation.resv_date >= %(param_1)s)) 

-- Get Used rooms (on a specific day)
SELECT room.room_id AS room_room_id, room.room_floor AS room_room_floor, room.room_number AS room_room_number, room.room_type AS room_room_type, room.building_id AS room_building_id 
FROM room 
WHERE EXISTS (SELECT 1 
FROM reservation 
WHERE room.room_id = reservation.room_id AND reservation.resv_date <= %(resv_date_1)s AND reservation.resv_days + reservation.resv_date >= %(param_1)s) 
```



