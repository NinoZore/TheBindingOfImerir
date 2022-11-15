# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:29:30 2022

@author: Nino
"""
###################################################################################
def Config_Data():
    global Resolution
    global Fps
    global FullScreen
    global Player_Key_Forward
    global Player_Key_Backward 
    global Player_Key_Left 
    global Player_Key_Right 

    with open("C:/Users/Nino/Documents/binding of imerir/TheBindingOfImerir/config.txt",'r+') as fichier_config:
        for line in fichier_config:

            Config = line[0:line.find(':')]
            removeequal = line[line.find(':'):]
            Value = removeequal[1:]

            if(Config == "Resolution"):
                Resolution = Value
            if(Config == "Fps"):
                Fps = Value
            if(Config == "FullScreen"):
                FullScreen = Value
            if(Config == "Player_Key_Forward"):
                Player_Key_Forward = Value
            if(Config == "Player_Key_Backward"):
                Player_Key_Backward = Value
            if(Config == "Player_Key_Left"):
                Player_Key_Left = Value
            if(Config == "Player_Key_Right"):
                Player_Key_Right = Value
    fichier_config.close()
###################################################################################
Config_Data()
print(Resolution)
print(Fps)
print(FullScreen)
print(Player_Key_Forward)
print(Player_Key_Backward)
print(Player_Key_Left)
print(Player_Key_Right)