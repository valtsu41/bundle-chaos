# Bundle chaos
## About
### The mod
This mod simply replaces all texts in the game to more random versions with markov chains. Most languages that use spaces should be supported.
### Versioning
The number before `.` indicates the algorithm version and the number after `.` indicates the build version. For example, `2.3` means that the version is the third build made with algorithm version 2. Every build has different texts. (The versioning can have errors in it.)
## Regenerating bundles
If you want to, you can regenerate the bundles to have different texts.
### You need:
- Python 3
- [Markovify](https://github.com/jsvine/markovify/blob/master/README.md#installation)
- A terminal

### Instructions:
1. Open the terminal and navigate to the root of the mod directory
2. Put the source bundles you want to use to the directory `Mindustry/core/assets/bundles`
3. Type `python3 randomiser.py`
4. Wait. It might take some time.
5. You should have the newly generated random bundles ready!
