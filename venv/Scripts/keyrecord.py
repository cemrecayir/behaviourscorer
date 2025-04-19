from pynput import keyboard
import time

print("\n ===== NOR object exploration timer =====")
print("\n Press right arrow key for right object and left arrow key for left object")
print("\n Pess esc key to see the sum \n")

isKeyPressed = False
timefirst = 0
keyTimeList = []
shouldContinue = True

def printMenu():
  print("\n ---MENU OPTIONS---")
  print("\n [a] Score an animal")
  print("\n [b] Show last scores")
  print("\n [c] Export as .csv")
  print("\n [d] Exit program \n")

def renameKey(key):
  if key == keyboard.Key.left:
    key = "Left key"
  elif key == keyboard.Key.right:
    key = "Right key"
  return key


def keyPress(key):
  global timefirst

  if key != keyboard.Key.esc and key != keyboard.Key.enter:
    global isKeyPressed

    if not isKeyPressed:
      print(renameKey(key), "is pressed...")
      timefirst = time.time()
      isKeyPressed = True
  

def keyRelease(key):
  global timefirst

  if key == keyboard.Key.esc:
    print("\n ======= TOTAL ======= \n")
    for keyTime in keyTimeList:
      print("{0} is pressed for a total of {1:.4f} seconds".format(renameKey(keyTime[0]), keyTime[1]))
    return False
  elif key != keyboard.Key.enter:
    
    keyExists = any(key in keyTime for keyTime in keyTimeList)


    if not keyExists:
    #if key not in keyTimeList:
      keyTimeList.append([key,0]) #you can start lists with the amount of elements you know you will need

    global isKeyPressed
    isKeyPressed = False
    duration_hold = time.time() - timefirst
    print(renameKey(key), "is pressed for {0:.4f} seconds".format(duration_hold))

    for keyTime in keyTimeList:
      if keyTime[0] == key:
        keyTime[1] += duration_hold

# begin main script
def mainScript():
  with keyboard.Listener(on_press=keyPress, on_release=keyRelease) as listener:
    listener.join()
# end main script

while shouldContinue:
  printMenu()
  menuSelection = input("Press the letter corresponding to the desired action: ")
  if menuSelection == "a":
    print("\n You can start scoring the animals \n")
    mainScript()
  shouldContinue = False
