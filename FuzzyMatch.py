import time
import re
from fuzzywuzzy import fuzz
import random

starttime = time.time()

tweets = []
with open("mergfeih_tweets_small.txt","r",encoding = 'utf-8') as f1: #tweets
        lines = f1.readlines()
        interval = int(len(lines)*0.001)*10 #find lines randomly by interval
        i = interval
        #print(i)
        randomline = []
        while(i <= len(lines)):
                linenum = random.randint(i-interval,i)
                #print(linenum)
                #print(lines[linenum])
                randomline.append(lines[linenum])
                i+= interval
        #print(len(randomline))
        
        for line in randomline:
                #print(line)
        #for line in f1:
                #words = line.split()
                #for word in words:
                matchloc = re.findall("[a-zA-Z]+(?:(?:\\s+|-)[a-zA-Z]+)*",line) #match location name pattern in tweets
                if matchloc:
                        tweets.append(matchloc)

locnames = []
loclist = []                        
with open("US-loc-names.txt","r",encoding = 'utf-8') as f2:#locnames
    for line in f2:
        line = ''.join([i for i in line if not i.isdigit()])
        line = line.split()
        locnames.append(line)
    for locname in locnames:
        for i in range(len(locname)):
            loclist.append(locname[i])
    setloc = set(loclist)
    listloc = list(setloc)

    for loc in listloc:
        #print(fuzz.token_set_ratio(loc,tweets))
        if (fuzz.token_set_ratio(loc,tweets) in range(80,100)):
                f = open("fuzzy_output.txt","a",encoding = 'utf-8')
                f.write("%d\n" %fuzz.token_set_ratio(loc,tweets))
                f.write("%s\n" %loc)
                print(fuzz.token_set_ratio(loc,tweets))
                print(loc)
            
f = open("fuzzy_output.txt","a")
f.write("time: %s seconds." %(time.time() - starttime))
print("time: %s seconds." %(time.time() - starttime))

f.close()
f1.close()
f2.close()
