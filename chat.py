import openai
from config import TOKEN

openai.api_key = TOKEN
messages = []

# Бесконечный цикл 
while True:
    content = input("Question: ")

    # Задаем вопрос
    messages.append({"role": "user", "content": content})
    
    # Отправляем на обработку
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # Получаем ответ
    chat_response = completion.choices[0].message.content

    # Добавляем ответ в память, для запоминания ответа
    messages.append({"role": "assistant", "content": chat_response})

    print(f'ChatGPT: {chat_response}')