import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0// Created by Tamal")
    x = input("tell me what you want me to speak: ")
    command = f"say {x}"
    os.system(command)