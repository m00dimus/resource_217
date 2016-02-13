DROP TABLE if exists `devices`;
CREATE TABLE `devices` (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique id for record in table
	skey TEXT, -- Key for devices
	svalue TEXT -- Value for devices
); 

DROP TABLE if exists `nodes`;
CREATE TABLE `nodes` (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique id for record in table
	skey TEXT, -- Key for nodes
	svalue TEXT -- Value for nodes
);
