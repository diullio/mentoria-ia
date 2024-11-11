from datetime import timedelta

# Configurando o banco de dados
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'

#Configurações da sessão
SECRET_KEY = 'mentoria-ia-2024-11-11'
SESSION_PERMANENT = 'False' #Sessão expirar quando navegador é fechado
PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)

