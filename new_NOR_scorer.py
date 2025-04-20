from pynput import keyboard
import time
import pandas as pd
import csv

print("\n===== NOR Video Scorer =====")


is_key_pressed = False
timefirst = 0
individual_score = {}
score_list = []
should_continue = True

def print_menu():
  print("\n\n--- MENU OPTIONS ---")
  print("\n[a] Score an animal")
  print("\n[b] Show last scores")
  print("\n[c] Export as .csv")
  print("\n[d] Exit program \n")

def rename_key(key):
  if key == keyboard.Key.left:
    key = "Left key"
  elif key == keyboard.Key.right:
    key = "Right key"
  return key


def key_press(key):
  global timefirst

  if key == keyboard.Key.left or key == keyboard.Key.right:
    global is_key_pressed

    if not is_key_pressed:
      print(rename_key(key), "is pressed...")
      timefirst = time.time()
      is_key_pressed = True
  


def key_release(key):
  global timefirst

  if key == keyboard.Key.left or key == keyboard.Key.right:
    
    key_exists = any(rename_key(key) in key_time for key_time in individual_score)

    if not key_exists:
      individual_score[rename_key(key)] = 0

    global is_key_pressed
    is_key_pressed = False
    duration_hold = time.time() - timefirst
    print(f"{rename_key(key)}, is pressed for {duration_hold:.3f} seconds")

    for key_time in individual_score:
      if key_time == rename_key(key):
        individual_score[rename_key(key)] += round(duration_hold, 3)

  elif key == keyboard.Key.esc:
    score_list.append(individual_score)
    print(f"individual_score = {individual_score}")
    print(f"score_list = {score_list}")
    print("\n ======= TOTAL ======= \n")
    for key_time in individual_score:
      print(f"{key_time} is pressed for a total of {individual_score[key_time]:.3f} seconds")
    return False


def listener_cont_menu():
  with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()
    while True:
      next_video = input("\nPress [y] to score next animal, press [n] to return to the main menu: ")
      if next_video == "y":
        return True
      elif next_video == "n":
        print("\nReturning to the main menu")
        return False
      else:
        print("\nInvalid input, please try again")
        pass


# Main script
def start_scoring():
  global individual_score
  new_animal = True
  while new_animal:
    print("\nYou can start scoring the animals\n")
    individual_score = {}
    new_animal = listener_cont_menu()

def format_score_list():
  for individual_score in score_list:
    print(f"- Left object: {individual_score['Left key']} s, \t Right object: {individual_score['Right key']} s")


# Menu actions
while should_continue:
  print_menu()
  menu_selection = input("Press the letter corresponding to the desired action: ")
  match menu_selection:
    case "a":
      start_scoring()
    case "b":
      print("\n\n=== Showing the scores ===")
      format_score_list()
    case "c":
      # df = pd.DataFrame(score_list, columns = ["key1", "time1", "key2", "time2"])
      # print(df)
      titles = ["Position1", "Time1", "Position2", "Time2"]
      with open('NORscrs', 'w') as f: ######### File name user input - take from work laptop
        write = csv.writer(f)
        write.writerow(titles)
        write.writerows(score_list)
    case "d":
      print("\nTerminating the program")
      should_continue = False