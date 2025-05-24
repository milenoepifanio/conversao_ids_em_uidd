import pandas as pd
import uuid # geração de UUIDs
import os  # manipulação de diretórios e arquivosrecrie 


def generate_uuid(value):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, str(value)))

input_directory = 'csv' # Diretório onde estão os arquivos CSV de entrada
output_directory = 'csv_2' # Diretório onde os arquivos processados serão salvos

os.makedirs(output_directory, exist_ok=True) # Cria o diretório de saída se ele não existir
# Nome das colunas a serem codificadas
columns_to_convert = ['state_id', 'country_id', 'account_id', 'customer_id', 'id'] 

# Colunas com valores string para conversão em decimais
columns_with_decimal_strings = ['pix_requested_at', 'pix_completed_at', 'transaction_requested_at', 'transaction_completed_at'] 

for filename in os.listdir(input_directory):
    if filename.endswith('.csv'): # Processa apenas arquivos .csv
        file_path = os.path.join(input_directory, filename)
        
        df = pd.read_csv(file_path)
        # Converte colunas com valores ".0" para inteiros
        for column in columns_with_decimal_strings:
            if column in df.columns:
                df[column] = df[column].apply(lambda x: int(str(x).replace('.0', '')) if pd.notna(x) else x).astype('Int64')
                print(f'Coluna "{column}" corrigida para Int64 no arquivo {filename}.')
            else:
                print(f'Coluna "{column}" não encontrada em {filename}. Pulando...')
                
        # Converte colunas específicas para UUID
        for column in columns_to_convert:
            if column in df.columns:
                df[column] = df[column].apply(generate_uuid)
                print(f'Coluna "{column}" convertida para UUID no arquivo {filename}.')
            else:
                print(f'Coluna "{column}" não encontrada em {filename}. Pulando...')
                
        # Define o caminho de saída com prefixo "uuid_"
        output_file_path = os.path.join(output_directory, f'uuid_{filename}')
        
        # Salva o DataFrame processado como novo CSV
        df.to_csv(output_file_path, index=False)
        print(f'Arquivo processado: {filename} -> {output_file_path}')