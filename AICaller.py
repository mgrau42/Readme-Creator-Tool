import os
import openai
from time import time,sleep

#ADD OPENAI KEY HERE
openai.api_key = "YOUR_OPENAI_API_KEY"

# You can get one in https://platform.openai.com/account/api-keys
# as of 19/02/2023 Open AI offers a free Trial for experimenting with $18 in free credit that can be used during your first 3 months.
# im not profiting in any way from this please check their web for detailed pricing, im not responsible in any way for generating or managing this key


#abre archivo guarda su contenido en infile y lo cierra
def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()

def save_file(content, filepath):
	with open(filepath, 'w', encoding='utf-8') as outfile:
		outfile.write(content)

def gpt3_completion(prompt, model="text-davinci-003", temp=0.1, max_tok=400, top_p=1.0, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
	max_retry = 5
	retry = 0
	print('Comunicating with OpenAi...')
	while True:
		try:
			response = openai.Completion.create(
				model=model,
				prompt=prompt,
				temperature=temp,
				max_tokens=max_tok,
				top_p=top_p,
				frequency_penalty=freq_pen,
				presence_penalty=pres_pen,
				stop=stop)
				#We are accessing the first element in the choices from the 'Completion' class list with [0]. Then, we access the text property of the Choice object to retrieve the generated text.
				#So, the line text = response['choices'][0]['text'].strip() retrieves the generated text from the API response and assigns it to the text variable.
			text = response['choices'][0]['text'].strip()
			return text
		except Exception as errcondition:
			retry += 1
			if retry >= max_retry:
				return"GPT· error: %s" % errcondition
			print('Error comunicating with OpenAi:', errcondition)
			sleep(1)
