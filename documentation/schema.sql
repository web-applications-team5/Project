CREATE TABLE address (
	id INTEGER NOT NULL, 
	"addressLine" VARCHAR(255) NOT NULL, 
	city VARCHAR(255) NOT NULL, 
	state VARCHAR(45) NOT NULL, 
	zipcode VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id)
);

CREATE TABLE user (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	phone VARCHAR(12), 
	email VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (id)
);

CREATE TABLE restaurant (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	"openTime" TIME NOT NULL, 
	"closeTime" TIME NOT NULL, 
	logo VARCHAR(255), 
	description VARCHAR(5000), 
	rating INTEGER, 
	address_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	UNIQUE (name), 
	FOREIGN KEY(address_id) REFERENCES address (id)
);

CREATE TABLE "order" (
	id INTEGER NOT NULL, 
	status VARCHAR(10), 
	"confirmationNumber" VARCHAR(100), 
	"createdDate" VARCHAR(45), 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);

CREATE TABLE menu (
	id INTEGER NOT NULL, 
	restaurant_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY(restaurant_id) REFERENCES restaurant (id)
);

CREATE TABLE photo (
	id INTEGER NOT NULL, 
	url VARCHAR(1024) NOT NULL, 
	restaurant_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY(restaurant_id) REFERENCES restaurant (id)
);

CREATE TABLE "menuItem" (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	price FLOAT NOT NULL, 
	description VARCHAR(5000), 
	photo VARCHAR(1024), 
	status VARCHAR(45) NOT NULL, 
	menu_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY(menu_id) REFERENCES menu (id)
);

CREATE TABLE "orderItem" (
	id INTEGER NOT NULL, 
	order_id INTEGER NOT NULL, 
	"menuItem_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY(order_id) REFERENCES "order" (id), 
	FOREIGN KEY("menuItem_id") REFERENCES "menuItem" (id)
);
