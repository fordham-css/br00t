import time
import os
import json
print('Welcome to your journal!')
print('Please select an option:')
print('1: Write new entry from command line')
print('2: Upload contents of upload.txt')
option = input()
print('Initiating option ' + str(option) + '...')
timestamp = time.strftime("%Y-%m-%d at %H-%M-%S", time.localtime())
reading = open("journal" + ".txt", 'r')
save = reading.read()
reading.close()
if option == 1:
	f = open("journal" + ".txt", 'w')
	value = raw_input('Please begin writing:')
	f.write(save + timestamp + '\n' + value)
	f.write('\n\n')
elif option == 2:
	reading_upload = open("upload.txt",'r')
	value = reading_upload.read()
	reading_upload.close()
	f = open("journal" + ".txt", 'w')
	f.write(save + timestamp + '\n' + value)
	f.write('\n\n')
print('Entry added!')