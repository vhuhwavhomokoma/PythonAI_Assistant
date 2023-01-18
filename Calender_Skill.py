#Calender feature for AI
#Author: Vhuwhavho Mokoma

from ics import Calendar, Event
from pathlib import Path
import os
import yaml
from datetime import datetime
from dateutil.relativedelta import *
import pytz
from yaml.loader import SafeLoader
import dateparser

calender_fn = 'myfile.ics'
calender_datafile = "myfile.yml"

class Calender_Skill():
   calender = Calendar()

   def __init__(self):
      """creates a banner to indicate begining of Calender Skill"""
      print("*"*10)
      print("Calender")
      print("*"*10)
   
   def add_event(self, begin:str, name:str, description:str):
      """Add event to the Calender"""
      event = Event()
      event.name = name
      event.begin = begin
      event.description = description
      try:
         self.calender.events.add(event)
         return True
      except:
         print("There was a problem adding the event, Sorry.")
         return False
   
   def remove_event(self, event_name:str):
      """Removes event from the calender"""
      for event in self.calender.events:
         if event.name == event_name:
            self.calender.events.remove(event)
            print("Removing event: "+event_name)
            return True
      
      print("Sorry could not find that event: "+event_name)
      return False
   
   def convert_to_dict(self):
      """Convert existing event information to a dict forom"""
      dict = []
      for event in self.calender.events:
         my_event = {}
         my_event['begin'] = event.begin.datetime
         my_event['name'] = event.name
         my_event['description'] = event.description
         dict.append(my_event)
      return dict
   
   def save(self):
      """Save calender ics file"""
      with open(calender_fn, 'w') as my_file:
         my_file.writelines(self.calender)
      
      if self.calender.events == set():
         print("No events - Removing YAML file")
         try:
            os.remove(calender_datafile)
         except:
            print("Couldn't delete the YAML file")
      
      else:
         with open(calender_datafile,'w') as outfile:
            yaml.dump(self.convert_to_dict(),outfile, default_flow_style=False)
      
   def load(self):
      """Load Calender data from yaml file"""
      filename = calender_datafile
      my_file = Path(filename)

      if my_file.is_file():
         stream = open(filename,'r')
         events_list = yaml.load(stream, Loader=SafeLoader)
         for item in events_list:
            event = Event()
            event.begin = item['begin']
            event.name = item['name']
            event.description = item['description']
            self.calender.events.add(event)
      else:
         print("File does not exist")
   
   def list_events(self,period:str=None):
      """List the upcoming events"""

      if period == None:
         period = "this week"

      if self.calender.events == set():
         print("No events in calender")
         return None
      else:
         event_list = []
         for event in self.calender.events:
            #event_date = event.begin.datetime
            event_list.append(event)
         return event_list

   def AI_add_event(self,Red):
         Red.say("What is the name of the event?")
         try:
               event_name = Red.listen()
               Red.say("When is this event?")
               event_begin = Red.listen()
               event_isodate = dateparser.parse(event_begin).strftime("%Y-%m-%d %H:%M:%S")
               Red.say("What is the event description?")
               event_description = Red.listen()
               message = "Ok, adding event " + event_name
               Red.say(message)
               self.add_event(begin=event_isodate, name=event_name, description=event_description)
               self.save()
               return True
         except:
               print("opps there was an error")
               return False

   def AI_remove_event(self,Red):
         Red.say("What is the name of the event you want me to remove?")
         try:
               event_name = Red.listen()
               try:
                  self.remove_event(event_name=event_name)
                  Red.say("Event removed successfully")
                  self.save()
                  return True
               except:
                  Red.say("Sorry I could not find the event",event_name)
                  return False
         except:
               print("opps there was an error")
               return False

   def Ai_list_events(self, Red)->bool:
         this_period = self.list_events(period="this month")
         if this_period is not None:
               message = "There "
               if len(this_period) > 1:
                  message = message + 'are '
               else:
                  message = message + 'is '
               message = message + str(len(this_period)) 
               if len(this_period) > 1:
                  message = message + ' events'
               else:
                  message = message + ' event'
               message = message + " in the diary"
               # print(message)
               Red.say(message)
               for event in this_period:
                  event_date = event.begin.datetime
                  weekday = datetime.strftime(event_date, "%A")
                  day = str(event.begin.datetime.day)
                  month = datetime.strftime(event_date, "%B")
                  year = datetime.strftime(event_date, "%Y")
                  time = datetime.strftime(event_date, "%I:%M %p")
                  name = event.name
                  description = event.description
                  message = "On " + weekday + " " + day + " of " + month + " " + year + " at " + time    
                  message = message + ", there is an event called " + name
                  message = message + " with an event description of " + description
                  # print(message)
                  Red.say(message)