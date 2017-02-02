import csv
attrname = []
attrname.append('ttid')
attrname.append('userid')
attrname.append('bellevue')
attrname.append('bill')
attrname.append('boston')
attrname.append('ca')
attrname.append('care')
attrname.append('charges')
attrname.append('cheezburger')
attrname.append('dc')
attrname.append('diego')
attrname.append('ebay')
attrname.append('health')
attrname.append('houston')
attrname.append('httpbitlycdqk')
attrname.append('httpbitlycjf')
attrname.append('httpbitlycamk')
attrname.append('jupdicom')
attrname.append('lol')
attrname.append('ma')
attrname.append('obama')
attrname.append('patriots')
attrname.append('redsox')
attrname.append('san')
attrname.append('san diego')
attrname.append('scans')
attrname.append('sd')
attrname.append('sdut')
attrname.append('seahawks')
attrname.append('seattle')
attrname.append('sox')
attrname.append('tcot')
attrname.append('texas')
attrname.append('tx')
attrname.append('uw')
attrname.append('wa')
attrname.append('washington')
attrname.append('houstoinan')
attrname.append('san dieg')
attrname.append('sun diego')
attrname.append('san dieago')
attrname.append('settl')
attrname.append('seatle')
attrname.append('washingston')
attrname.append('washingtion')
attrname.append('washingtondc')
attrname.append('location')

print(attrname)

with open("test-tweets.txt","r",encoding = 'utf-8') as f, open ('test-addapprox44-uid.csv','w',newline='') as csvfile:
    fieldnames = [attrname[0],attrname[1],attrname[2],attrname[3],
                  attrname[4],attrname[5],attrname[6],attrname[7],
                  attrname[8],attrname[9],attrname[10],attrname[11],
                  attrname[12],attrname[13],attrname[14],attrname[15],
                  attrname[16],attrname[17],attrname[18],attrname[19],
                  attrname[20],attrname[21],attrname[22],attrname[23],
                  attrname[24],attrname[25],attrname[26],attrname[27],
                  attrname[28],attrname[29],attrname[30],attrname[31],
                  attrname[32],attrname[33],attrname[34],attrname[35],
                  attrname[36],attrname[37],attrname[38],attrname[39],
                  attrname[40],attrname[41],attrname[42],attrname[43],
                  attrname[44],attrname[45],attrname[46]]
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
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,
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
                         attrname[19]:attrval[19],
                         attrname[20]:attrval[20],
                         attrname[21]:attrval[21],
                         attrname[22]:attrval[22],
                         attrname[23]:attrval[23],
                         attrname[24]:attrval[24],
                         attrname[25]:attrval[25],
                         attrname[26]:attrval[26],
                         attrname[27]:attrval[27],
                         attrname[28]:attrval[28],
                         attrname[29]:attrval[29],
                         attrname[30]:attrval[30],
                         attrname[31]:attrval[31],
                         attrname[32]:attrval[32],
                         attrname[33]:attrval[33],
                         attrname[34]:attrval[34],
                         attrname[35]:attrval[35],
                         attrname[36]:attrval[36],
                         attrname[37]:attrval[37],
                         attrname[38]:attrval[38],
                         attrname[39]:attrval[39],
                         attrname[40]:attrval[40],
                         attrname[41]:attrval[41],
                         attrname[42]:attrval[42],
                         attrname[43]:attrval[43],
                         attrname[44]:attrval[44],
                         attrname[45]:attrval[45],
                         attrname[46]:loc})
f.close()
csvfile.close()
print('End')    
