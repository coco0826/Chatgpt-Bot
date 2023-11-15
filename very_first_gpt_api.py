import openai

openai.api_key='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'


def ask_to_gpt_35_turbo(user_input):
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        top_p=0.1,
        temperature=0.1,
        messages=[
            {'role': 'system', 'content': 'Your are a helpful assistant.'},
            {'role': 'user', 'content': user_input}
        ]
    )

    return response.choices[0].message.content


user_request='''
여자친구 사귀는 방법을 알려줘.
'''

r = ask_to_gpt_35_turbo(user_request)
print(r)