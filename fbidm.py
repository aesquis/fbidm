#! /usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
from keys import keys
import pickle
import time
import logging
 
#Credem les Keys
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
logger = logging.getLogger('fbidm')
hdlr = logging.FileHandler('/xxxxxxxxx')   #Here you have to inform your path for log file. Like /home/user/fbidm/fbidm.log
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
 
logger.info('Inici de les tasques')
 
#definim l'api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
#Definim les llistes que utilitzarem
followList =[]
destinataris =[]
 
#Contar nombre de followers per el log
user = api.get_user('eltempsavic')
logger.info ('Ara tens %s followers ',user.followers_count)
 
#agafem tots els noms de follower i els afegim dins la llista
try:
        for follower in tweepy.Cursor(api.followers).items():
                followList.append(follower.screen_name)
        logger.info('Get followers list ok!')
except Exception as e:
        logger.exception("message")
 
#agafar id's dels followers i afegir en la llista
#agafar id's dels followers i afegir en la llista
#for ids in tweepy.Cursor(api.followers_ids).items():
#       followList.append(ids)
 
#definim el que serà l'arxiu de la base de dades
file_name = '/pat_for_database'   #Here you have to inform your path for db file. Like /home/user/fbidm/db
 
#Obrim l'arxiu per lectura
try:
        fileObject = open(file_name,'r')
except Exception as e:
        logger.exception("message")
 
# Carreguem la base de dades en una llista
enviats = pickle.load(fileObject)
 
#Comparem entre els followers i la base de dades que teniem guardada 
#i afegim les discrepàncies a la llista destinataris
destinataris =
 
 
# Fer el follow back dels usuaris de la llista destinataris
try:
        def fb():
                for follower in destinataris:
                        api.create_friendship(follower)
                        logger.info('Follow to %s OK', follower)
 
except Exception as e:
        logger.exception("message")
 
# Fer Direct Message a usuaris de la llista destinataris
try:
        def sd():
                for follower in destinataris:
                        missatge = "Moltes gràcies per el teu interès, esperem que gaudeixes del temps"
                        api.send_direct_message(screen_name=follower, text = missatge )
                        logger.info('Direct Message to %s OK', follower)
 
                        except Exception as e:
        logger.exception("message")
 
#Tancar el fitxer de lectura
fileObject.close()
 
fb()
sd()
 
#Procés de regenerar la base de dades
try:
        fileObject = open(file_name, 'wb')
        pickle.dump(followList,fileObject)
        logger.info('Base de dades regenerada OK')
except Exception as e:
        logger.exception("message")
 
 
# tanquem fitxer
fileObject.close()
logger.info('Fi de les tasques')
print ("Resultat OK")
