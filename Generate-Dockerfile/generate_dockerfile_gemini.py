from google import genai
import os

# Set API key

# Export your Google API key as an environment variable before running the script in your terminal:

# export GOOGLE_API_KEY="your_api_key_here"


# Configure the gemini model

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


PROMPT = """ 
ONLY Generate an ideal Dockerfile for {language} with best practices. Do not provide any description
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
- Multi stage build
"""

def generate_dockerfile(language):
    response = client.models.generate_content(model='gemini-3-flash-preview', contents=PROMPT.format(language=language))
    return response.text



if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)