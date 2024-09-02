import os
from openai import OpenAI
from dotenv import load_dotenv

class MavSDKCodeGenerator:
    def __init__(self, api_key=None):
        if api_key:
            self.api_key = api_key
        else:
            load_dotenv()
            self.api_key = os.getenv("OPENAI_API_KEY")
        
        self.client = OpenAI(api_key=self.api_key)

    def create_prompt(self, command):
        prompt = (
            "You are an expert in drone programming using MavSDK. "
            "Generate Python code using MavSDK to execute the following command. "
            "Include necessary imports, drone connection setup, and error handling. "
            "Assume the script is run in an async environment. "
            "Do not include any markdown code block indicators.\n\n"
            f"Command: {command}\n\n"
            "Python Code:\n"
        )
        return prompt

    def generate_code(self, command):
        prompt = self.create_prompt(command)
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert MavSDK programmer."},
                {"role": "user", "content": prompt},
            ]
        )
        
        code = response.choices[0].message.content.strip()
        return self.clean_code(code)

    def clean_code(self, code):
        # Remove any potential markdown code block indicators
        code = code.replace("```python", "").replace("```", "")
        return code.strip()

    def save_code(self, code, filename="drone_script.py"):
        with open(filename, "w") as file:
            file.write(code)
        print(f"Code saved to {filename}")

# Example usage
if __name__ == "__main__":
    generator = MavSDKCodeGenerator()
    command = "Take off, fly to coordinates (47.397606, 8.543060) at an altitude of 10 meters, hover for 5 seconds, then land."
    code = generator.generate_code(command)
    print("Generated MavSDK Code:\n")
    print(code)
    generator.save_code(code)