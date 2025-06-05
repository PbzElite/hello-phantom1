from gpt4all import GPT4All
from weatherscrape_test import WeatherScrape
model = GPT4All('Meta-Llama-3-8B-Instruct.Q4_0.gguf', allow_download=False)
#model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf', allow_download=False)

weatherresponse = [WeatherScrape.scrapeWeather("today"), WeatherScrape.scrapeWeather("tomorrow")]
print(f"weatherresponse:\ntoday: {weatherresponse[0]}\ntomorrow: {weatherresponse[1]}")
system_prompt = '### System:\nYou are an AI  assistant model, meant to answer the questions of users with information given to you by a real-time source, and your own knowledge. If your source gives you no information about the question, answer it without using the source. Keep your responses brief, and only supply the information asked for. Your source tells you that the weather today is '+ weatherresponse[0] +', and the weather tomorrow is ' + weatherresponse[1] + '.\n\n'
prompt_template = '### User:\n{0}\n\n### Response:\n'

output = ""

with model.chat_session(system_prompt=system_prompt, prompt_template=prompt_template):
    for token in model.generate(input("Q: "), streaming=True):
        #print(token)
        print(token, end='', flush=True)
        output += (token + '')

print('Saved output: ' + output)
print('Spoken output: ' + output.split('###')[0])