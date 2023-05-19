# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:48:18 2023

@author: willk
"""

#asdk;fasdfjasdf

import requests
from bs4 import BeautifulSoup
import time
#from playsound import playsound

class Race:
    isMedical = ""
    
    def __init__(self, myDate, myTime, myLocation, myMeta, myTitle, myRaceName, myJobDesc):
        self.date = myDate
        self.time = myTime
        self.location = myLocation
        self.meta = myMeta
        self.title = myTitle
        self.raceName = myRaceName
        self.jobDesc = myJobDesc
        
    def printDetails(self):
        print("DATE: ",self.date)
        print("TIME: ",self.time)
        print("LOCATION: ",self.location)
        print("META: ",self.meta)
        print("TITLE: ",self.title)
        print("RACENAME: ",self.raceName)
        print("JOBDESC: ",self.jobDesc)
        print("ISMEDICAL: ",self.isMedical)
        print()
        
    def printTest(self):
        print("DATE: ",self.date)
        print("RACENAME: ",self.raceName)
        print("TITLE: ",self.title)
        print("ISMEDICAL: ",self.isMedical)
        print()
        
    def checkMedical(self):
        medTerms = ["Medical","medical","Practitioner","practitioner","Physician","physician"] #,"Physician","physician"
        if any(word in self.title for word in medTerms) \
            or any(word in self.jobDesc for word in medTerms):
            self.isMedical = "Yes"
        else:
            self.isMedical = "No"
            
    def printNonMed(self):
        if self.isMedical == "No":
            self.printDetails()

def webToSoup():
    url = 'https://www.nyrr.org/getinvolved/volunteer/opportunities?available_only=true&itemId=3EB6F0CC-0D76-4BAF-A894-E2AB244CEB44&limit=40&offset=40&opportunity_type=9%2B1%20Qualifier&totalItemLoaded=8'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    return text

def cleanSoup(mySoup):
    
    output = ""
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
        ]
    
    for t in mySoup:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    
    startIndex = output.index('start race_detail/role_listing')
    endIndex = output.index('start footer')
    myOutput = output[startIndex:endIndex]
    
    return myOutput

def parseText(myText):
    globalCount = 1
    localCount = 1
    ignoreLines = ["start race_detail/role_listing","Apply","end btn", "start btn","Cancel"]
    raceList = []
    myRaces = []
    
    for line in myText.splitlines():
        if globalCount == 100:
            break
        myLine = line.strip()
        if myLine in ignoreLines:
            continue
        
        if len(myLine) > 1:
            if localCount == 1:
                raceList.append(myLine)
            elif localCount == 2:
                raceList.append(myLine)
            elif localCount == 3:
                raceList.append(myLine)
            elif localCount == 4:
                raceList.append(myLine)
            elif localCount == 5:
                raceList.append(myLine)
            elif localCount == 6:
                raceList.append(myLine)
            elif localCount == 7:
                raceList.append(myLine)
            else:
                raceList[6] = raceList[6] + " " + myLine
            
            localCount = localCount + 1
            globalCount = globalCount + 1
        

        if myLine == "9+1":
            localCount = 1
        
            myRace = Race(raceList[0],raceList[1],raceList[2],raceList[3],raceList[4],raceList[5],raceList[6])
            myRace.checkMedical()
            
            myRaces.append(myRace)
            raceList.clear()
            
    return myRaces

temp = 1
check = False
mySleep = 55 #seconds
maxRuns = 60

#playsound('C:/Users/willk/OneDrive/Desktop/nyrr volunteer tracker/strong-minded-ringtone.mp3')

print("Running", maxRuns, "times. Checking every", mySleep, "seconds.")

while temp <= maxRuns:
    
    t = time.localtime()
    current_time = time.strftime("%I:%M %p", t)
    
    print("[" + current_time + "] (" + str(temp) + ")", "Checking for nyrr volunteer opportunities...")
    
    webSoup = webToSoup()
    cleanText = cleanSoup(webSoup)
    nyrrRaces = parseText(cleanText)
    
    
    for item in nyrrRaces:
        if item.isMedical == "No":
            check = True
    
    if check:
        for item in nyrrRaces:
            item.printNonMed()
        #playsound('C:/Users/willk/OneDrive/Desktop/nyrr volunteer tracker/strong-minded-ringtone.mp3')
    else:
        print("No opportunities found - checking again in a min")
    
    time.sleep(mySleep)
    check = False
    temp = temp + 1
