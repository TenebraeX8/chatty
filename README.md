# Chatty
Chatty is a very simple chatbot developed during a research paper I wrote.
It uses AIML for simple pattern matching and with very restricted abilities

## Prerequisites
For running the program, python 3 is required.
In addition, the [python-aiml package](https://github.com/cdwfs/pyaiml).
This can installed using
```pip install python-aiml```

In order to run Chatty, call
```python chatty.py```
from base directory

## Using Chatty
The following patterns will be recognized and answered:
- "HI"
- "HELLO I AM *" (name will be saved as username)
- "HOW IS THE WEATHER TODAY" or "CAN YOU TELL ME THE WEATHER"
- "I LIKE *"
- "BYE" and "BYE *" (name will be used if saved)

The bot is case-insensitive. In case you want to check if there is a problem, you can call 
```python chatty.py -t```
In order to test the possible inputs. It should not generate an error for any of them.