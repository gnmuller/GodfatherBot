#! python3

#Quotes from the godfather 
#Made into tweets

from random import randrange
from random import randint
import re 




#Godfather 2 script parsing


SecondFullScript = open("GodfatherTwoScript.txt", "rt")

GFTwodata = SecondFullScript.read()

#Create list of to delete:

delete_list = ["\t", "THE GODFATHER","FADE FROM BLACK:", "DON CORLEONE", "BONASERA", "SONNY", "SANDRA", "CLEMENZA", "PAULIE", "NAZORINE", "HAGEN", "(O.S.)", "INT DAY", "INT NIGHT",
"EXT DAY","MALL", "(SUMMER 1945)", "KAY", "MICHEAL", "(AMUSED)","WEDDING PARTY", "CARLO", "(WHISPERED)", "WOMAN", "DON'S HALL & STAIRS" " : ", "(IMPRESSED)", "(NODDING)", "MALL TABLES", "DON'S OFFICE",]


for item in delete_list:
    GFTwodata = GFTwodata.replace(item, ' ')

with open ('GodfatherTwoScript.txt', 'rt') as GFST:
    GFTwoLines = [line.strip() for line in GFST]

SecondFullScript.close()

while ("" in GFTwoLines):
    GFTwoLines.remove("")
    
GFTwoLines = [x.replace ('\t', ' ') for x in GFTwoLines]

#checking to make sure that it works
#print (GFTwoLines)

#read Godfather 1 One Script

FSA = open("Full_Script.txt")

Bigdata = FSA.read()

for item in delete_list:
    Bigdata = Bigdata.replace(item, ' ')
    
with open ('Full_Script.txt', 'rt') as FS:
    MoreLines = [line.strip() for line in FS]

FSA.close()

while ("" in MoreLines):
    MoreLines.remove("")
    
MoreLines = [x.replace ('\t', ' ') for x in MoreLines]

#print( MoreLines2)

#if out of things to tweet, have a protocol

#tweet out stuff

import tweepy
import random

auth = tweepy.OAuthHandler(" ", 
    " ")
auth.set_access_token(" ", " ")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


random_index = randrange(len(GFTwoLines))
GFTitem = GFTwoLines [random_index]
GFTolditem = GFTwoLines [random_index - 1]
GFTnewitem = GFTwoLines [random_index +1]

GFTtweet = GFTolditem + " " + GFTitem + " " + GFTnewitem
#print(GFTtweet)
GFTsplittweet = re.sub ("\." , '\n\n', GFTtweet)

#print( "space")
print (GFTsplittweet)

random_index = randrange(len(MoreLines))
MLitem = MoreLines[random_index]
MLolditem = MoreLines [random_index - 1]
MLnewitem = MoreLines [random_index +1]

MLtweet = MLolditem + " " + MLitem + " " + MLnewitem
#print(MLtweet)
MLsplittweet = re.sub ("\." , '\n\n', MLtweet)

#print( "space")
print (MLsplittweet)

# splittweet1 = re.sub ( "\!", '\n\n', tweet)
# splittweet2 = re.sub ( "\;", '\n\n', tweet)
# splittweet3 = re.sub ( "\?", '\n\n', tweet)


#print (splittweet)

OneOrTwo = random.randint(1,2)

if OneOrTwo == 1:
    api.update_status(status = MLsplittweet)
if OneOrTwo == 2: 
    api.update_status(status = GFTsplittweet)


