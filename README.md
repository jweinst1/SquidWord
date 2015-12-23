#Squidword

Squidword is a python command line program that can compress written English language into JSON data via the form of sentence tries. This makes a great method for checking grammar, or natural language processing.

Normally, tries are a type of prefix structure used for looking up words, in a manner which does not include collisions, such as with Hash tables. Squidword uses tries to store statements, either sentences or questions, for looking up.

##Storing

Squidword creates sentence tries by splitting a string of sentence by the `" "` character, and then creating a node for each word in the trie. Repeated words from different statements in the same order are bound to the same node. Here is an example:

```
>>> f = strie()
>>> f.statement("People don't love corn.")
>>> f.statement("People do love corn.")
>>> f.statement("People can love corn.")
>>> f.statement("People could love corn.")
>>> f
{'People': 
	{'do': {'love': {'corn.': {}}}, 
	'could': {'love': {'corn.': {}}}, 
	'can': {'love': {'corn.': {}}}, 
	"don't": {'love': {'corn.': {}}}}}
```

The tries are implemented with Python builtin dictionaries to easily allow them to be written to JSON format. All of the language files can be accessed with command line arguments, since Squidword is bundled in a Python package.

##Commands

These are the commands that can be run from the command line. The notation `<>` signifies a custom paramter with no brackets.

####`Squidword start <Filename> <langname>` : 
Scans and parses a file for English sentences, questions, and other statements, into a new JSON file in the `.squidword` directory. `langname` should not have any extension on it.

####`Squidword put <Filename> <langname>` : 
Scans and parses a file for English sentences, questions, and other statements, into an existing JSON language file in the `.squidword` directory. Will not work if <Filename> as a path does not exist.

####`Squidword files` : 
Prints out a list of all files that exist in the `.squidword` directory.

####`Squidword random <langname>` : 
Prints out a random statement from one of the JSON sentence tries stored in the package. It constructs the statement randomly by searching the tree with randomly selected nodes.

####`Squidword getfile <langname>` : 
Copies one of the JSON files stored in the `.squidword` directory to the current directory the package is stored in.

####`Squidword init` : 
Creates the `.squidword` directory as a subdirectory. This must always be done before any other command in the program is used.

####`Squidword link <linkname> <langname>` : 
Takes a url address, and parses the loaded HTML file for English sentences, questions, other statements, into a new or existing JSON file of the name langname.

####`Squidword CLI`: 
Initiates a command line interface session, where you can commit statements and sentences to a trie one by one and reference them individually. This gives a simple way for a user to understand the data structure and it's potential uses.
