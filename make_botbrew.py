# Make the goals separately
# Just a simple python script to make pkg and print the logs if it fails

from sys import argv
from os import system

fail, success = 0, 0

goals = argv[1:]

for goal in goals:
	print "Making %s..." % goal
	make = system("make %s 2> build.log" % goal)
	if make != 0: # Fail ?
		print "%s failed" % goal
		system("cat build.log") # Show the logs
		fail += 1
	else:
		success += 1

print "Failed: %s" % str(fail)
print "Succesfull: %s" % str(success)
print "Total: %s" % str(len(goals))
