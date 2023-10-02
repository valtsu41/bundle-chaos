# Used for generating the randomised bundle.

import markovify
import os, sys

try:
	bundledir = os.listdir("./Mindustry/core/assets/bundles")
except FileNotFoundError:
	print("Could not locate Mindustry bundles at 'Mindustry/core/assets/bundles'")
	sys.exit()


for filename in bundledir:
	input = open("./Mindustry/core/assets/bundles/" + filename, "r")
	try:
		output = open("./bundles/" + filename, "w")
	except FileNotFoundError:
		print("Could not find 'bundles' directory for output")
		sys.exit()
	input.seek(0)

	parsedinput = []
	parsedinput_f = []
	for linenum, line in enumerate(input):
		splitline = line.split(" = ")
		if len(splitline) < 2:
			continue
		try:
			if "{" in splitline[1]:
				parsedinput_f.append(splitline[1].split())
			else:
				parsedinput.append(splitline[1].split())
		except IndexError:
			print(f"Bundle syntax error in file {filename} at line {linenum + 1}")
			sys.exit()
	marko = markovify.Text(None, parsed_sentences=parsedinput, well_formed=False, state_size=2).compile()
	marko_f = markovify.Text(None, parsed_sentences=parsedinput_f, well_formed=False, state_size=2).compile()
	input.seek(0)

	lineamount = sum(1 for line in input)
	input.seek(0)

	oopsies = 0
	for linenum, line in enumerate(input):
		print(f"Generating: {filename} ({linenum + 1}/{lineamount}) ({oopsies} failed)", end="\r")
		splitline = line.split(" ")
		linelength = len(splitline) - 2
		if linelength < 1:
			continue
		
		mark = marko_f if "{" in line else marko
		if linelength > 2:
			chainoutput = mark.make_sentence(tries=10000, min_words=round(linelength * 0.5), max_words=round(linelength * 1.75))
		else:
			chainoutput = mark.make_sentence(tries=10000, max_words=round(linelength * 1.75), test_output=False)

		if chainoutput == None:
			oopsies += 1
			chainoutput = "".join(splitline[0]) + " = " + "oh no"
			
		output.write(f"{splitline[0]} = {chainoutput}\n")

	print(f"Generating: {filename} (COMPLETED)", end="\n")
	input.close()
	output.close()

print("Finished generating bundles")
