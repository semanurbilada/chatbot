<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/3649/3649460.png" width="200" height="200" alt="chatbot">
</div>

<h1 align="center">ChatBot</h1>

*  [:hash: Purpose](#hash-purpose)
*  [:hash: Basic Scripts](#hash-basic-scripts)
*  [:hash: Notes](#hash-notes)

<p align="justify">

# :hash: Purpose
Welcome to the Chatbot project! This Open-Source Chatbot is widely used to be a various addition to Full-Stack web projects, improves user interactions by connecting Front-End and Back-End APIs. 🔗

Imagine you're building a website or a web application, that involves user interaction; this ChatBot can play a main role in delivering real-time responses, assistance, and more user experience with the dataset that you developed as a custom in the intents.json file. 🤖 💬

Do not forget; when you develop the custom dataset, you need to test and update to ChatBot and custom dataset multiple times. 

# :hash: Basic Scripts
1. Virtual environment setup:
```
python -m venv environment_name
```

2. To activate the virtual environment (Windows):
```
environment_name/Scripts/activate
```

3. To activate the virtual environment (Linux / MacOS):
```
source environment_name/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Run:
#### [Click Here, to see `How to run the chatbot?`](https://github.com/semanurbilada/chatbot/tree/feature/client/chatbotAPI)

# :hash: Notes

#### 1. gitignore content (chatbotAPI folder): Files from training.py after running.

#### 2. intents.json (chatbotAPI folder): Dataset; It stores all possible inputs and responses for training.

#### 3. Client folder: Contains a base example of how to send a message to chatbot from client.

#### 4. Warning: If you are a Windows user; in the training.py file, sometimes you need to add two lines for the library of nltk:

```
nltk.download('punkt')
nltk.download('wordnet')
```
</p>