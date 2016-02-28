# Lab 1

Implements lab 1 from datamining course. 

### What does it does

It implements testing of plain classifier and [One Rule](http://www.saedsayad.com/oner.htm) algorythm. 

The count of data selected to the training data depends on [MAX_SELECTOR](main.py#L8)

### File walkthrough

* [classifier.py](classifier.py) - implements plain classifier based on self-written primitive algorythm
* [onerule.py](onerule.py) - implements classifier based on [One Rule](http://www.saedsayad.com/oner.htm) algorythm
* [main.py](main.py) - implements main program method: main function to run the testing of algorythm and reading from csv file
* [iris.data](iris.data) - file that holds data to be analyzed
* [iris.names](iris.names) - seems to be some kind of *manual* to the [iris.data](iris.data) file.

### Lab results

1. With training data 50 points, 
	* *Plain classifier* algorythm shows not good results of 26 errors of 151 checks;
	* *One Rule* algorythm shows ideal accuracy: 0 errors of 151 checks.
2. With training data 15 points: 
	* *Plain classifier* has 58 errors of 151 total.
	* *One Rule* algorythm shows accuracy of 6.6%: 10 of 151 were incorrect 
