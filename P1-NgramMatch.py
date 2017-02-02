import re
import ngram
import time
import random

starttime = time.time()

tweets = ""
t = ""
with open("mergfeih_tweets_small.txt","r",encoding = 'utf-8') as f1: #tweets
    lines = f1.readlines()
    interval = int(len(lines)*0.001)*10
    i = interval
    #print(interval)
    randomline = []
    while(i <= len(lines)):
        linenum = random.randint(i-interval,i)
        #print(linenum)
        #print(lines[linenum])
        randomline.append(lines[linenum])
        i += interval
    #print(len(randomline))
    for line in randomline:
        #print(line)
    #for line in f1:
        tweets = tweets+" "+line
    tweets = re.findall("[a-zA-Z]+(?:(?:\\s+|-)[a-zA-Z]+)*",tweets)
    #print(type(tweets))
    #tweets = tweets.split()
    #print(type(tweets))
    for tweet in tweets:
        t = t+" "+tweet
    t = t.split()
    #print(t)

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
        G = ngram.NGram(t)
        #print(G.search(loc))
        if(G.search(loc,threshold=0.5)):
            #print(G.search(loc))
            f = open("ngram_output.txt","a",encoding = 'utf-8')
            f.write("%s\n" %loc)
            print(loc)

f = open("ngram_output.txt","a")
f.write("time: %s seconds." %(time.time() - starttime))
print("time: %s seconds." %(time.time() - starttime))

f.close()
f1.close()
f2.close()
