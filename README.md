# step-game-lib

This library is used to create decision-based mult-end games

## Installation
Download or clone it and then install with `setup.py`
For reference, `python setup.py install`

## Usage
For use, import the step class

```
from steplib import Step
``` 

It is optional to add choices to the `Step` class upon initialization

However, that means you have to provide children,

for example,

```
choices = {
  "1": Step object 1,
  "2": Step object 2
}
```

These are a dictionary describing the result of the user input

If the user inputs "1", it will activate step object 1

For what the user actually sees,

use options followed by the prompt

For example,

```
options = {
  "somechoice": "1",
  "someotherchoice": "2"
}
```
