short_text =['how are you', 'I am fine', 'what about you', 'I am good too']

def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

show_messages(short_text)

def send_messages(messages,sent_messages):
    """Simulate sending each message, until none are left.
    Move each message to sent_messages after sending."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
    print("\n--------------------------------")
sent_messages = []
send_messages(short_text[:], sent_messages)