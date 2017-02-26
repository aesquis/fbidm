# fbidm
Python script wich makes a follow back and direct message to a new Twitter followers with Tweepy

This script connects to your Twitter account and get all your followers screen_name, then compare with database stored in last execution and if there is new follows, makes a followback and sends it a private Message. Finally store again followers ant write all the movements to a log file.

1.- Configure your user and app Keys and Tokens in file keys.py
2.- Configure path for database and log
 
Database pickle
https://docs.python.org/2/library/pickle.html

Log with looging
https://docs.python.org/2/library/logging.html

 That's all
