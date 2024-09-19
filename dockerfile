# Usar uma imagem base do Python
FROM python:3.12

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o diretório de trabalho
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que o aplicativo usará
EXPOSE 8080

# Comando para iniciar o aplicativo
CMD ["python", "transcription_api.py"]