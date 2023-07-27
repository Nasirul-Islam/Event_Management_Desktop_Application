USE event_management_app;


CREATE TABLE all_events(
    e_type VARCHAR(50),
    e_name VARCHAR(50),
    e_amount INT,
    e_seats INT,
    e_menu VARCHAR(100),
    e_date DATE,
    e_time TIME,
    u_name VARCHAR(50),
    u_email VARCHAR(50),
    u_phone INT,
    u_address VARCHAR(100),
    u_PaymentMathod VARCHAR(50),
    u_TransactionID VARCHAR(50)
);

select * from all_events;
