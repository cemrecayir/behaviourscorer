from pynput import keyboard
import time
import pandas as pd
import csv

print("\n===== NOR object exploration timer =====")
# print("\nPress right arrow key for right object and left arrow key for left object")
# print("\nPess esc key to see the sum \n")

isKeyPressed = False
timefirst = 0
individualScore = []
scoreList = []
shouldContinue = True

def printMenu():
  print("\n\n---MENU OPTIONS---")
  print("\n[a] Score an animal")
  print("\n[b] Show last scores")
  print("\n[c] Export as .csv")
  print("\n[d] Exit program \n")

def renameKey(key):
  if key == keyboard.Key.left:
    key = "Left key"
  elif key == keyboard.Key.right:
    key = "Right key"
  return key


def keyPress(key):
  global timefirst

  if key == keyboard.Key.left or key == keyboard.Key.right:
    global isKeyPressed

    if not isKeyPressed:
      print(renameKey(key), "is pressed...")
      timefirst = time.time()
      isKeyPressed = True
  


def keyRelease(key):
  global timefirst

  if key == keyboard.Key.left or key == keyboard.Key.right:
    
    keyExists = any(renameKey(key) in keyTime for keyTime in individualScore)

    if not keyExists:
    #if key not in keyTimeList:
      individualScore.append([renameKey(key),0]) #you can start lists with the amount of elements you know you will need

    global isKeyPressed
    isKeyPressed = False
    duration_hold = time.time() - timefirst
    print(renameKey(key), "is pressed for {0:.3f} seconds".format(duration_hold))

    for keyTime in individualScore:
      if keyTime[0] == renameKey(key):
        keyTime[1] += round(duration_hold, 3)

  elif key == keyboard.Key.esc:
    flatList = [element for innerList in individualScore for element in innerList]
    scoreList.append(flatList)
    print("\n ======= TOTAL ======= \n")
    for keyTime in individualScore:
      print("{0} is pressed for a total of {1:.3f} seconds".format(keyTime[0], keyTime[1]))
    return False


def listenerContMenu():
  with keyboard.Listener(on_press=keyPress, on_release=keyRelease) as listener:
    listener.join()
  return input("\nPress [y] to score next animal, press [n] to return to the main menu: ") == "y"


# Main script
def mainScript():
  global individualScore
  newAnimal = True
  while newAnimal:
    print("\nYou can start scoring the animals\n")
    individualScore = []
    newAnimal = listenerContMenu()

def scoreListFormat():
  for individualScore in scoreList:
    print(*individualScore)
    #for keyTime in individualScore:
      #print("{0}: {1:.3f} seconds".format(renameKey(keyTime[0]), keyTime[1]), sep="")

    #print("\n{0}: {1:.4f} seconds, {2}: {3:.4f} seconds".format(renameKey(individualScore[0][0]), individualScore[0][1], renameKey(individualScore[1][0]), individualScore[1][1]))

# Menu actions
while shouldContinue:
  printMenu()
  menuSelection = input("Press the letter corresponding to the desired action: ")
  match menuSelection:
    case "a":
      mainScript()
    case "b":
      print("\n\n=== Showing the scores ===")
      scoreListFormat()
    case "c":
      # df = pd.DataFrame(scoreList, columns = ["key1", "time1", "key2", "time2"])
      # print(df)
      titles = ["Position1", "Time1", "Position2", "Time2"]
      with open('NORscrs', 'w') as f:
        write = csv.writer(f)
        write.writerow(titles)
        write.writerows(scoreList)
    case "d":
      print("\nTerminating the program")
      shouldContinue = False