# AVOVA Project for Timsort

A simple project to test Python's `sort()` function under various conditions. A full factorial design is created using list lengths of 1000000, 2000000 and 3000000 along with randomly generated starting lists created using several probability distributions. Thus this expirment contains two factors: list length and original sorting (or lack there of).

The file `project_4.Rmd` contains an analysis of the data.

## Links

* Sorting data of known distribution: https://stackoverflow.com/questions/6166546/sorting-algorithms-for-data-of-known-statistical-distribution
* Probability sorting: http://www.cs.rochester.edu/~cding/Documents/Publications/icpp04.pdf

## Build the Development Environment
To create your python environment simply run
```
make build_env
```
from this repositories base directory and then run
```
source env/bin/activate
```
as well. This will activate the virtual environment 
created in the first line of code. All development should
be done using this environment to ensure that results can
be reproduced by other contributors.
