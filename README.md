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

use options followed by the choice you want to see in `choices`

For example,

```
options = {
  "somechoice": "1",
  "someotherchoice": "2"
}
```

The first argument is the prompt itself.

A complete example:
```
master = Step("Hello! How can I help you?", {
  "s": success
  "f": failure
}, {
  "star this": "s",
  "fork this": "f"
}
```
To create endings, use the same `Step` class, but leave both `choices` and `options` as defaults
```
success = Step("Success!")
failure = Step("Failure!")
```
To start the program, call master directly,
```
master()
```
