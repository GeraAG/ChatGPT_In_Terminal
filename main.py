from openai import OpenAI

client = OpenAI()
txt_input = ''
print("Send a message ")

while txt_input.lower() != 'exit':
  txt_input = input()
  if txt_input.lower() == 'exit':
    break
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=300,
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": txt_input}
    ]
  )

  print(completion.choices[0].message.content)





