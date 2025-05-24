# Conversão e Padronização de Dados CSV

Este script realiza o processamento de arquivos CSV, convertendo colunas específicas para UUID e ajustando colunas numéricas com valores em formato string. É útil para anonimização de dados e padronização de campos numéricos.

## ⚙️ Funcionalidades

- Converte colunas com IDs (`state_id`, `country_id`, `account_id`, `customer_id`, `id`) para UUIDs determinísticos.
- Remove `.0` de strings numéricas e converte as colunas (`pix_requested_at`, `pix_completed_at`, `transaction_requested_at`, `transaction_completed_at`) para inteiros (`Int64`).
- Salva os arquivos processados em uma nova pasta com o prefixo `uuid_`.