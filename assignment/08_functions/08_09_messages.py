# 08_09_messages.py

def show_messages(messages):
    """Prints each message in the list."""
    for message in messages:
        print(message)
text_messages = [
    "Hey, how are you?",
    "Don't forget the meeting at 3.",
    "Can you send me the file?",
    "¡Hola! ¿Cómo estás?"
]

# Call the function
show_messages(text_messages)