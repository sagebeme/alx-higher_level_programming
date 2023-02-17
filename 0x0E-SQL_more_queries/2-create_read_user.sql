-- Creates the database hbtn_0d_2 and with id and name
-- The user_0d_2 has SELECT privilege on hbtn_0d_2 with password user_0d_2_pwd
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;
CREATE TABLE
    IF NOT EXISTS `force_name`(
        `id`    INT,
        `name`  VARCHAR(256) NOT NULL
    );
