from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def main():
    print("Asking a question from gemini")

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {
                "role": "system",
                "content": "Your are math assistant. you just answer relevant question. dont' answer irrelevant question.",
            },
            {"role": "user", "content": "Who is the founder of Paksitan?"},
        ],
    )
    message = response.choices[0].message.content
    print("Gemini Response: ")
    print(message)
    # print(response)
    # print(response.choices)
    # print(response.choices[0])
    # print(response.choices[0].message)
    # print(response.choices[0].message.content)

if __name__ == "__main__":
    main()

