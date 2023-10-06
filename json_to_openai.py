import os
import openai
import json
import save
# Check data formatting 
# https://cookbook.openai.com/examples/chat_finetuning_data_prep

chave_open = "sua-chave"

def json_to_l(objeto):
    print("Entrando json_to_l")
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
    print(f"Saida L : {output_jsonl_file}")
    fine(output_jsonl_file)
    #return output_jsonl_file


def fine(objeto):
    objeto = objeto
    #save.organizador(objeto) # final da função
    print (f"ENTRANDO FINE OBJETO = {objeto}")

    openai.api_key = (chave_open, "rb")
    op = openai.File.create(
        file=open(objeto),   #"dados.jsonl", "rb"),
        purpose='fine-tune'
    )
    # Minimo 10 linhas para finetuning
    print(op)
    openai.FineTuningJob.create(training_file=op.get("id"), model="gpt-3.5-turbo")

