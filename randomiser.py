#Used for generating the randomised bundle.

import markovify
import os


for filename in os.listdir("./original"):
	print("Generating: " + filename)

	input = open("./original/" + filename, "r")
	output = open("./bundles/" + filename, "w")
	
	inputstring = input.read()
	marko = markovify.NewlineText(inputstring, well_formed=False, state_size=2)
	
	input.seek(0)
	
	for line in input:
		splitline = line.split(" ")
		if splitline[0] == "\n":
			output.write("\n")
		else:
			startstate = (splitline[0], "=")
			chainoutput = marko.make_sentence(tries=100, init_state=startstate, test_output=False)
			output.write(chainoutput + "\n")
		
	input.close()
	output.close()