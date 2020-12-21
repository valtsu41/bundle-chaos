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
	for linenum, line in enumerate(input):
		splitline = line.split(" = ")
		if len(splitline) > 1:
			try:
				inputstring += splitline[1]
			except IndexError:
				print("Bundle syntax error in file " + filename + " at line " + str(linenum + 1))
				sys.exit()

	marko = markovify.NewlineText(inputstring, well_formed=False, state_size=2)
	input.seek(0)

	lineamount = sum(1 for line in input)
	input.seek(0)

	for linenum, line in enumerate(input):
		print("Generating: " + filename + " (" + str(linenum + 1) + "/" + str(lineamount) + ")", end="\r")
		splitline = line.split(" ")
		linelength = len(splitline) - 2
		if linelength < 1:
			continue

		chainoutput = marko.make_sentence(tries=10000, min_words=round(linelength * 0.75), max_words=round(linelength * 1.5), test_output=False)
		if chainoutput == None:
			chainoutput = "".join(splitline[0]) + " = " + "oh no"
		output.write(splitline[0] + " = " + chainoutput + "\n")

	print("Generating: " + filename + " (COMPLETED)", end="\n")
	input.close()
	output.close()

print("Finished generating bundles")
