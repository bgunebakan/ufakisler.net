CREATE DATABASE  IF NOT EXISTS `ufakisler` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_turkish_ci */;
USE `ufakisler`;
CREATE USER 'web_user'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON ufakisler.* TO 'web_user'@'localhost';
FLUSH PRIVILEGES;
#
