import pynput.keyboard

def process_key(key):
   print(key)

keyboard_listener = pynput.keyboard.Listener(on_press = process_key)

with keyboard_listener:
  keyboard_listener.join()
