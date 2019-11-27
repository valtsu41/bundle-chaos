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

os.system("git tag -a " + version)
print("New build '" + str(version) + "' created")