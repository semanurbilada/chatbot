### Scripts for Chatbot

1. `cd chatbot`
2. `python training.py` or `python3 training.py`
3. `python chatbot.py` or `python3 chatbot.py`

#### gitignore content: Files from training.py after running.

#### intents.json: It stores all possible inputs and responses for training.

#### Warning: If you are a Windows user; in the training.py file, sometimes you need to add two lines for the library of nltk:

#### `nltk.download('punkt')`
#### `nltk.download('wordnet')`