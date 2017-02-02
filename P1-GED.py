import re
import time
import random

starttime = time.time()

def GED (f,t):
    m = 1
    i = -1
    d = -1
    r = -1

    def equal(ch1,ch2):
        if ch1==ch2:
            return m
        if ch1!=ch2:
            return r;

    A = [[-999 for x in range(len(t)+1)] for x in range(len(f)+1)]
    #print(A)

    for j in range(len(f)+1):
        A[j][0] = j*d
    for k in range(len(t)+1):
        A[0][k] = k*i

    for j in range(1,len(f)+1):
        for k in range(1,len(t)+1):
            A[j][k]= max(A[j][k-1]+d,A[j-1][k]+i,A[j-1][k-1]+equal(f[j-1],t[k-1]))

    #print(A)
    return (A[len(f)][len(t)])
    #length = min(len(f),len(t))
    #matchRatio = A[len(f)][len(t)]/length
    #return(matchRatio)

tweets = ""
t = ""
locnames = []
loclist = []
with open("mergfeih_tweets_small.txt","r",encoding = 'utf-8') as f1, open("US-loc-names.txt","r",encoding = 'utf-8') as f2:
    lines = f1.readlines()
    interval = int(len(lines)*0.001)*100
    i = interval
    randomline = []
    while(i <= len(lines)):
        linenum = random.randint(i-interval,i)
        randomline.append(lines[linenum])
        i += interval
        
    for line in randomline:
        tweets = tweets+" "+line
    tweets = re.findall("[a-zA-Z]+(?:(?:\\s+|-)[a-zA-Z]+)*",tweets)
    #print(tweets)
    for tweet in tweets:
        t = t+" "+tweet
    t = t.split()

    for line in f2:
        line = ''.join([i for i in line if not i.isdigit()])
        line = line.split()
        locnames.append(line)
    for locname in locnames:
        for i in range(len(locname)):
            loclist.append(locname[i])
    setloc = set(loclist)
    listloc = list(setloc)

    for i in range(len(t)):
        match = []
        for loc in listloc:
            match.append(GED(loc,t[i]))
        #print(match)
        bestmatch = max(match)
        print(bestmatch)
        for loc in listloc:
            if GED(loc,t[i])== bestmatch and bestmatch != len(loc):
                print(loc)
                print(t[i])
    

print("time: %s seconds." %(time.time() - starttime))
