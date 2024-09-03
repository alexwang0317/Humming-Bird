import os
from openai import OpenAI
from dotenv import load_dotenv

class DroneCommandPlanner:
    def __init__(self, api_key=None):
        # Load the API key from the environment variable if not provided
        if api_key:
            self.api_key = api_key
        else:
            load_dotenv()
            self.api_key = os.getenv("OPENAI_API_KEY")
        
        # Initialize the OpenAI client
        self.client = OpenAI(api_key=self.api_key)

    def create_prompt(self, command):
        """
        Creates a prompt for OpenAI to process.
        """
        prompt = (
            "You are an expert in drone programming. "
            "Break down the following command into simple, executable steps for a drone to perform. "
            "The drone uses the MavSDK library for control.\n\n"
            f"Command: {command}\n\n"
            "Steps:\n"
        )
        return prompt

    def get_plan(self, command):
        """
        Sends the command to OpenAI and returns a simplified plan.
        """
        prompt = self.create_prompt(command)
        
        # Send the prompt to OpenAI and get the response using the correct API method
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert drone programming assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        
        # Extract and return the response content
        plan = response.choices[0].message.content.strip()
        return plan

# Example usage
if __name__ == "__main__":
    planner = DroneCommandPlanner()
    command = "Fly 5 meters in the air and hover for 10 seconds."
    plan = planner.get_plan(command)
    print("Drone Command Plan:\n")
    print(plan)