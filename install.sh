#!/bin/bash

sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev
sudo apt-get install python-mysqldb
sudo apt-get install mysql-server
cd ..
virtualenv ./ufakisler.net/
source ./ufakisler.net/bin/activate
cd ufakisler.net
pip install -U -r requirements.txt
echo "installation is done"
echo "--------------------"
echo "   MYSQL SETTINGS   "
echo "--------------------"

echo "CREATE DATABASE  IF NOT EXISTS `ufakisler` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_turkish_ci */;"
echo "USE `ufakisler`;"
echo "CREATE USER 'web_user'@'localhost' IDENTIFIED BY '123456';"
echo "GRANT ALL PRIVILEGES ON ufakisler.* TO 'web_user'@'localhost';"
echo "FLUSH PRIVILEGES;"
mysql < mysql.sql -u root -p 
