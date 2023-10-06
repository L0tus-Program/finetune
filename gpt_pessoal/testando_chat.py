import openai

# sua chave API
openai.api_key = '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'

def chat_with_gpt3():
    while True:
        # Pegue a mensagem do usuário
        message = input("Você: ")
        if message.lower() in ['sair', 'exit']:
            print("Encerrando chat...")
            break

        # Envie a mensagem para o GPT-3.5-turbo e obtenha a resposta
        persona = "Você é o Jerbis um assistente de TI empenhado a tirar dúvidas de leigos na área da informática e auxiliar a resolver problemas da área. Não deve entrar em assuntos não relacionados a área de informática e computação."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": persona},
                {"role": "user", "content": message}
                
            ]
        )

        print("ChatGPT:", response.choices[0].message['content'].strip())

if __name__ == '__main__':
    print("Iniciando chat com ChatGPT. Digite 'sair' ou 'exit' para encerrar.")
    chat_with_gpt3()
