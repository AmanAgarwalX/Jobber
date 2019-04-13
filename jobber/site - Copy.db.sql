BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `user` (
	`id`	INTEGER NOT NULL,
	`type`	VARCHAR ( 10 ) NOT NULL,
	`email`	VARCHAR ( 120 ) NOT NULL UNIQUE,
	`name`	VARCHAR ( 120 ) NOT NULL,
	`profile_picture`	VARCHAR ( 50 ) NOT NULL,
	`password`	VARCHAR ( 12 ) NOT NULL,
	`company_name`	VARCHAR ( 120 ),
	`company_gst_number`	VARCHAR ( 120 ),
	`company_info`	TEXT,
	`position`	VARCHAR ( 120 ),
	`cv`	VARCHAR ( 50 ),
	PRIMARY KEY(`id`)
);
INSERT INTO `user` VALUES (1,'employer','aa@aa.com','anan','default.jpg','$2b$12$ouXATEywnW9nb8T29VIr8OdbeWQLpVDHVNVRio5PBstpLc3CskNfK','anan','anan','nana','anan','none.pdf');
INSERT INTO `user` VALUES (2,'employee','aa@aaa.com','Aman ','default.jpg','$2b$12$hU55zFjJYpX7Cj8luM.UruQGwPIkvFPXFGtzI9n4kFxVqwOf2Yjtu',NULL,NULL,NULL,NULL,'aa@aaa.com1554707195421.pdf');
INSERT INTO `user` VALUES (3,'employee','aaa@aaa.com','ana','default.jpg','$2b$12$MAeY199OdnePXpzE5Piwsel0GSeFgpCdI5k4ryI0ct3sKyUhhnAIy',NULL,NULL,NULL,NULL,'none.pdf');
INSERT INTO `user` VALUES (4,'employer','aman@aman.com','aa','default.jpg','$2b$12$rIxgsPnm47l0ih9OYoKBg.302SwhiKTpAVqlxUNVZx8RQhZybofiy','aa','aa','aa','aa','none.pdf');
CREATE TABLE IF NOT EXISTS `post` (
	`id`	INTEGER NOT NULL,
	`title`	VARCHAR ( 100 ) NOT NULL,
	`date_posted`	DATETIME NOT NULL,
	`content`	TEXT NOT NULL,
	`old_cv`	VARCHAR ( 50 ),
	`user_id`	INTEGER NOT NULL,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
);
INSERT INTO `post` VALUES (1,'Aman ','2019-04-08 07:06:06.787961','upload','aa@aaa.com1554707166623.pdf',2);
INSERT INTO `post` VALUES (2,'Aman ','2019-04-08 07:06:35.449572','upload','aa@aaa.com1554707195421.pdf',2);
CREATE TABLE IF NOT EXISTS `likes` (
	`user_id`	INTEGER,
	`post_id`	INTEGER,
	FOREIGN KEY(`post_id`) REFERENCES `post`(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
);
CREATE TABLE IF NOT EXISTS `job` (
	`id`	INTEGER NOT NULL,
	`title`	VARCHAR ( 100 ) NOT NULL,
	`location`	VARCHAR ( 100 ) NOT NULL,
	`typeofjob`	VARCHAR ( 100 ) NOT NULL,
	`salary`	INTEGER NOT NULL,
	`date_posted`	DATETIME NOT NULL,
	`description`	TEXT NOT NULL,
	`user_id`	INTEGER NOT NULL,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
);
INSERT INTO `job` VALUES (1,'aman','aman','aman',123,'2019-04-04 08:42:34.423184','aman',1);
INSERT INTO `job` VALUES (2,'aaa','aaa','aaa',1234,'2019-04-08 07:08:17.053523','aaa',4);
CREATE TABLE IF NOT EXISTS `interviews` (
	`user_id`	INTEGER,
	`interview_id`	INTEGER,
	FOREIGN KEY(`interview_id`) REFERENCES `interview`(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
);
CREATE TABLE IF NOT EXISTS `interview` (
	`id`	INTEGER NOT NULL,
	`title`	VARCHAR ( 100 ) NOT NULL,
	`location`	VARCHAR ( 100 ) NOT NULL,
	`time`	DATETIME NOT NULL,
	`description`	TEXT NOT NULL,
	`job`	INTEGER NOT NULL,
	FOREIGN KEY(`job`) REFERENCES `job`(`id`),
	PRIMARY KEY(`id`)
);
INSERT INTO `interview` VALUES (1,'a','a','2019-04-11 00:00:00.000000','a',1);
INSERT INTO `interview` VALUES (2,'aa','aa','2019-12-31 12:59:00.000000','aa',1);
INSERT INTO `interview` VALUES (3,'aa','aa','2019-12-31 12:59:00.000000','aa',2);
INSERT INTO `interview` VALUES (4,'aaa','a','2019-12-31 12:59:00.000000','aa',2);
COMMIT;
