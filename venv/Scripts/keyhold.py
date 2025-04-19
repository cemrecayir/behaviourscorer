from pynput import keyboard

isKeyNotPressed = True

def on_press(key):
  if key != keyboard.Key.esc:
      global isKeyNotPressed
      if isKeyNotPressed:
        print('Key pressed: {0} '.format(key))
        isKeyNotPressed = False

def on_release(key):
  if key == keyboard.Key.esc:
    return False
  global isKeyNotPressed
  isKeyNotPressed = True
  print('Key released: {0}'.format(key))

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()