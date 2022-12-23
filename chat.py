#!/usr/bin/env python

from os import environ
from openai.error import AuthenticationError
from pprint import pprint

import openai

openai.api_key = environ.get('OPENAI_API_KEY')

model_engine = 'text-davinci-002'

while True:
    text = input('❓: ')

    try:
        response = openai.Completion.create(
            engine=model_engine, prompt=text, max_tokens=1024
        )

        print(38*'-', '🤖', 38*'-')
        print(str(response['choices'][0]['text']).strip())
        print(80*'-')
    except AuthenticationError as e:
        print('\n🤚 Coé mané, faltou o token da API')
        print('Define aí quando for dar o run:\n')
        print('docker run --rm -it -e OPENAI_API_KEY=xxxx chat-gpt\n')
