import os
import re
import webbrowser
import smtplib
import time
import datetime
import requests
import subprocess
import urllib.request
import urllib3
import selenium
from selenium import webdriver
import fbchat
from fbchat.models import *
from fbchat import Client
from itertools import islice
from fbchat.models import ThreadType, Message
thread_type = ThreadType.USER
image='/Users/Dell/Desktop/Echipe wildcats/alte stiri/a.jpg'

#client1= Client('zaharie_andrei66@yahoo.com','Andreius2007')
folder='/Users/Dell/Desktop/temaroamana/'
nr=0
def verificare(x):
        user = client1.fetchAllUsers()
        #enter the name of your friends that you want to save phothos from them
        clasa=["Daniela Cucicea","Marozsan Alex","Claudiu Span","Denis Dragos","Zimbru Andrei","Paul Gavriș","Dana Buciuman",
               "Ioana Poduț","Mihai Tomoiagă","Vlad Radu","Alex Breban","Vlad Victor Zamuruev","Roland Telegdi",
               "Sebastian Grec","Cezar Cozmuta","Dieter Breitkopf","Tudor Poran","Andreea Rusan","Zah Andrei",
               "Catalin Cardos","Mircea Hanganu","Razvan Both","Szabo Mark","Denis Cadar","Andrei Zaharie","Elian Borcut"];
        for k in range(0,len(user)):
            if x==user[k].uid:
                for i in range(0,len(clasa)):
                    if clasa[i] in user[k].name:
                        #print(user[k].name)
                        return 1
        return 0
def denumire(x):
        user = client1.fetchAllUsers()
        clasa=["Daniela Cucicea","Marozsan Alex","Claudiu Span","Denis Dragos","Zimbru Andrei","Paul Gavriș","Dana Buciuman",
               "Ioana Poduț","Mihai Tomoiagă","Vlad Radu","Alex Breban","Vlad Victor Zamuruev","Roland Telegdi",
               "Sebastian Grec","Cezar Cozmuta","Dieter Breitkopf","Tudor Poran","Andreea Rusan","Zah Andrei",
               "Catalin Cardos","Mircea Hanganu","Razvan Both","Szabo Mark","Denis Cadar","Andrei Zaharie"];
        for k in range(0,len(user)):
            if x==user[k].uid:
                for i in range(0,len(clasa)):
                    if clasa[i] in user[k].name:
                        print(user[k].name)
                        return user[k].name


                
def salvare(url,folder,nume,extensie):
    folderr=folder+nume+'.'+extensie
    urllib.request.urlretrieve(url,folderr)
    print('salvare incheiata cu succes')
k=0
class TestBot(Client):
    def onMessage(
        self, mid=None, 
        author_id=None, 
        message=None, 
        message_object=None, 
        thread_id=None, 
        thread_type=ThreadType.USER, 
        ts=None, metadata=None, msg=None
    ):
           global k
           if message_object.text == None:
                print("S-a trimis o imagine")
                for i in range(0,len(message_object.attachments)):
                        url=message_object.attachments[i].large_preview_url
                        #print(message_object.attachments[i].large_preview_url)
                        if url:
                           extensie=message_object.attachments[i].original_extension
                           x=message_object.author
                           if verificare(x)== 1 and thread_type != ThreadType.GROUP:
                                global folder
                                nume= denumire(x)
                                global nr
                                nume= nume+str(nr)
                                nr=nr+1
                                salvare(url,folder,nume,extensie)
                                print('poza cu numarul',i)
           print(message_object.text)
           k=k+1
           if k == 12:
                time.sleep(2)
                os.system('cls')
                print("+++++++++++++++++Programul e activ++++++++++++++++++++")
                k=0
            #print(message_object.attachments[i].large_preview_url)
            #print(message_object.attachments[0].large_preview_url)
            #print(message_object.uid)
           
client1=TestBot('your email for mess','your password password')

client1.listen()



