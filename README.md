# PohBingSen-GovTech
 Technical_Test
Task 2
1. An architecture diagram of the infrastructure/s required to host your API. (Usage of AWS services is preferred) 
a) User login / registration service
b) Payment Service for successful booking
c) User Database
d) Carpark/lot Database
*) To handle high traffic flow of request, the AWS service has API gateway and auto scaling group to handle the traffic efficiently.
*) If the user inputs a non-existing location, it will return an error message. To validate the user input against known carpark locations.
*) If the lot is taken up while the user is travelling to the location, it will send a message telling the user is occupied and give the user option of the nearby available carpark lot. It will always send live updates of the reserved carpark lot while the user has booked the carpark slot successfully.

2. A system design diagram that provides the logical flow of the carpark availability API. 
a) Upon registered successful / login successfully, user able to request the carpark availability with their current location
b) After the user books a desired carpark lot, it will send a status of “pending” and direct user to payment service
c) After payment completed, the system will send a status of “confirmed”
d) If the user doesn’t occupy the carpark lot within 15 minutes, the status will change to “cancelled”. The booking fee will be forfeited. 

3. A database schema that depicts the tables together with fields required as well as the data type of the fields. This is for both storing and accessing data required by the API/s.
a) Carpark Lot Details Table – store all carparks information in Singapore
Create Table CarparkDetails (
    Carpark_id INTEGER,
    Carpark_name VARCHAR(100),
    Location VARCHAR(100), 
    Total_lots INTEGER,
    Primary Key (Carpark_id)
);

b) Carpark Availability Table
Create Table CarparkAvailability (
    Lot_id INTEGER,
    Carpark_id INTEGER,
    Lots_available INTEGER, 
    Lot_type VARCHAR(5),
    Update_datetime CURRENT_TIMESTAMP,
    PRIMARY KEY (Lot_id),
    FOREIGN KEY (Carpark_id) REFERENCES CarparkDetails (Carpark_id)
);

c) User Table
Create Table User (
    User_id INTEGER,
    Password VAR(100),
    Name VARCHAR(100),
    Email VARCHAR(100),
    Contact_number VARCHAR(100),
    PRIMARY KEY (User_id)
);
d) Booking Table
Create Table Booking (
    Booking_id INTEGER,
    User_id INTEGER,
    Carpark_id INTEGER,
    Lot_id INTEGER,
    Status VARCHAR(100),
    PRIMARY KEY (Booking_id),
    FOREIGN KEY (User_id) REFERENCES User (User_id),
    FOREIGN KEY (Carpark_id) REFERENCES CarparkDetails (Carpark_id),
    FOREIGN KEY (Lot_id) REFERENCES CarparkAvailability (Lot_id)
    
4. An API document that provides the information of the API/s required.  
                   (Swagger documentation is a plus)

