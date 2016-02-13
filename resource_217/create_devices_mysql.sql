DROP TABLE if exists `devices`;
CREATE TABLE `devices` (
	id int PRIMARY KEY AUTO_INCREMENT, -- Unique id for record in table
	skey char(10), -- Key for devices
	svalue char(10) -- Value for devices
); 

DROP TABLE if exists `nodes`;
CREATE TABLE `nodes` (
	id int PRIMARY KEY AUTO_INCREMENT, -- Unique id for record in table
	skey char(10), -- Key for nodes
	svalue char(10) -- Value for nodes
);
