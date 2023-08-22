import os

def routeOfString (path, string):
	for f in os.listdir(path):
		name, ext = os.path.splitext(f)
		if ext == '.txt':
			if open(rf'{path}/{f}',"r").read().find(string) >= 0:
				print(f'{string} found in \n {os.path.abspath(f)}')

path = input('path: ')
text = input('input text: ')

routeOfString(path, text)