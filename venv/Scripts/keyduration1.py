from pynput import keyboard
import time

isKeyNotPressed = True
timefirst = time.time()

def on_press(key):
  global timefirst
  if key != keyboard.Key.esc:
      global isKeyNotPressed
      if isKeyNotPressed:
        timefirst = time.time()
        print('Key pressed: {0} '.format(key))
        isKeyNotPressed = False
  

def on_release(key):
  global timefirst
  if key == keyboard.Key.esc:
    return False
  global isKeyNotPressed
  isKeyNotPressed = True
  duration_hold = time.time() - timefirst
  print("The key is pressed for",duration_hold,'seconds')



with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()