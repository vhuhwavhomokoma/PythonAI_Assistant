#AI assistant RED
#Author: Vhuhwavho Mokoma

import pyjokes
from ai import AI
import torchvision
from PIL import Image
#import digitNN
from Calender_Skill import Calender_Skill
from Weather import Weather
import dateparser
from datetime import datetime




def joke():
    funnyjoke = pyjokes.get_joke()
    print(funnyjoke)
    Red.say(funnyjoke)

def DigitAnalysis():
    transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),torchvision.transforms.Normalize((0.1204,),(0.4012,))])
    filepath = "img_43.jpg"
    image = Image.open(filepath)
    image_tensor = transform(image)
    output = 0 #digitNN.model(image_tensor)
    digit = output.argmax(1).item()
    return digit





# Main AI method
#digit_neuralnetwork = digitNN.DigitNeuralNetwork()
Red = AI()
weather = Weather()
calender = Calender_Skill()
calender.load()
Red.say("Analysis complete")

command = ""
while (True):
    command = Red.listen()
    print("Command was "+ command)
    if(command=="goodbye"):
        break

    if(command=="result"):
        anaylsis = "The number is "+str(DigitAnalysis())
        print(DigitAnalysis())
        Red.say(anaylsis)
    if(command=="what am I studying"):
        Red.say("Bsc Computer Science and Computer Engineering")
    if(command=="tell me a joke"):
        joke()
    if(command=="remove event"):
        calender.AI_remove_event(Red)
    if(command=="add event"):
        calender.AI_add_event(Red)
    if(command=="list"):
        calender.Ai_list_events(Red)
    if(command in ["tell me the weather","what's the weather like"]):
        Red.say(weather.forecast())

Red.say("Goodbye, shutting down")
