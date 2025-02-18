from openai import OpenAI
import os
import time

def retrieve_api_key() -> str:
    return os.getenv("OPENAI_API_KEY")

def main():
    model_name = "gpt-4o"
    openai_api_key = retrieve_api_key()

    if openai_api_key is None: 
        print("OPENAI_API_KEY is not set in the environment variables. Please configure and try again.")
        return

    client = OpenAI(api_key=openai_api_key)

    while True:
        try: 
            user_input = input("Please enter a question or 'quit' to exit the program: ")
            if user_input.lower().strip() == "quit":
                break;
            
            response = client.chat.completions.create(
                model = model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Please provide your response in short, clear and concise format."},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.5,
                max_tokens=1024,
                top_p=1.0
            )
            
            if response.choices and response.choices[0].message and response.choices[0].message.content:
                print(f"Assistant: {response.choices[0].message.content}")
            else: 
                print("No valid response received from the OpenAI API.")
                
            time.sleep(3) # avoid rate limit 
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    main()