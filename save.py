import json
import os
import datetime



def organizador(objeto):
    print("Entrando organizador")

    # Diretório onde os arquivos JSONL serão salvos
    output_directory = 'jsonl_files'

    # Obtenha a data atual
    data_atual = datetime.datetime.now()

    # Crie uma estrutura de pastas organizadas por ano e mês
    ano = data_atual.year
    mes = data_atual.month
    pasta_ano_mes = os.path.join(output_directory, f'{ano:04d}', f'{mes:02d}')

    # Crie a estrutura de pastas se ela não existir
    os.makedirs(pasta_ano_mes, exist_ok=True)

    # Construa o nome do arquivo JSONL com a data
    nome_arquivo_jsonl = f'{data_atual.strftime("%Y-%m-%d_%H-%M-%S")}.jsonl'
    caminho_arquivo_jsonl = os.path.join(pasta_ano_mes, nome_arquivo_jsonl)

    # Abra o arquivo JSONL de saída em modo de escrita
    with open(caminho_arquivo_jsonl, 'w') as file:
        # Escreva os objetos JSON do argumento diretamente no arquivo JSONL
        for obj in objeto:
            json_line = json.dumps(obj)
            file.write(json_line + '\n')

    print(f'Arquivo JSONL gerado e salvo em {caminho_arquivo_jsonl}')
 
 
 # Carregue os dados JSON do arquivo
#with open('dados.json') as json_file:
 #   dados_json = json.load(json_file)


#organizador(dados_json)