import os
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("./.env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chapter_creation(
    title: str,
    subject: str,
    genre_motivation: str,
    description: str,
    styling: str,
    images: bool,
    chatGPTModel: str,
):
    print(f"Writing chapters for {title}")
    response = client.chat.completions.create(
        model=chatGPTModel,
        response_format={"type": "json_object"},
        max_tokens=3000,
        messages=[
            {
                "role": "system",
                "content": f"You are a creative, experienced, and prolific write in the {subject} genre of literature. {genre_motivation}. Give the output as JSON.",
            },
            {
                "role": "user",
                "content": f"First, write the chapters and subheadings for the ebook titled {title}. Provide the chapter names as keys and the corresponding subheaders as values. {styling}",
            },
        ],
    )

    with open("chapters.json", "w") as chapter_list:
        print(response.choices[0].message.content)
        json.dump(json.loads(response.choices[0].message.content), chapter_list)


def chapter_content_creation(
    # title,
    # subject,
    # chapters,
    # genre_motivation,
    # description,
    # styling,
    # images,
    # chatGPTModel,
):

    num = 1
    with open("chapters.json", "r") as chapter_list:
        chapters = json.load(chapter_list)
    for chapter in chapters:
        subheader1 = chapters[chapter][f"{num}.1"]
        subheader2 = chapters[chapter][f"{num}.2"]
        print(subheader1, subheader2)
        num += 1

    # Decide whether to loop through each chapter and have seperate AI calls for each or have it do all of them at once

    # response = client.chat.completions.create(
    #     model=chatGPTModel,
    #     response_format={"type": "json_object"},
    #     max_tokens=3000,
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": f"You are a creative, experienced, and prolific write in the {subject} genre of literature. {genre_motivation}. Give the output as JSON.",
    #         },
    #         {
    #             "role": "user",
    #             "content": f"First, write the chapters and subheadings for the ebook titled {title}. Provide the chapter names as keys and the corresponding subheaders as values. {styling}",
    #         },
    #     ],
    # )
    #


chapter_content_creation()

# chapter_creation(
#     "A girl and her guitar",
#     "sci-fi",
#     "The story should end with an epic guitar duel.",
#     "Tell the story of a girl and her guitar.",
#     "This story should have five chapters, each with two subheadings in total. Be sure to list the chapters as keys and subheaders as values.",
#     "False",
#     "gpt-3.5-turbo",
# )
