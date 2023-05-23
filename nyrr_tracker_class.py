# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:23:12 2023

@author: willk
"""

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