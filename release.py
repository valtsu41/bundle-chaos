#Used for releases, do not try at home.

import os, sys
import json

version = sys.argv[1]

modfile = open("mod.json", "r+")
moddata = json.load(modfile)
modfile.close()

moddata["version"] = float(version)

modfile = open("mod.json", "w")
json.dump(moddata, modfile, indent="\t")
modfile.close()

os.system("git add mod.json bundles && git commit -m \"Release " + version + "\"")
os.system("git tag -a " + version)
print("New release '" + str(version) + "' created")
