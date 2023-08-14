<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/3649/3649460.png" width="200" height="200" alt="chatbot">
</div>

<h1 align="center">Chatbot</h1>

*  [:hash: Purpose](#hash-purpose)
*  [:hash: Basic Scripts](#hash-basic-scripts)
*  [:hash: Notes](#hash-notes)

<p align="justify">

## Purpose
Welcome to the Chatbot project! This Open-Source Chatbot is widely used to be a various addition to Full-Stack web projects, improves user interactions by connecting Front-End and Back-End APIs. 🔗

Imagine you're building a website or a web application, that involves user interaction; this chatbot can play a main role in delivering real-time responses, assistance, and more user experience with the data set that you developed as a custom in the intents.json file. 🤖 💬

Do not forget when you develop the custom data set, you need to test and update to chatbot and custom data set multiple times. 

## Basic Scripts
To run the basic scripts, follow these commands:

```
cd chatbot
```
```
python training.py
# or
python3 training.py
```
```
python chatbot.py
# or
python3 chatbot.py
```

## Notes

#### 1. gitignore content: Files from training.py after running.

#### 2. intents.json: Data set; It stores all possible inputs and responses for training.

#### 3. Warning: If you are a Windows user; in the training.py file, sometimes you need to add two lines for the library of nltk:

```
nltk.download('punkt')
nltk.download('wordnet')
```
</p>