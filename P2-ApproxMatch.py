import csv
attrname = []
attrname.append('ttid')
attrname.append('userid')
attrname.append('boston')
attrname.append('houston')
attrname.append('houstoinan')
attrname.append('san diego')
attrname.append('san')
attrname.append('diego')
attrname.append('san dieg')
attrname.append('sun diego')
attrname.append('san dieago')
attrname.append('seattle')
attrname.append('seattl')
attrname.append('seatle')
attrname.append('washington dc')
attrname.append('washington')
attrname.append('dc')
attrname.append('washingston')
attrname.append('washingtion')
attrname.append('location')

print(attrname)

with open("dev-tweets.txt","r",encoding = 'utf-8') as f, open ('dev-approx17-uid.csv','w',newline='') as csvfile:
    fieldnames = [attrname[0],attrname[1],attrname[2],attrname[3],attrname[4],
                  attrname[5],attrname[6],attrname[7],attrname[8],attrname[9],
                  attrname[10],attrname[11],attrname[12],attrname[13],attrname[14],
                  attrname[15],attrname[16],attrname[17],attrname[18],attrname[19]]
    writer = csv.DictWriter(csvfile,fieldnames = fieldnames)

    writer.writeheader()
    for line in f:
        line = line.lower()
        line = line.split()
        ttid = line[1]
        userid = line[0]
        loc = line[len(line)-1].upper()
        line = ' '.join([word for word in line if not word.isdigit()])

        attrval = [ttid,userid,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   loc]
        for i in range(2,len(attrval)-1):
            tf = line.count(attrname[i])
            if (tf != 0):
                attrval[i] = tf
                #attrval[i] = 1
                
        writer.writerow({attrname[0]:ttid,
                         attrname[1]:userid,
                         attrname[2]:attrval[2],
                         attrname[3]:attrval[3],
                         attrname[4]:attrval[4],
                         attrname[5]:attrval[5],
                         attrname[6]:attrval[6],
                         attrname[7]:attrval[7],
                         attrname[8]:attrval[8],
                         attrname[9]:attrval[9],
                         attrname[10]:attrval[10],
                         attrname[11]:attrval[11],
                         attrname[12]:attrval[12],
                         attrname[13]:attrval[13],
                         attrname[14]:attrval[14],
                         attrname[15]:attrval[15],
                         attrname[16]:attrval[16],
                         attrname[17]:attrval[17],
                         attrname[18]:attrval[18],
                         attrname[19]:loc})
f.close()
csvfile.close()
print('End')    
