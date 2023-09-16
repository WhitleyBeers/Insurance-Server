CREATE TABLE `Location` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL
);

CREATE TABLE `Customer` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);


CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)

);

INSERT INTO `Location` VALUES (null, 'Nashville North', "64 Washington Heights");
INSERT INTO `Location` VALUES (null, 'Nashville South', "101 Penn Ave");


INSERT INTO `Employee` VALUES (null, "Madi Peper", "35498 Madison Ave", 1);
INSERT INTO `Employee` VALUES (null, "Kristen Norris", "100 Main St", 1);
INSERT INTO `Employee` VALUES (null, "Meg Ducharme", "404 Unknown Ct", 2);
INSERT INTO `Employee` VALUES (null, "Hannah Hall", "204 Empty Ave", 1);
INSERT INTO `Employee` VALUES (null, "Leah Hoefling", "200 Success Way", 2);


INSERT INTO `Customer` VALUES (null, "Mo Silvera", "201 Created St", "mo@silvera.com", "password");
INSERT INTO `Customer` VALUES (null, "Bryan Nilsen", "500 Internal Error Blvd", "bryan@nilsen.com", "password");
INSERT INTO `Customer` VALUES (null, "Jenna Solis", "301 Redirect Ave", "jenna@solis.com", "password");
INSERT INTO `Customer` VALUES (null, "Emily Lemmon", "454 Mulberry Way", "emily@lemmon.com", "password");



INSERT INTO `Animal` VALUES (null, "Snickers", "Recreation", "Dalmation", 4, 1);
INSERT INTO `Animal` VALUES (null, "Jax", "Treatment", "Beagle", 1, 1);
INSERT INTO `Animal` VALUES (null, "Falafel", "Treatment", "Siamese", 4, 2);
INSERT INTO `Animal` VALUES (null, "Doodles", "Kennel", "Poodle", 3, 1);
INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);
INSERT INTO `Animal` VALUES (null, "Cleo", "Kennel", "Poodle", 2, 2);
INSERT INTO `Animal` VALUES (null, "Popcorn", "Kennel", "Beagle", 3, 2);
INSERT INTO `Animal` VALUES (null, "Curly", "Treatment", "Poodle", 4, 2);
INSERT INTO `Animal` VALUES (null, "dede", "unknown", "whoknows", 4, 2);

SELECT
    a.id,
    a.name,
    a.breed,
    a.status,
    a.location_id,
    a.customer_id,
    l.name location_name,
    l.address location_address,
		c.name customer_name,
		c.address customer_address,
		c.email customer_email
FROM Animal a
JOIN Location l
    ON l.id = a.location_id
JOIN Customer c
    ON c.id = a.customer_id

SELECT
   a.id,
   a.name,
   a.address,
   a.location_id,
   l.name location_name,
   l.address location_address
FROM employee a
JOIN Location l
    ON l.id = a.location_id

				  