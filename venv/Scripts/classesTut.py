from pynput import keyboard
import time
import csv
import animal

isKeyPressed = False
timefirst = 0
shouldContinue = True
animalList = []

    
def printMenu():
  print("\n\n---MENU OPTIONS---")
  print("\n[a] Score an animal")
  print("\n[b] Show last scores")
  print("\n[c] Export as .csv")
  print("\n[d] Exit program \n")

def keyPress(key):
    if key == keyboard.Key.left or key == keyboard.Key.right:
        global timefirst
        global isKeyPressed

        if not isKeyPressed:
            timefirst = time.time()
            isKeyPressed = True


def keyRelease(key):
    if key == keyboard.Key.left or key == keyboard.Key.right:
        global isKeyPressed
        global timefirst
        isKeyPressed = False
        duration_hold = time.time() - timefirst
        print(duration_hold)
        updateButtonTime(key, duration_hold)

    elif key == keyboard.Key.esc:
        wannaCont = input("Do you want to shocre another animal? [y]")
        if wannaCont != "y":
           return False
        else:
           scoreNewAnimal()


def updateButtonTime(key, time):
    global animalList
    if key == keyboard.Key.left:
        animalList[len(animalList)-1].leftTime += time
    elif key == keyboard.Key.right:
        animalList[len(animalList)-1].rightTime += time

def scoreNewAnimal():
   global animalList
   animalList.append(a.Animal())

def scoreList():
   for animal in animalList:
      animal.printAnimal()
   


def listen():
  scoreNewAnimal()
  with keyboard.Listener(on_press=keyPress, on_release=keyRelease) as listener:
    listener.join()

def menu():
    printMenu()
    menuSelection = input("Press the letter corresponding to the desired action: ")
    match menuSelection:
        case "a":
          listen()
        case "b":
          print("\n\n=== Showing the scores ===")
          scoreList()
        case "c":
          fileName = input('Enter the file name to be saved:')
        case "d":
          global shouldContinue
          print("\nTerminating the program")
          shouldContinue = False

def mainScript():
    global shouldContinue

    while shouldContinue:
      menu()


mainScript()

