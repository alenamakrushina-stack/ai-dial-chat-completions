import asyncio
import os
import task
from dotenv import load_dotenv
load_dotenv()

from task.clients.client import DialClient
from task.constants import DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role
from dotenv import load_dotenv


async def start(stream: bool) -> None:

    DIAL_API_KEY = os.getenv('DIAL_API_KEY')
    print("DIAL_API_KEY from env:", os.getenv('DIAL_API_KEY'))

    # 1.1. Get deployment name, for demo use 'gpt-4o'
    deployment_name = 'gpt-4o'
    client = DialClient(deployment_name=deployment_name)

    # 2. Create Conversation object
    conversation = Conversation()

    # 3. Get System prompt
    system_prompt = input("Provide System prompt or press 'enter' to continue.\n> ").strip()
    if not system_prompt:
        system_prompt = DEFAULT_SYSTEM_PROMPT
    conversation.add_message(Message(role=Role.SYSTEM, content=system_prompt))

    print("\nType your question or 'exit' to quit.")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        # 6. Add user message
        conversation.add_message(Message(role=Role.USER, content=user_input))
        messages = conversation.get_messages()

        if stream:
            ai_message = await client.stream_completion(messages)
        else:
            ai_message = client.get_completion(messages)
        # 8. Add generated message to history, print
        print(f"AI: {ai_message.content}")
        conversation.add_message(ai_message)

    # 1.1. Get deployment name, for demo use 'gpt-4o'
    deployment_name = 'gpt-4o'
    client = DialClient(deployment_name=deployment_name)

    # 2. Create Conversation object
    conversation = Conversation()

    # 3. Get System prompt
    system_prompt = input("Provide System prompt or press 'enter' to continue.\n> ").strip()
    if not system_prompt:
        system_prompt = DEFAULT_SYSTEM_PROMPT
    conversation.add_message(Message(role=Role.SYSTEM, content=system_prompt))

    print("\nType your question or 'exit' to quit.")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        # 6. Add user message
        conversation.add_message(Message(role=Role.USER, content=user_input))
        messages = conversation.get_messages()

        if stream:
            ai_message = await client.stream_completion(messages)
        else:
            ai_message = client.get_completion(messages)
        # 8. Add generated message to history, print
        print(f"AI: {ai_message.content}")
        conversation.add_message(ai_message)




asyncio.run(
    start(True)
)
