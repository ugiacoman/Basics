import string
import sys,os



def readTAList(filename):
        list = { }
        for line in open(filename, "r"):
                line = line.strip( )
                word = line.split( )
                if len(word) != 2:
                        print ("Error:", line)
                        continue
                list[word[0]] = word[1]
        return list

def  setForward(email):
    if len(email) == 0: return
    if email.find("@") == -1: return
    if email.find("@cs.wm.edu") != -1: return
    os.system("echo '%s' > ~/.forward"%(email))
    return

def save(values):
    global ta, tabin, prof, profbin
    fname = os.environ['HOME'] + "/.cs141"
    # print "fname =", fname
    fh = open(fname, "w")
    for k in values.keys():
        if k == "" or k == "email": continue
        fh.write("%s %s\n" % (k, values[k]))
    fh.close()
    
def readChk(prompt, legalSet):
    while 1:
        val = input(prompt)
        if val != "" and val in legalSet: return val
        print (val, "illegal, please re-enter.")
    return 1

def readNonEmpty(label):
    while 1:
        val = input(label)
        if val != "": return val
        print ("Value required, please re-enter")
    return 1

def prompt(keylist):
    global prof, ta, label
    values = { }
    val = ""
    for k in keylist:
        if k == "": continue
        if k == "email":
            val = input(label[k])
            setForward(val)
        elif k == "first" or k == "last":
            val = readNonEmpty(label[k])
            values[k] = val
        else:
            val = readChk(label[k], legalkeys[k])
            values[k] = val
    values["prof"] = prof[values["lecture"]]
    values["ta"] = ta[values["lab"]]
    values["profbin"] = profbin[values["lecture"]]
    values["tabin"] = tabin[values["lab"]]
    save(values)
    return


label = {"first": "First Name: ",
        "last": "Last Name: ",
        "email": "Forward CS Email to: ",
        "lecture": "Lecture Section (1,2,...): ",
        "lab": "Lab Section (1,2,...): "}
entry = {"first": "",
        "last":  "",
        "email": "",
        "lecture":  "",
        "lab": ""}
keylist = ["","first", "last", "email", "lecture", "lab"]
prof = {"1":"debbie", "2":"debbie"}
#This ta list is read from debbie folder
ta = readTAList("/home/f85/debbie/.talabs")
#ta = {"1": "kdm", "2":"kdm", "3":"bdit", 
#      "4":"bdong", "5":"ejnovak", "6":"hrs"}
tabin = {"1":"bin/submit", "2":"bin/submit", "3":"bin/submit", 
         "4":"bin/submit", "5":"bin/submit", "6":"bin/submit", "7":"bin/submit", "8":"bin/submit"}
profbin = {"1":"bin/submit", "2":"bin/submit" }
profkeys = set(prof.keys())
takeys = set(ta.keys())
legalkeys = {"lecture": profkeys, "lab": takeys}
profno = -1
tano = -1

prompt(keylist)
