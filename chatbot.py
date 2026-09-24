import random

def simple_chatbot():
    print("Chatbot: Hello! I am your Python assistant. Type 'bye' to exit.")
    
    # Predefined responses
    responses = {
        "hello": ["Hi there!", "Hello! How can I help you today?", "Hey! Nice to meet you."],
        "how are you": ["I'am fine , I'm doing great! How about you?", "Doing well, thanks for asking!"],
        "what is your name": ["I'm a simple Python bot created by you!", "You can call me PyBot."],
        "bye": ["Goodbye! Have a wonderful day!", "Bye! Come back soon."]
    }

    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("You: ").strip().lower()
        
        # Check for exit condition
        if user_input == "bye":
            print(f"Chatbot: {random.choice(responses['bye'])}")
            break
            
        # Find a matching response or use a default fallback
        found_match = False
        for key in responses:
            if key in user_input:
                print(f"Chatbot: {random.choice(responses[key])}")
                found_match = True
                break
                
        if not found_match:
            print("Chatbot: I'm not sure how to respond to that. Can you ask me something else?")

if __name__ == "__main__":
    simple_chatbot()