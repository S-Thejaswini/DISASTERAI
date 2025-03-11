from groq import Groq

# Initialize the Groq client with your API key
API_KEY = "YOUR_API_KEY"  # Replace with your actual Groq API key
client = Groq(api_key=API_KEY)

# Define the system message to make the assistant focus on disaster-related queries
system_message = {
    "role": "system",
    "content": "You are an assistant trained to answer only disaster-related queries. If a user asks a non-disaster-related question, politely inform them that you can only respond to disaster-related topics."
}

# Initialize the conversation history with the system message
conversation_history = [system_message]

# Function to handle chat with the assistant
def chat_response(conversation_history):
    # Make the request to the Groq model
    completion = client.chat.completions.create(
        model="llama3-8b-8192",  # The model you're using
        messages=conversation_history,  # Send the conversation history
        temperature=1,  # Randomness of the response (higher = more creative)
        max_tokens=1024,  # Max number of tokens in the response
        top_p=1,  # Controls diversity
        stream=False, # Don't stream, get the full response in one go
    )
    
    # Extract and return the assistant's response
    return completion.choices[0].message.content

def main():
    print("Welcome to the Disaster Response Assistant! Type 'exit' to end the conversation.")
    
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Ending the conversation. Goodbye!")
            break
        
        # Add the user's message to the conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Get the assistant's response based on the conversation history
        bot_response = chat_response(conversation_history)
        
        # Add the bot's response to the conversation history
        conversation_history.append({"role": "assistant", "content": bot_response})
        
        # Print the bot's response
        print(f"Bot: {bot_response}")

# Run the chatbot
if __name__ == "__main__":
    main()
