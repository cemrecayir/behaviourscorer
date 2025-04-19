from pynput import keyboard
import csv
import animal

shouldContinue = True
animalList = []

    
def printMenu():
  print("\n\n---MENU OPTIONS---")
  print("\n[a] Score an animal")
  print("\n[b] Show last scores")
  print("\n[c] Export as .csv")
  print("\n[d] Exit program \n")

def scoreNewAnimal():
   global animalList
   anotherAnimal = True
   while anotherAnimal:
    newAnimal = animal.Animal()
    newAnimal.scoreAnimal()
    animalList.append(newAnimal)
    anotherAnimal = input("Do you want to score another animal? [y]") == "y"
      

def scoreList():
   for animal in animalList:
      animal.printAnimal()

def menu():
    printMenu()
    menuSelection = input("Press the letter corresponding to the desired action: ")
    match menuSelection:
        case "a":
          scoreNewAnimal()
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