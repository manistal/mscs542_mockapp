-- Example data for Ski Resort App
-- Author: Miguel Nistal

-- Resorts
INSERT INTO resort (resort_id, resort_name) VALUES (1, 'FunMountain');
INSERT INTO resort (resort_id, resort_name) VALUES (2, 'CoolRanch');

-- Buildings, because resorts have places to stay
INSERT INTO building (building_id, building_name, building_address, resort_id) VALUES (1, 'FunLodge', '100 FunRoad, Fun, CO', 1);
INSERT INTO building (building_id, building_name, building_address, resort_id) VALUES (2, 'CoolLodge', '100 CoolRoad, Cool, CO', 2);

-- Guests, the Starks like snow
INSERT INTO guest (guest_id, guest_fname, guest_lname, guest_email) VALUES (1, 'John', 'Snow', 'snow@watch.com');
INSERT INTO guest (guest_id, guest_fname, guest_lname, guest_email) VALUES (2, 'Eddard', 'Stark', 'oldstark@stark.com');
INSERT INTO guest (guest_id, guest_fname, guest_lname, guest_email) VALUES (5, 'Queen', 'Elizabeth', 'queen@corgies.net');
INSERT INTO guest (guest_id, guest_fname, guest_lname, guest_email) VALUES (7, 'Catlyn', 'Stark', 'msstark@stark.com');
INSERT INTO guest (guest_id, guest_fname, guest_lname, guest_email) VALUES (8, 'Eddard', 'Stark', 'snow@watch.com');

-- Golf courses, politicians like golf courses
INSERT INTO golf_course (golf_course_id, golf_course_name, golf_course_holes, resort_id) VALUES (1, 'HRCLinks', 13, 1);
INSERT INTO golf_course (golf_course_id, golf_course_name, golf_course_holes, resort_id) VALUES (2, 'BernieLinks', 18, 1);
INSERT INTO golf_course (golf_course_id, golf_course_name, golf_course_holes, resort_id) VALUES (3, 'TrumpLinks', 13, 2);
INSERT INTO golf_course (golf_course_id, golf_course_name, golf_course_holes, resort_id) VALUES (4, 'McMuffinLinks', 18, 2);

-- Rooms, numerically generated 
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (1, 1, 1, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (2, 1, 2, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (3, 1, 3, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (4, 1, 4, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (5, 1, 5, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (6, 1, 6, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (7, 1, 7, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (8, 1, 8, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (9, 1, 9, 'Basic', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (10, 1, 20, 'Suite', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (11, 1, 21, 'Suite', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (12, 1, 22, 'Suite', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (13, 1, 23, 'Suite', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (14, 1, 24, 'Suite', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (15, 1, 30, 'Deluxe', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (16, 1, 70, 'Special', 1);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (17, 1, 1, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (18, 1, 2, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (19, 1, 3, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (20, 1, 4, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (21, 1, 5, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (22, 1, 6, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (23, 1, 7, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (24, 1, 8, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (25, 1, 9, 'Basic', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (26, 1, 20, 'Suite', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (27, 1, 21, 'Suite', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (28, 1, 22, 'Suite', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (29, 1, 23, 'Suite', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (30, 1, 24, 'Suite', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (31, 1, 30, 'Deluxe', 2);
INSERT INTO room (room_id, room_floor, room_number, room_type, building_id) VALUES (32, 1, 70, 'Special', 2);

-- Reservations
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (1, '2017-11-29', 8, 1, NULL, 17);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (3, '2017-11-21', 17, 2, NULL, 1);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (4, '2017-12-03', 6, 5, NULL, 16);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (5, '2017-11-01', 1, 2, NULL, 31);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (6, '2017-11-28', 4, 7, NULL, 18);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (7, '2017-11-29', 2, 8, NULL, 10);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (8, '2017-11-28', 23, 1, NULL, 15);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (9, '2017-12-12', 13, 1, NULL, 1);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (10, '2017-12-12', 13, 1, NULL, 2);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (11, '2017-12-12', 13, 1, NULL, 3);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (12, '2017-12-12', 13, 1, NULL, 4);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (13, '2017-12-12', 13, 1, NULL, 5);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (14, '2017-12-12', 13, 1, NULL, 6);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (15, '2017-12-08', 2, 1, NULL, 10);
INSERT INTO reservation (resv_id, resv_date, resv_days, guest_id, cc_id, room_id) VALUES (16, '2017-12-08', 2, 1, NULL, 11);

-- SkiPasses, Jon Snow and Kids
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (131, '2017-12-08', 'FullDay', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (132, '2017-12-08', 'FullDay', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (133, '2017-12-08', 'Child', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (134, '2017-12-08', 'Child', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (135, '2017-12-08', 'Child', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (136, '2017-12-09', 'FullDay', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (137, '2017-12-09', 'FullDay', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (138, '2017-12-09', 'Child', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (139, '2017-12-09', 'Child', 16, 1);
INSERT INTO ski_pass (skipass_id, skipass_day, skipass_type, resv_id, resort_id) VALUES (140, '2017-12-09', 'Child', 16, 1);

