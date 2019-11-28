#Used for generating the randomised bundle.

import markovify
import os, sys

try:
	bundlepath = os.listdir("./Mindustry/core/assets/bundles")
except FileNotFoundError:
	print("Could not locate Mindustry bundles at 'Mindustry/core/assets/bundles'")
	sys.exit()


for filename in bundlepath:

	input = open("./Mindustry/core/assets/bundles/" + filename, "r")
	try:
		output = open("./bundles/" + filename, "w")
	except FileNotFoundError:
		print("Could not find 'bundles' directory for output")
		sys.exit()
	input.seek(0)
	
	inputstring = ""
	for line in input:
		splitline = line.split(" = ")
		if splitline[0] != "\n":
			try:
				inputstring += splitline[1]
			except IndexError:
				print("Invalid bundle file format")
				sys.exit()
		
	marko = markovify.NewlineText(inputstring, well_formed=False, state_size=2)
	input.seek(0)
	
	lineamount = sum(1 for line in input)
	input.seek(0)
	
	for linenum, line in enumerate(input):
		print("Generating: " + filename + " (" + str(linenum) + "/" + str(lineamount) + ")", end="\r")
		splitline = line.split(" ")
		try:
			chainoutput = marko.make_sentence(tries=10000, max_words=(len(splitline) - 2), test_output=False)
			if chainoutput == None:
				raise KeyError
		except KeyError:
			chainoutput = "".join(splitline[0]) + " = " + "oh no"
		output.write(splitline[0] + "=" + chainoutput + "\n")
		if len(splitline) - 2 == 0:
			print("EORKRBWNENEKDLELELEKEKEkdkekennebebeK")
			sys.exit()
	
	print("Generating: " + filename + " (COMPLETED)", end="\n")
	input.close()
	output.close()

print("Finished generating bundles")