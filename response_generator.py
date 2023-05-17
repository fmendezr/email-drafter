import openai
import os 

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]

def generate_prompt(subject, sender_name, recipient_name, tone, goal, bg_info, im_info, length, language="english"):
    prompt = f"""
    Generate an email in {language} meeting the criteria enclosed in the parenthesis below and seperated by comas: \
    (
        subject of email: {subject},
        addressed to: {recipient_name}
        signed by: {sender_name}
        tone of email: {tone},
        goal: {goal},
        background_info: {bg_info},
        important info that must be included: {im_info}, 
        target length of body of email: {length}
    )
    Remember to take your time to generate a response. Once so review if ti meats all the criterias inside the parenthesis. If so \
    deliver the response. If it does not match the critera take your time creating a more appropiate response. Do not be repetitive
    """
    return prompt

def get_response(subject, sender_name, recipient_name, tone, goal, bg_info, im_info, length, language="english"):
    return get_completion(generate_prompt(subject, sender_name, recipient_name, tone, goal, bg_info, im_info, length, language))
