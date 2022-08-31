create table user(
	id bigint SEQUENCE,
	name varchar(255),
	email varchar(255),
	phone_number varchar(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
create table company(
	id bigint SEQUENCE,
	name varchar(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP	
);
create table cmp_domain(
	id bigint SEQUENCE,
	domain_name text,
	domain_extension varchar(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table scrap_type(
	id int SEQUENCE,
	name varchar(40),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
create table scrap_data(
	id bigint SEQUENCE,
	cmp_domain_id BIGINT,
	currency varchar(20),
	full_url text,
	url text ,
	active bool,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	CONSTRAINTS scrap_data_cmp_domain_id FOREIGN KEY(cmp_domain_id) REFERENCES cmp_domain(id)
);
create table scrap_price(
	id bigint SEQUENCE,
	scrap_data_id BIGINT,
	price int,
	scraped_time timestamptz,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	CONSTRAINTS scrap_price_scrap_data_id FOREIGN KEY(scrap_data_id) REFERENCES scrap_data(id)
);

create table price_alert(
	id bigint SEQUENCE,
	user_id bigint,
	scrap_data BIGINT,
	current_price int,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
create table notification(
	id bigint SEQUENCE,
	user_id bigint,
	price_alert_id BIGINT,
	notification_type int,
	status bool,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table device_type(
	id int SEQUENCE,
	name text,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



