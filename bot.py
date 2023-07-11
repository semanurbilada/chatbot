"""
- Phyton env: ...
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, new friend 😇",
])
trainer.train([
    "What are you, a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":p", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🌸 {chatbot.get_response(query)}")