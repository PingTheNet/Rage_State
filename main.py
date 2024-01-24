import os

rage = "┻━┻" # ╯°□°)╯︵┻━┻
unrage = current_state = "┳━┳" # ┳━┳ノ( º _ ºノ)
is_running = True
invalid_input = False
history = []

while is_running:
  os.system("clear")
  print(f"Number States on record: {len(history)}")
  print(f"Rage states of the past: {history}\n")
  if invalid_input:
    print("Invalid choice. Please enter 'rage' 'unrage' or 'exit'.")
    invalid_input = False
  print(f"\nCurrent state: {current_state}")
  user = input("What is your state of rage? Please enter 'rage' 'unrage' or 'exit': ")
  if user.lower() == "rage":
      current_state = rage
  elif user.lower() == "unrage":
      current_state = unrage
  elif user.lower() == "exit":
      print(f"\nCurrent state: {unrage}\n")
      print("We've made sure the table back in the correct state so it's ready for the next time!")
      is_running = False
  else:
      invalid_input = True
  if not invalid_input:
    history.append(current_state)
