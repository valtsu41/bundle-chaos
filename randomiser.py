#Used for generating the randomised bundle.

import markovify
import os, sys

try:
	bundlepath = os.listdir("./Mindustry/core/assets/bundles")
except FileNotFoundError:
	print("Could not locate Mindustry bundles at 'Mindustry/core/assets/bundles'")
	sys.exit()

for filename in bundlepath:
	print("Generating: " + filename)

	input = open("./Mindustry/core/assets/bundles/" + filename, "r")
	try:
		output = open("./bundles/" + filename, "w")
	except FileNotFoundError:
		print("Could not find 'bundles' directory for output")
		sys.exit()
	
	inputstring = input.read()
	marko = markovify.NewlineText(inputstring, well_formed=False, state_size=2)
	
	input.seek(0)
	
	for line in input:
		splitline = line.split(" ")
		if splitline[0] == "\n":
			output.write("\n")
		else:
			try:
				chainoutput = marko.make_sentence(tries=100, max_words=(len(splitline) - 2), test_output=False)
				print(len(splitline) - 2)
				if chainoutput == None:
					raise KeyError
			except KeyError:
				chainoutput = "".join(splitline[0]) + " = " + "oh no"
			output.write(chainoutput + "\n")
		
	input.close()
	output.close()

print("Finished generating bundles")