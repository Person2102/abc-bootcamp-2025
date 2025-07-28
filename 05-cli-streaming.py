from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

stream = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn in korean.",
    stream=True,
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end="", flush=True)