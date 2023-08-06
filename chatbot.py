import os
import openai

def setup_openai():
    # Set the OpenAI API key from the environment variable "OPENAI_API_KEY"
    openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_text(prompt):
    # Create a completion request to the OpenAI API using the provided prompt
    completions = openai.Completion.create(
        engine="text-davinci-003",  # Specify the language model engine to use
        prompt=prompt,  # The text prompt to generate the response from
        max_tokens=1024,  # Maximum length of the generated response in tokens
        n=1,  # Number of responses to generate
        stop=None,  # Tokens at which the response should stop (None means no specific stopping tokens)
        temperature=0.5,  # Temperature parameter controls the randomness of the generated text
    )

    # Extract the generated text from the API response
    message = completions.choices[0].text
    return message

if __name__ == "__main__":
    # Set up the OpenAI API by reading the API key from the environment variable
    setup_openai()

    while True:
        # Get user input as a prompt
        user_input = input("You: ")
        
        # Generate a response from the user input using the OpenAI API
        response = generate_text(user_input)
        
        # Display the generated response from the chatbot
        print("Bot: ", response)
