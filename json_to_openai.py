import os
import openai
import json

# Check data formatting 
# https://cookbook.openai.com/examples/chat_finetuning_data_prep

def json_to_l(objeto):
    # Caminho para o arquivo JSON de entrada
    input_json_file = objeto
    # Caminho para o arquivo JSONL de saída
    output_jsonl_file = 'dados.jsonl'

    # Lista para armazenar objetos JSON do arquivo de entrada
    json_objects = []

    # Leia o arquivo JSON e carregue os dados
    with open(input_json_file, 'r') as file:
        json_objects = json.load(file)

    # Abra o arquivo JSONL de saída em modo de escrita
    with open(output_jsonl_file, 'w') as file:
        # Itere sobre os objetos JSON e escreva cada um em uma nova linha no arquivo JSONL
        for obj in json_objects:
            json_line = json.dumps(obj)
            file.write(json_line + '\n')

    print(f'Conversão de {input_json_file} para {output_jsonl_file} concluída com sucesso!')
    #Enviando jsonl convertido para função fine
    fine(output_jsonl_file)


def fine(objeto):
    objeto = objeto
    print (f"ENTRANDO FINE OBJETO = {objeto}")
    """openai.api_key = os.getenv("OPENAI_API_KEY") # Chave openai
    openai.File.create(
    file=open("mydata.jsonl", "rb"),
    purpose='fine-tune'
    )

    #Create a fine-tuned model
    openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo") # Colocar o nome da persona do GPT ?
"""
    # In addition to creating a fine-tuning job, you can also list existing jobs, retrieve the status of a job, or cancel a job.
"""
    # List 10 fine-tuning jobs
    openai.FineTuningJob.list(limit=10)

    # Retrieve the state of a fine-tune
    openai.FineTuningJob.retrieve("ft-abc123")

    # Cancel a job
    openai.FineTuningJob.cancel("ft-abc123")

    # List up to 10 events from a fine-tuning job
    openai.FineTuningJob.list_events(id="ft-abc123", limit=10)

    # Delete a fine-tuned model (must be an owner of the org the model was created in)
    openai.Model.delete("ft-abc123")

    #Use a fine-tuned model -> Acho que é só ua alternativa
    completion = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )
    print(completion.choices[0].message)"""



# Invocando funcao fine

#fine(objeto = None)