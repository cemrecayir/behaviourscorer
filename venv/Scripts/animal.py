from pynput import keyboard
import time

class Animal:
    def __init__(self):
        self.leftTime = 0
        self.rightTime = 0
        self.timeFirst = 0
        self.isKeyPressed = False
    
    def printAnimal(self):
        print("The left key has been pressed for {0:.3f} seconds".format(self.leftTime))
        print("The right key has been pressed for {0:.3f} seconds".format(self.rightTime))

    def scoreAnimal(self):
        self.listen()

    def listen(self):
      with keyboard.Listener(on_press=self.keyPress, on_release=self.keyRelease) as listener:
        listener.join()

    def keyPress(self, key):
      if key == keyboard.Key.left or key == keyboard.Key.right:

          if not self.isKeyPressed:
              self.timefirst = time.time()
              self.isKeyPressed = True

    def keyRelease(self, key):
      if key == keyboard.Key.left or key == keyboard.Key.right:
          self.isKeyPressed = False
          duration_hold = time.time() - self.timefirst
          print(duration_hold)
          self.updateButtonTime(key, duration_hold)

      elif key == keyboard.Key.esc:
        return False

    def updateButtonTime(self, key, time):
      if key == keyboard.Key.left:
          self.leftTime += time
      elif key == keyboard.Key.right:
          self.rightTime += time