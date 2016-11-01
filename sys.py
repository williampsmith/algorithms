}import os, sys

# popen function calls a sys call and ports output to a program accessible text file
# we can then read from the file with the read() function
os.system("cd ~/Desktop/algorithms/")
a = os.popen("ls -l .").read()

print(a)

for num, line in enumerate(a.split('\n')):
	print('line number ', num, 'is :', line)

a = os.popen("cd ~/Desktop/; ls -l .").read()

print("\nDesktop contents: \n\n", a)