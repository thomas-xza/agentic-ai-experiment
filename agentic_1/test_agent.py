#!/usr/bin/env python3

from agents import Agent, Runner, RunConfig
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
)

async def main():
    
    print(os.getenv("OPENAI_API_KEY"))

    result = await Runner.run(
        agent,
        "When did the Roman Empire fall?",
        run_config=RunConfig(model="gpt-5.6-luna"),
    )

    print("Awaiting")
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())
