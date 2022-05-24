import re

def chatBot(userinput):
    chatbottext = re.sub(r".*my name is (\w+)", r"Good morning \1. How can I help you today?", userinput, flags=re.IGNORECASE)
    chatbottext = re.sub(r".*help me with (\w+)", r"Yes I can help you with \1. Please enter your programme of study.", chatbottext, flags=re.IGNORECASE)
    chatbottext = re.sub(r".*programme of study is (\w+)", r"Which module of \1 are you doing?", chatbottext, flags=re.IGNORECASE)
    chatbottext = re.sub(r"\?", r".", chatbottext, flags=re.IGNORECASE)
    chatbottext = re.sub(r".*doing (\w+)", r"Your details for \1 will be emailed", chatbottext, flags=re.IGNORECASE)
    chatbottext = re.sub(r".*your name?", r"My name is Wilford the Assistant", chatbottext, flags=re.IGNORECASE)
    chatbottext = re.sub(r".*you are (\w+)", r"Thank you. You are just as \1 as I am", chatbottext, flags=re.IGNORECASE)
       
    print(chatbottext)

userinput = input("Hello, What is your name? \n(To end the chat, type \"Bye\")\n")

while userinput != "Bye":
    chatBot(userinput)
    userinput = input()
      
print("Good Bye :)")
