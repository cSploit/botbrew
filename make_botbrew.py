# Make the goals separately
# Just a simple python script to make pkg and print the logs if it fails

from sys import argv
from os import system

fail, success = 0, 0
disabled = [] # Put packages name you don't want to compile...

args = argv[1:]
goals = []

for arg in args:
	if ' ' in arg:
		goals.extend(arg.split(' '))
	else:
		goals.append(arg)

for goal in goals:
	if goal not in disabled:
		print "Making %s..." % goal
		make = system("make -s %s &> build.log" % goal)
		if make != 0: # Fail ?
			print "%s failed" % goal
			system("cat build.log") # Show the logs
			fail += 1
		else:
			success += 1

print "Failed: %s" % str(fail)
print "Succesfull: %s" % str(success)
print "Disabled: %s" % str(len(disabled))
print "Total: %s" % str(len(goals))
