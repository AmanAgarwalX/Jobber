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
INSERT INTO `user` VALUES (2,'employee','aa@aaa.com','Aman','default.jpg','$2b$12$hU55zFjJYpX7Cj8luM.UruQGwPIkvFPXFGtzI9n4kFxVqwOf2Yjtu','','','','','aa@aaa.com1554707195421.pdf');
INSERT INTO `user` VALUES (3,'employee','aaa@aaa.com','ana','default.jpg','$2b$12$MAeY199OdnePXpzE5Piwsel0GSeFgpCdI5k4ryI0ct3sKyUhhnAIy','','','','','aaa@aaa.com1555038290105.pdf');
INSERT INTO `user` VALUES (4,'employer','aman@aman.com','aa','default.jpg','$2b$12$rIxgsPnm47l0ih9OYoKBg.302SwhiKTpAVqlxUNVZx8RQhZybofiy','aa','aa','aa','aa','none.pdf');
INSERT INTO `user` VALUES (5,'employee','hi@hi.com','yo','default.jpg','some',NULL,NULL,NULL,NULL,'none.pdf');
CREATE TABLE IF NOT EXISTS `likes` (
	`user_id`	INTEGER,
	`post_id`	INTEGER,
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`),
	FOREIGN KEY(`post_id`) REFERENCES `post`(`id`)
);
CREATE TABLE IF NOT EXISTS `keywords` (
	`user_id`	INTEGER,
	`keyword_title`	INTEGER,
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`),
	FOREIGN KEY(`keyword_title`) REFERENCES `keyword`(`title`)
);
INSERT INTO `keywords` VALUES (3,'untitled');
INSERT INTO `keywords` VALUES (3,'spreadsheet');
INSERT INTO `keywords` VALUES (3,'teri');
INSERT INTO `keywords` VALUES (3,'dhadkan');
INSERT INTO `keywords` VALUES (3,'hi');
INSERT INTO `keywords` VALUES (3,'jindagi');
INSERT INTO `keywords` VALUES (3,'ka');
INSERT INTO `keywords` VALUES (3,'hissa');
INSERT INTO `keywords` VALUES (3,'hai');
INSERT INTO `keywords` VALUES (3,'maera');
INSERT INTO `keywords` VALUES (3,'dilip');
INSERT INTO `keywords` VALUES (3,'bhaiya');
INSERT INTO `keywords` VALUES (3,'saarvi');
INSERT INTO `keywords` VALUES (3,'tu');
INSERT INTO `keywords` VALUES (3,'ek');
INSERT INTO `keywords` VALUES (3,'aham');
INSERT INTO `keywords` VALUES (3,'mera');
INSERT INTO `keywords` VALUES (3,'mohaabbat');
INSERT INTO `keywords` VALUES (3,'aur');
INSERT INTO `keywords` VALUES (3,'meri');
INSERT INTO `keywords` VALUES (3,'fitrat');
INSERT INTO `keywords` VALUES (3,'mein');
INSERT INTO `keywords` VALUES (3,'fark');
INSERT INTO `keywords` VALUES (3,'itna');
INSERT INTO `keywords` VALUES (3,'ankit');
INSERT INTO `keywords` VALUES (3,'tera');
INSERT INTO `keywords` VALUES (3,'attitude');
INSERT INTO `keywords` VALUES (3,'nahi');
INSERT INTO `keywords` VALUES (3,'jaata');
INSERT INTO `keywords` VALUES (3,'mujhe');
INSERT INTO `keywords` VALUES (3,'jhukna');
INSERT INTO `keywords` VALUES (3,'aata');
INSERT INTO `keywords` VALUES (3,'ruchi');
INSERT INTO `keywords` VALUES (3,'jeene');
INSERT INTO `keywords` VALUES (3,'sahara');
INSERT INTO `keywords` VALUES (3,'hoti');
INSERT INTO `keywords` VALUES (3,'choti');
INSERT INTO `keywords` VALUES (3,'khusiyan');
INSERT INTO `keywords` VALUES (3,'anju');
INSERT INTO `keywords` VALUES (3,'bhabhi');
INSERT INTO `keywords` VALUES (3,'khwaise');
INSERT INTO `keywords` VALUES (3,'yuhi');
INSERT INTO `keywords` VALUES (3,'har');
INSERT INTO `keywords` VALUES (3,'roj');
INSERT INTO `keywords` VALUES (3,'badalti');
INSERT INTO `keywords` VALUES (3,'rahti');
INSERT INTO `keywords` VALUES (3,'khush');
INSERT INTO `keywords` VALUES (3,'hu');
INSERT INTO `keywords` VALUES (3,'apni');
INSERT INTO `keywords` VALUES (3,'si');
INSERT INTO `keywords` VALUES (3,'kaamyabi');
INSERT INTO `keywords` VALUES (3,'par');
INSERT INTO `keywords` VALUES (3,'kadmo');
INSERT INTO `keywords` VALUES (3,'ki');
INSERT INTO `keywords` VALUES (3,'raftar');
INSERT INTO `keywords` VALUES (3,'dhimi');
INSERT INTO `keywords` VALUES (3,'jarur');
INSERT INTO `keywords` VALUES (3,'anup');
INSERT INTO `keywords` VALUES (3,'jitni');
INSERT INTO `keywords` VALUES (3,'apne');
INSERT INTO `keywords` VALUES (3,'jamir');
INSERT INTO `keywords` VALUES (3,'ke');
INSERT INTO `keywords` VALUES (3,'saath');
INSERT INTO `keywords` VALUES (3,'maut');
INSERT INTO `keywords` VALUES (3,'mohabbat');
INSERT INTO `keywords` VALUES (3,'sirf');
INSERT INTO `keywords` VALUES (3,'naam');
INSERT INTO `keywords` VALUES (3,'se');
INSERT INTO `keywords` VALUES (3,'badnaam');
INSERT INTO `keywords` VALUES (3,'aman');
INSERT INTO `keywords` VALUES (3,'asli');
INSERT INTO `keywords` VALUES (3,'drd');
INSERT INTO `keywords` VALUES (3,'internet');
INSERT INTO `keywords` VALUES (3,'failure');
INSERT INTO `keywords` VALUES (3,'deta');
INSERT INTO `keywords` VALUES (3,'sahare');
INSERT INTO `keywords` VALUES (3,'dhundhne');
INSERT INTO `keywords` VALUES (3,'aadat');
INSERT INTO `keywords` VALUES (3,'hamari');
INSERT INTO `keywords` VALUES (3,'mahavir');
INSERT INTO `keywords` VALUES (3,'jijaaji');
INSERT INTO `keywords` VALUES (3,'hum');
INSERT INTO `keywords` VALUES (3,'akele');
INSERT INTO `keywords` VALUES (3,'puri');
INSERT INTO `keywords` VALUES (3,'mehfil');
INSERT INTO `keywords` VALUES (3,'barabar');
INSERT INTO `keywords` VALUES (3,'din');
INSERT INTO `keywords` VALUES (3,'mujhse');
INSERT INTO `keywords` VALUES (3,'lipat');
INSERT INTO `keywords` VALUES (3,'kar');
INSERT INTO `keywords` VALUES (3,'samay');
INSERT INTO `keywords` VALUES (3,'bhi');
INSERT INTO `keywords` VALUES (3,'royega');
INSERT INTO `keywords` VALUES (3,'sandip');
INSERT INTO `keywords` VALUES (3,'kahega');
INSERT INTO `keywords` VALUES (3,'banda');
INSERT INTO `keywords` VALUES (3,'sahi');
INSERT INTO `keywords` VALUES (3,'tha');
INSERT INTO `keywords` VALUES (3,'main');
INSERT INTO `keywords` VALUES (3,'kharab');
INSERT INTO `keywords` VALUES (3,'chal');
INSERT INTO `keywords` VALUES (3,'raha');
INSERT INTO `keywords` VALUES (3,'muskan');
INSERT INTO `keywords` VALUES (3,'koi');
INSERT INTO `keywords` VALUES (3,'mol');
INSERT INTO `keywords` VALUES (3,'hota');
INSERT INTO `keywords` VALUES (3,'kuch');
INSERT INTO `keywords` VALUES (3,'rishto');
INSERT INTO `keywords` VALUES (3,'tol');
INSERT INTO `keywords` VALUES (3,'mil');
INSERT INTO `keywords` VALUES (3,'jaate');
INSERT INTO `keywords` VALUES (3,'raste');
INSERT INTO `keywords` VALUES (3,'lekin');
INSERT INTO `keywords` VALUES (3,'aapki');
INSERT INTO `keywords` VALUES (3,'ntarah');
INSERT INTO `keywords` VALUES (3,'anmol');
INSERT INTO `keywords` VALUES (3,'neeru');
INSERT INTO `keywords` VALUES (3,'pagal');
INSERT INTO `keywords` VALUES (3,'jo');
INSERT INTO `keywords` VALUES (3,'baat');
INSERT INTO `keywords` VALUES (3,'maanta');
INSERT INTO `keywords` VALUES (3,'kushal');
INSERT INTO `keywords` VALUES (3,'ji');
INSERT INTO `keywords` VALUES (3,'bas');
INSERT INTO `keywords` VALUES (3,'khusi');
INSERT INTO `keywords` VALUES (3,'accha');
INSERT INTO `keywords` VALUES (3,'lagta');
INSERT INTO `keywords` VALUES (3,'logo');
INSERT INTO `keywords` VALUES (3,'k');
INSERT INTO `keywords` VALUES (3,'pyar');
INSERT INTO `keywords` VALUES (3,'kabhi');
INSERT INTO `keywords` VALUES (3,'badalta');
INSERT INTO `keywords` VALUES (3,'parents');
INSERT INTO `keywords` VALUES (3,'duniya');
INSERT INTO `keywords` VALUES (3,'unhe');
INSERT INTO `keywords` VALUES (3,'baap');
INSERT INTO `keywords` VALUES (3,'kehte');
INSERT INTO `keywords` VALUES (3,'aisa');
INSERT INTO `keywords` VALUES (3,'aaye');
INSERT INTO `keywords` VALUES (3,'anisha');
INSERT INTO `keywords` VALUES (3,'jiski');
INSERT INTO `keywords` VALUES (3,'mummy');
INSERT INTO `keywords` VALUES (3,'kaam');
INSERT INTO `keywords` VALUES (3,'na');
INSERT INTO `keywords` VALUES (3,'karwaye');
INSERT INTO `keywords` VALUES (3,'kaha');
INSERT INTO `keywords` VALUES (3,'milta');
INSERT INTO `keywords` VALUES (3,'samajhne');
INSERT INTO `keywords` VALUES (3,'wala');
INSERT INTO `keywords` VALUES (3,'ayush');
INSERT INTO `keywords` VALUES (3,'sab');
INSERT INTO `keywords` VALUES (3,'samjha');
INSERT INTO `keywords` VALUES (3,'chale');
INSERT INTO `keywords` VALUES (3,'haath');
INSERT INTO `keywords` VALUES (3,'thame');
INSERT INTO `keywords` VALUES (3,'rakhna');
INSERT INTO `keywords` VALUES (3,'bheed');
INSERT INTO `keywords` VALUES (3,'bhari');
INSERT INTO `keywords` VALUES (3,'kho');
INSERT INTO `keywords` VALUES (3,'jau');
INSERT INTO `keywords` VALUES (3,'kahi');
INSERT INTO `keywords` VALUES (3,'ye');
INSERT INTO `keywords` VALUES (3,'jimmedari');
INSERT INTO `keywords` VALUES (3,'tumhari');
INSERT INTO `keywords` VALUES (3,'juth');
INSERT INTO `keywords` VALUES (3,'lalach');
INSERT INTO `keywords` VALUES (3,'fareb');
INSERT INTO `keywords` VALUES (3,'pare');
INSERT INTO `keywords` VALUES (3,'khuda');
INSERT INTO `keywords` VALUES (3,'shukra');
INSERT INTO `keywords` VALUES (3,'aaj');
INSERT INTO `keywords` VALUES (3,'yaha');
INSERT INTO `keywords` VALUES (3,'khade');
CREATE TABLE IF NOT EXISTS `keyword` (
	`title`	VARCHAR ( 100 ) NOT NULL,
	PRIMARY KEY(`title`)
);
INSERT INTO `keyword` VALUES ('aman');
INSERT INTO `keyword` VALUES ('untitled');
INSERT INTO `keyword` VALUES ('spreadsheet');
INSERT INTO `keyword` VALUES ('teri');
INSERT INTO `keyword` VALUES ('dhadkan');
INSERT INTO `keyword` VALUES ('hi');
INSERT INTO `keyword` VALUES ('jindagi');
INSERT INTO `keyword` VALUES ('ka');
INSERT INTO `keyword` VALUES ('hissa');
INSERT INTO `keyword` VALUES ('hai');
INSERT INTO `keyword` VALUES ('maera');
INSERT INTO `keyword` VALUES ('dilip');
INSERT INTO `keyword` VALUES ('bhaiya');
INSERT INTO `keyword` VALUES ('saarvi');
INSERT INTO `keyword` VALUES ('tu');
INSERT INTO `keyword` VALUES ('ek');
INSERT INTO `keyword` VALUES ('aham');
INSERT INTO `keyword` VALUES ('mera');
INSERT INTO `keyword` VALUES ('mohaabbat');
INSERT INTO `keyword` VALUES ('aur');
INSERT INTO `keyword` VALUES ('meri');
INSERT INTO `keyword` VALUES ('fitrat');
INSERT INTO `keyword` VALUES ('mein');
INSERT INTO `keyword` VALUES ('fark');
INSERT INTO `keyword` VALUES ('itna');
INSERT INTO `keyword` VALUES ('ankit');
INSERT INTO `keyword` VALUES ('tera');
INSERT INTO `keyword` VALUES ('attitude');
INSERT INTO `keyword` VALUES ('nahi');
INSERT INTO `keyword` VALUES ('jaata');
INSERT INTO `keyword` VALUES ('mujhe');
INSERT INTO `keyword` VALUES ('jhukna');
INSERT INTO `keyword` VALUES ('aata');
INSERT INTO `keyword` VALUES ('ruchi');
INSERT INTO `keyword` VALUES ('jeene');
INSERT INTO `keyword` VALUES ('sahara');
INSERT INTO `keyword` VALUES ('hoti');
INSERT INTO `keyword` VALUES ('choti');
INSERT INTO `keyword` VALUES ('khusiyan');
INSERT INTO `keyword` VALUES ('anju');
INSERT INTO `keyword` VALUES ('bhabhi');
INSERT INTO `keyword` VALUES ('khwaise');
INSERT INTO `keyword` VALUES ('yuhi');
INSERT INTO `keyword` VALUES ('har');
INSERT INTO `keyword` VALUES ('roj');
INSERT INTO `keyword` VALUES ('badalti');
INSERT INTO `keyword` VALUES ('rahti');
INSERT INTO `keyword` VALUES ('khush');
INSERT INTO `keyword` VALUES ('hu');
INSERT INTO `keyword` VALUES ('apni');
INSERT INTO `keyword` VALUES ('si');
INSERT INTO `keyword` VALUES ('kaamyabi');
INSERT INTO `keyword` VALUES ('par');
INSERT INTO `keyword` VALUES ('kadmo');
INSERT INTO `keyword` VALUES ('ki');
INSERT INTO `keyword` VALUES ('raftar');
INSERT INTO `keyword` VALUES ('dhimi');
INSERT INTO `keyword` VALUES ('jarur');
INSERT INTO `keyword` VALUES ('anup');
INSERT INTO `keyword` VALUES ('jitni');
INSERT INTO `keyword` VALUES ('apne');
INSERT INTO `keyword` VALUES ('jamir');
INSERT INTO `keyword` VALUES ('ke');
INSERT INTO `keyword` VALUES ('saath');
INSERT INTO `keyword` VALUES ('maut');
INSERT INTO `keyword` VALUES ('mohabbat');
INSERT INTO `keyword` VALUES ('sirf');
INSERT INTO `keyword` VALUES ('naam');
INSERT INTO `keyword` VALUES ('se');
INSERT INTO `keyword` VALUES ('badnaam');
INSERT INTO `keyword` VALUES ('asli');
INSERT INTO `keyword` VALUES ('drd');
INSERT INTO `keyword` VALUES ('internet');
INSERT INTO `keyword` VALUES ('failure');
INSERT INTO `keyword` VALUES ('deta');
INSERT INTO `keyword` VALUES ('sahare');
INSERT INTO `keyword` VALUES ('dhundhne');
INSERT INTO `keyword` VALUES ('aadat');
INSERT INTO `keyword` VALUES ('hamari');
INSERT INTO `keyword` VALUES ('mahavir');
INSERT INTO `keyword` VALUES ('jijaaji');
INSERT INTO `keyword` VALUES ('hum');
INSERT INTO `keyword` VALUES ('akele');
INSERT INTO `keyword` VALUES ('puri');
INSERT INTO `keyword` VALUES ('mehfil');
INSERT INTO `keyword` VALUES ('barabar');
INSERT INTO `keyword` VALUES ('din');
INSERT INTO `keyword` VALUES ('mujhse');
INSERT INTO `keyword` VALUES ('lipat');
INSERT INTO `keyword` VALUES ('kar');
INSERT INTO `keyword` VALUES ('samay');
INSERT INTO `keyword` VALUES ('bhi');
INSERT INTO `keyword` VALUES ('royega');
INSERT INTO `keyword` VALUES ('sandip');
INSERT INTO `keyword` VALUES ('kahega');
INSERT INTO `keyword` VALUES ('banda');
INSERT INTO `keyword` VALUES ('sahi');
INSERT INTO `keyword` VALUES ('tha');
INSERT INTO `keyword` VALUES ('main');
INSERT INTO `keyword` VALUES ('kharab');
INSERT INTO `keyword` VALUES ('chal');
INSERT INTO `keyword` VALUES ('raha');
INSERT INTO `keyword` VALUES ('muskan');
INSERT INTO `keyword` VALUES ('koi');
INSERT INTO `keyword` VALUES ('mol');
INSERT INTO `keyword` VALUES ('hota');
INSERT INTO `keyword` VALUES ('kuch');
INSERT INTO `keyword` VALUES ('rishto');
INSERT INTO `keyword` VALUES ('tol');
INSERT INTO `keyword` VALUES ('mil');
INSERT INTO `keyword` VALUES ('jaate');
INSERT INTO `keyword` VALUES ('raste');
INSERT INTO `keyword` VALUES ('lekin');
INSERT INTO `keyword` VALUES ('aapki');
INSERT INTO `keyword` VALUES ('ntarah');
INSERT INTO `keyword` VALUES ('anmol');
INSERT INTO `keyword` VALUES ('neeru');
INSERT INTO `keyword` VALUES ('pagal');
INSERT INTO `keyword` VALUES ('jo');
INSERT INTO `keyword` VALUES ('baat');
INSERT INTO `keyword` VALUES ('maanta');
INSERT INTO `keyword` VALUES ('kushal');
INSERT INTO `keyword` VALUES ('ji');
INSERT INTO `keyword` VALUES ('bas');
INSERT INTO `keyword` VALUES ('khusi');
INSERT INTO `keyword` VALUES ('accha');
INSERT INTO `keyword` VALUES ('lagta');
INSERT INTO `keyword` VALUES ('logo');
INSERT INTO `keyword` VALUES ('k');
INSERT INTO `keyword` VALUES ('pyar');
INSERT INTO `keyword` VALUES ('kabhi');
INSERT INTO `keyword` VALUES ('badalta');
INSERT INTO `keyword` VALUES ('parents');
INSERT INTO `keyword` VALUES ('duniya');
INSERT INTO `keyword` VALUES ('unhe');
INSERT INTO `keyword` VALUES ('baap');
INSERT INTO `keyword` VALUES ('kehte');
INSERT INTO `keyword` VALUES ('aisa');
INSERT INTO `keyword` VALUES ('aaye');
INSERT INTO `keyword` VALUES ('anisha');
INSERT INTO `keyword` VALUES ('jiski');
INSERT INTO `keyword` VALUES ('mummy');
INSERT INTO `keyword` VALUES ('kaam');
INSERT INTO `keyword` VALUES ('na');
INSERT INTO `keyword` VALUES ('karwaye');
INSERT INTO `keyword` VALUES ('kaha');
INSERT INTO `keyword` VALUES ('milta');
INSERT INTO `keyword` VALUES ('samajhne');
INSERT INTO `keyword` VALUES ('wala');
INSERT INTO `keyword` VALUES ('ayush');
INSERT INTO `keyword` VALUES ('sab');
INSERT INTO `keyword` VALUES ('samjha');
INSERT INTO `keyword` VALUES ('chale');
INSERT INTO `keyword` VALUES ('haath');
INSERT INTO `keyword` VALUES ('thame');
INSERT INTO `keyword` VALUES ('rakhna');
INSERT INTO `keyword` VALUES ('bheed');
INSERT INTO `keyword` VALUES ('bhari');
INSERT INTO `keyword` VALUES ('kho');
INSERT INTO `keyword` VALUES ('jau');
INSERT INTO `keyword` VALUES ('kahi');
INSERT INTO `keyword` VALUES ('ye');
INSERT INTO `keyword` VALUES ('jimmedari');
INSERT INTO `keyword` VALUES ('tumhari');
INSERT INTO `keyword` VALUES ('juth');
INSERT INTO `keyword` VALUES ('lalach');
INSERT INTO `keyword` VALUES ('fareb');
INSERT INTO `keyword` VALUES ('pare');
INSERT INTO `keyword` VALUES ('khuda');
INSERT INTO `keyword` VALUES ('shukra');
INSERT INTO `keyword` VALUES ('aaj');
INSERT INTO `keyword` VALUES ('yaha');
INSERT INTO `keyword` VALUES ('khade');
CREATE TABLE IF NOT EXISTS `jobs_applied` (
	`user_id`	INTEGER,
	`job_id`	INTEGER,
	`selected`	INTEGER,
	FOREIGN KEY(`job_id`) REFERENCES `job`(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
);
INSERT INTO `jobs_applied` VALUES (3,2,0);
INSERT INTO `jobs_applied` VALUES (3,3,0);
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
INSERT INTO `job` VALUES (2,'aaa','aaa','aaa',1234,'2019-04-08 07:08:17.053523','aaa',4);
INSERT INTO `job` VALUES (3,'new job','kolkata','it',500000,'2019-04-12 01:32:26.779690','very good job',1);
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
	PRIMARY KEY(`id`),
	FOREIGN KEY(`job`) REFERENCES `job`(`id`)
);
INSERT INTO `interview` VALUES (3,'aa','aa','2019-12-31 12:59:00.000000','aa',2);
INSERT INTO `interview` VALUES (4,'aaa','a','2019-12-31 12:59:00.000000','aa',2);
INSERT INTO `interview` VALUES (5,'new interview','bara bazaar','2019-12-31 12:59:00.000000','important interview',3);
COMMIT;
