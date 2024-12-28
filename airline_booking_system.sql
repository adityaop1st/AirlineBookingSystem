CREATE DATABASE flight_booking_system;
use  flight_booking_system;

CREATE TABLE account (
    user_name varchar(10),
    password varchar(20) NOT NULL,
    PRIMARY KEY (user_name)
);

INSERT INTO account value ('aditya', 'test');


create table seat(
	seat_id char(5) primary key,
    seat_number char(10),
    class varchar(10)

    );


create table airline(
	airline_id char(5) primary key,
    name char(10),
    country varchar(10)
    );

insert INTO AIRLINE VALUE ('00001', 'AkashAir', 'IN');
insert INTO AIRLINE VALUE ('00003', 'SpiceJat', 'IN');

drop table flight;
create table flight(
	Flight_id char(15) primary key,
    Flight_number char(15),
    Departure varchar(10),
    Arival varchar(10),
    Departure_time datetime,
    Arival_time datetime,
    airline_id char(5),
	FOREIGN KEY (airline_id) REFERENCES airline(airline_id)
    );

insert into flight
value ('SG-2962', 'SG-2962', 'PNQ', 'ADI', '2024-12-26 06:00:00','2024-12-26 08:00:00', '00003');

insert into flight
value ('SG-2961', 'SG-2961', 'PNQ', 'ADI', '2024-12-26 11:00:00','2024-12-26 15:00:00', '00003');

insert into flight
value ('QP-1509', 'QP-1509', 'PNQ', 'ADI', '2024-12-26 08:00:00','2024-12-26 10:00:00', '00001');

insert into flight
value ('QP-1508', 'QP-1508', 'PNQ', 'ADI', '2024-12-26 15:00:00','2024-12-26 17:00:00', '00001');

select * from flight;

drop table seat;
create table seat(
seat_id char(15) primary key,
seat_number char(10),
class varchar(10),
Flight_id char(15),
FOREIGN KEY (Flight_id) REFERENCES flight(Flight_id)
);

insert into seat value('SG-A-001','A-001', 'ECONOMY', 'SG-2962');
insert into seat value('SG-A-002','A-001', 'ECONOMY', 'SG-2962');
insert into seat value('SG-B-003','B-003', 'Business', 'SG-2962');
insert into seat value('SG-B-004','B-004', 'Business', 'SG-2962');
insert into seat value('SG-A-005','A-001', 'ECONOMY', 'SG-2962');
insert into seat value('SG-A-006','A-001', 'ECONOMY', 'SG-2962');



insert into seat value('SG-62-A-001','A-001', 'ECONOMY', 'SG-2961');
insert into seat value('SG-62-A-002','A-001', 'ECONOMY', 'SG-2961');
insert into seat value('SG-62-B-003','B-003', 'Business', 'SG-2961');
insert into seat value('SG-62-B-004','B-004', 'Business', 'SG-2961');
insert into seat value('SG-62-A-005','A-001', 'ECONOMY', 'SG-2961');
insert into seat value('SG-62-A-006','A-001', 'ECONOMY', 'SG-2961');

insert into seat value('QP-1509-A-001','A-001', 'ECONOMY', 'QP-1509');
insert into seat value('QP-1509-A-002','A-001', 'ECONOMY', 'QP-1509');
insert into seat value('QP-1509-B-003','B-003', 'Business', 'QP-1509');
insert into seat value('QP-1509-B-004','B-004', 'Business', 'QP-1509');
insert into seat value('QP-1509-A-005','A-001', 'ECONOMY', 'QP-1509');
insert into seat value('QP-1509-A-006','A-001', 'ECONOMY', 'QP-1509');

insert into seat value('QP-1508-A-001','A-001', 'ECONOMY', 'QP-1508');
insert into seat value('QP-1508-A-002','A-001', 'ECONOMY', 'QP-1508');
insert into seat value('QP-1508-B-003','B-003', 'Business', 'QP-1508');
insert into seat value('QP-1508-B-004','B-004', 'Business', 'QP-1508');
insert into seat value('QP-1508-A-005','A-001', 'ECONOMY', 'QP-1508');
insert into seat value('QP-1508-A-006','A-001', 'ECONOMY', 'QP-1508');