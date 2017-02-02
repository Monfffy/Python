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
        if ch1.lower()==ch2.lower():
            return m
        if ch1.lower()!=ch2.lower():
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
    #print(A[len(f)][len(t)])
    length = min(len(f),len(t))
    matchRatio = A[len(f)][len(t)]/length
    return(matchRatio)

tweets = ""
t = ""
locnames = []

with open("train-tweets.txt","r",encoding = 'utf-8') as f1, open("loc-names.txt","r",encoding = 'utf-8') as f2:
    lines = f1.readlines()
    
    for line in lines:
        tweets = tweets+" "+line
    tweets = re.findall("[a-zA-Z]+(?:(?:\\s+|-)[a-zA-Z]+)*",tweets)
    #print(tweets)
    for tweet in tweets:
        t = t+" "+tweet
    t = t.split()

    for line in f2:
        line = line.strip()
        locnames.append(line)

        if(' ' in line):
            line = line.split()
            locnames.append(line[0])
            locnames.append(line[1])
            
    print(locnames)

    for i in range(len(t)):
        for loc in locnames:
            matchRatio = GED(loc,t[i])
            #print(matchRatio)
            if((matchRatio > 0.8) and (matchRatio != 1.0)):
                f = open("GED_ouput.txt","a",encoding = 'utf-8')
                f.write("%f\n" %matchRatio)
                print(matchRatio)
                f.write("'%s'\n" %t[i])
                print("'%s'" %t[i])
                f.write("%s\n" %loc )
                print(loc)

f.write("time: %s seconds." %(time.time() - starttime))                
print("time: %s seconds." %(time.time() - starttime))

f.close()
f1.close()
f2.close()
