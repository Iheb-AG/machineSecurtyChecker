# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZeGzYiNJPs_5qU5Qi5X2LtqROxyi6Gy

#Documentation

The user interacts with the expert system to determine the hazards that can affect their machine by answering a series of questions:

 - Validation of the entered password
 - Is the machine up to date?
 - Is an antivirus installed?
 - Is the firewall activated?
 - Has there been any interaction with an unknown website/program?

Regarding the obtained results:

 - The system informs the user about the identified risks.
 - The system also provides information about the security of their machine.

# pip installs
"""
# use those commands in your command prompt/terminal to install dependencies

# !pip install experta
# !pip install --upgrade frozendict
# # !pip install re

"""# implementation"""

from experta import *
import re
# import getpass

choices={"yes":True,"no":False}
threatTrigger = False

class Threats(Fact):
    pass

class ThreatClassification(KnowledgeEngine):
    @Rule(Threats(threats={"user_password":None}))
    def weakPassword(self):
      print("Your password is weak. Make sure to include a combination of alphabets, numbers, and symbols and have a length of at least 8.")
      # threatTrigger=True

    @Rule(Threats(threats={"outdated_software":True}))
    def outdatedSoftware(self):
        print("Your system is not updated. A vulnerability can be exploited to hack your system.")
        # threatTrigger=True

    @Rule(Threats(threats={"antivirus_installed":False}))
    def noAntivirus(self):
        print("Your system does not have antivirus. A virus can harm your system.")
        # threatTrigger=True

    @Rule(Threats(threats={"firewall_enabled":False}))
    def noFirewall(self):
        print("Your system does not have firewall. Unauthorized access may occur.")
        # threatTrigger=True

    @Rule(Threats(threats={"sus_link":True}))
    def susLink(self):
        print("You've probably interacted with a suspicious link.")
        # threatTrigger=True


engine = ThreatClassification()
engine.reset()


user_password = input("test your password : ")
engine.declare(Threats(threats={"user_password":re.match(r"[A-Za-z0-9]{8,}",user_password)}))
engine.declare(Threats(threats={"outdated_software":choices[input("do You postpone your update for too long ?")]}))
engine.declare(Threats(threats={"antivirus_installed":choices[input("do you have antivirus on your system ? ")]}))
engine.declare(Threats(threats={"firewall_enabled":choices[input("do you have firewall enabled ?")]}))
engine.declare(Threats(threats={"sus_link":choices[input("have you downloaded from / interacted with suspicious website/software ? ")]}))

# if(threatTrigger==True):
#   print("Your system is all safe !")

engine.run()
