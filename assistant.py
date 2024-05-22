from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
from event_handler import EventHandler
# load api key manually from .env file
load_dotenv()
key = os.getenv('OPENAI_API_KEY')
openai.api_key = key
client = OpenAI()


thread = client.beta.threads.create()
event_handler = EventHandler()
def send_message(message, delta_callback=None):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    if delta_callback:
        event_handler.text_delta_callback=delta_callback
    with client.beta.threads.runs.stream(
        thread_id=thread.id,
        assistant_id="asst_aIaIoyif1qLSCRKk6eSNf8rl",
        instructions="Please address the user as Jane Doe. The user has a premium account.",
        event_handler=event_handler,
    ) as stream:
        stream.until_done()

def print_delta(delta):
    print(delta.value, end="", flush=True)
    
if __name__ == "__main__":
    send_message("Hello", delta_callback=print_delta)