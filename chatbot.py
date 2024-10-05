import tkinter as tk
from tkinter import scrolledtext, messagebox
import time
import os
import speech_recognition as sr
import pyttsx3
import wikipediaapi

# Initialize the speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

#gen responce
def generate_response(message):
    message = message.lower()
    if "hi" in message:
        return "Hello! How can I assist you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing well! How about you?"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        #undefine questions 
        getpage = get_wikipedia_summary(message)
        return getpage


# Set properties for pyttsx3 (optional)
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female voice
tts_engine.setProperty('rate', 150)  # Speed of speech

# Function for handling user input and generating a response
def send():
    user_message = entry.get()  # Get the message from the entry field

    if not user_message.strip():
        return  # Ignore empty messages
    
    chat_area.config(state=tk.NORMAL)
    
    # Display the user's message
    chat_area.insert(tk.END, "You: " + user_message + "\n")
    
    # Generate a response
    bot_response = chatbot_response(user_message)
    
    # Display the bot's response
    chat_area.insert(tk.END, "Bot: " + str(bot_response) + "\n\n")
    chat_area.yview(tk.END)  # Auto scroll to the latest message
    
    # Speak the bot's response
    speak(bot_response)
    
    chat_area.config(state=tk.DISABLED)  # Disable the chat area to prevent user edits
    entry.delete(0, tk.END)  # Clear the entry field
    
# Text-to-speech function
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Voice input function using speech recognition
def voice_input():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust to ambient noise
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, "Listening...\n")
            chat_area.config(state=tk.DISABLED)
            audio = recognizer.listen(source)  # Listen to voice input
            
            user_message = recognizer.recognize_google(audio)  # Convert audio to text using Google's API
            entry.insert(tk.END, user_message)  # Insert the recognized text into the entry field
            send()  # Send the message
    except sr.UnknownValueError:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Sorry, I didn't understand that.\n")
        chat_area.config(state=tk.DISABLED)
    except sr.RequestError:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "API unavailable or network error.\n")
        chat_area.config(state=tk.DISABLED)

# Save chat history to a file
def save_history():
    chat_history = chat_area.get("1.0", tk.END)
    if chat_history.strip():
        with open("chat_history.txt", "w") as file:
            file.write(chat_history)
        messagebox.showinfo("Chat History", "Chat history saved successfully!")
    else:
        messagebox.showinfo("Chat History", "No conversation to save.")

# Load chat history from a file
def load_history():
    if os.path.exists("chat_history.txt"):
        with open("chat_history.txt", "r") as file:
            chat_area.config(state=tk.NORMAL)
            chat_area.delete("1.0", tk.END)
            chat_area.insert(tk.END, file.read())
            chat_area.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Chat History", "No saved chat history found.")

# Clear chat
def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)
    chat_area.config(state=tk.DISABLED)

# function to get responce from webpage
def get_wikipedia_summary(query):
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary[:500]  # Return the first all characters
    else:
        return "I couldn't find any information on that topic."

# Function to generate a basic response
def chatbot_response(message):
    if "tell me about" in message:
        topic = message.replace("tell me about", "").strip()
        return get_wikipedia_summary(topic)

    message = message.lower()
    
    if "hello" in message:
        return "Hi there! How can I help you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing fine!"
    elif "time" in message:
        return "The current time is " + time.strftime('%I:%M %p')
    elif "bye" in message:
        return "Goodbye! Have a great day!"

    else:
        # GPT-based or other chatbot response
        return generate_response(message)


# Create the main window
root = tk.Tk()
root.title("ChatBot")

# Chat area (scrollable)
chat_area = scrolledtext.ScrolledText(root,bg="black",fg="white", wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
chat_area.pack(padx=20, pady=10)

# Entry field for user input
entry = tk.Entry(root, width=70,bg="black", font=("Arial", 12),fg="white")
entry.pack(padx=20, pady=10, side=tk.LEFT, expand=True, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send, font=("Arial", 12))
send_button.pack(padx=10, pady=10, side=tk.LEFT)

# Voice Input button
voice_button = tk.Button(root, text="Speak", command=voice_input, font=("Arial", 12))
voice_button.pack(padx=10, pady=10, side=tk.LEFT)

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="zer0/1.0 (2002.krithik@gmail.com)"
)

# Menu bar for saving/loading chat history
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save Chat History", command=save_history)
file_menu.add_command(label="Load Chat History", command=load_history)
file_menu.add_command(label="Clear Chat", command=clear_chat)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Run the application
root.mainloop()
