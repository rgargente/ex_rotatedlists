# Coding exercise: search item inside a sorted, rotated, non unique list 

- A sorted list is one like: [2, 4, 5, 6, 10, 22]
- A sorted, rotated list is one like: [6, 10, 22, 2, 4, 5]
- A sorted, non unique, rotated list is one like this: [6, 6, 10, 22, 22, 22, 2, 4, 4, 5]

Writing an algorithm to search for the position of an element (any position, if there are more than one) in an 
efficient way is not a trivial task. Some cases especially difficult are the ones where it is hard to find non
repeating elements like for example looking for 2 in [5, 5, 5, 5, 5,5, 5, 5, 5, 5, 5, 1, 2, 5, 5].
## How to run the program

The exercise is implemented using Python 3. 

I have provided an Anaconda environment file to easily create an environment to run the software. If you have Anaconda
installed, simply run the following command in a terminal:
```
 conda env create -f environment.yml
```

Otherwise install each dependency using ```pip install ```. You can read the environment.yml file to know which 
dependencies you need, but I would recommend just installing whatever python tells is missing
since most of the dependencies should already be installed by default. 

There are two folders, one for each exercise. Please read the comments included with the code as the provide some 
insight about the design.

## Files
There are two source files, rotlist.py and test/test_rotlist.py. The former contains two algorithms, one to find values
in a sorted list of unique elements and another one to find values in a sorted, rotated list of non unique elements. 
The test file contains multiple tests implemented using pytest. They can be run executing ``pytest`` in a terminal.

The code contains comments and some design considerations.  