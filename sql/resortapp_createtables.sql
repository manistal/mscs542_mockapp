-- Author: Miguel Nistal
-- MSCS542 Final Project


-- Enum Creation (Need types available before tables) 
-- ==================================================
CREATE TYPE accepted_cc_providers AS ENUM (
    'Visa',
    'MasterCard',
    'AmericanExpress'
);

CREATE TYPE available_rental_types AS ENUM (
    'Skis',
    'Snowboard',
    'GolfClubs'
);

CREATE TYPE available_room_types AS ENUM (
    'Basic',
    'Suite',
    'Deluxe',
    'Special'
);

CREATE TYPE available_skipass_types AS ENUM (
    'Child',
    'HalfDay',
    'FullDay'
);

-- Table Creation 
-- =================
CREATE TABLE building (
    building_id integer NOT NULL,
    building_name character varying(100) NOT NULL,
    building_address character varying NOT NULL,
    resort_id integer
);

CREATE TABLE credit_card (
    cc_id integer NOT NULL,
    cc_number character varying(16) NOT NULL,
    cc_provider accepted_cc_providers,
    cc_address character varying NOT NULL,
    cc_expiration date,
    guest_id integer
);

CREATE TABLE golf_course (
    golf_course_id integer NOT NULL,
    golf_course_name character varying(100),
    golf_course_holes integer,
    resort_id integer
);

CREATE TABLE golf_reservation (
    golfresv_id integer NOT NULL,
    golfresv_time timestamp without time zone,
    golf_course_id integer,
    resv_id integer
);

CREATE TABLE guest (
    guest_id integer NOT NULL,
    guest_fname character varying(100) NOT NULL,
    guest_lname character varying(100) NOT NULL,
    guest_email character varying(100)
);

CREATE TABLE rental (
    rental_id integer NOT NULL,
    rental_type available_rental_types,
    rental_day date,
    resv_id integer,
    resort_id integer
);

CREATE TABLE reservation (
    resv_id integer NOT NULL,
    resv_date date,
    resv_days integer,
    guest_id integer,
    cc_id integer,
    room_id integer
);

CREATE TABLE resort (
    resort_id integer NOT NULL,
    resort_name character varying(100) NOT NULL
);

CREATE TABLE room (
    room_id integer NOT NULL,
    room_floor integer NOT NULL,
    room_number integer NOT NULL,
    room_type available_room_types,
    building_id integer
);

CREATE TABLE ski_pass (
    skipass_id integer NOT NULL,
    skipass_day date,
    skipass_type available_skipass_types,
    resv_id integer,
    resort_id integer
);

-- Sequence Creation (need unique PKs) 
-- ===================================
CREATE SEQUENCE building_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE cc_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE golf_course_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE golfresv_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE guest_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


CREATE SEQUENCE rental_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE resort_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE resv_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE room_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE skipass_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


-- Set the primary keys to the sequences 
-- =======================================
ALTER TABLE ONLY building
    ADD CONSTRAINT building_pkey PRIMARY KEY (building_id);

ALTER TABLE ONLY credit_card
    ADD CONSTRAINT credit_card_pkey PRIMARY KEY (cc_id);

ALTER TABLE ONLY golf_course
    ADD CONSTRAINT golf_course_pkey PRIMARY KEY (golf_course_id);

ALTER TABLE ONLY golf_reservation
    ADD CONSTRAINT golf_reservation_pkey PRIMARY KEY (golfresv_id);

ALTER TABLE ONLY guest
    ADD CONSTRAINT guest_pkey PRIMARY KEY (guest_id);

ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_pkey PRIMARY KEY (rental_id);

ALTER TABLE ONLY reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (resv_id);

ALTER TABLE ONLY resort
    ADD CONSTRAINT resort_pkey PRIMARY KEY (resort_id);

ALTER TABLE ONLY room
    ADD CONSTRAINT room_pkey PRIMARY KEY (room_id);

ALTER TABLE ONLY ski_pass
    ADD CONSTRAINT ski_pass_pkey PRIMARY KEY (skipass_id);


-- Set the foreign keys for the relationships
-- ===========================================
ALTER TABLE ONLY building
    ADD CONSTRAINT building_resort_id_fkey FOREIGN KEY (resort_id) REFERENCES resort(resort_id);

ALTER TABLE ONLY credit_card
    ADD CONSTRAINT credit_card_guest_id_fkey FOREIGN KEY (guest_id) REFERENCES guest(guest_id);

ALTER TABLE ONLY golf_course
    ADD CONSTRAINT golf_course_resort_id_fkey FOREIGN KEY (resort_id) REFERENCES resort(resort_id);

ALTER TABLE ONLY golf_reservation
    ADD CONSTRAINT golf_reservation_golf_course_id_fkey FOREIGN KEY (golf_course_id) REFERENCES golf_course(golf_course_id);

ALTER TABLE ONLY golf_reservation
    ADD CONSTRAINT golf_reservation_resv_id_fkey FOREIGN KEY (resv_id) REFERENCES reservation(resv_id);

ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_resort_id_fkey FOREIGN KEY (resort_id) REFERENCES resort(resort_id);

ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_resv_id_fkey FOREIGN KEY (resv_id) REFERENCES reservation(resv_id);

ALTER TABLE ONLY reservation
    ADD CONSTRAINT reservation_cc_id_fkey FOREIGN KEY (cc_id) REFERENCES credit_card(cc_id);

ALTER TABLE ONLY reservation
    ADD CONSTRAINT reservation_guest_id_fkey FOREIGN KEY (guest_id) REFERENCES guest(guest_id);

ALTER TABLE ONLY reservation
    ADD CONSTRAINT reservation_room_id_fkey FOREIGN KEY (room_id) REFERENCES room(room_id);

ALTER TABLE ONLY room
    ADD CONSTRAINT room_building_id_fkey FOREIGN KEY (building_id) REFERENCES building(building_id);

ALTER TABLE ONLY ski_pass
    ADD CONSTRAINT ski_pass_resort_id_fkey FOREIGN KEY (resort_id) REFERENCES resort(resort_id);

ALTER TABLE ONLY ski_pass
    ADD CONSTRAINT ski_pass_resv_id_fkey FOREIGN KEY (resv_id) REFERENCES reservation(resv_id);


