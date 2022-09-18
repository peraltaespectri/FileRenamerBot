import os

class Config(object):
    # obter um token de @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # As coisas da API do Telegram
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Atualizar canal para Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    # canal de registro
    #LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
    # Obtenha esses valores em my.telegram.org
    CHAT_ID = os.environ.get("CHAT_ID", "")
    # Variedade para armazenar usuários autorizados a usar o bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    # Membros indesejados banidos..
    BANNED_USERS = []
    # o local de download, onde o servidor HTTP é executado
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Tamanho máximo de upload de arquivo do telegrama
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # tamanho do bloco que deve ser usado com solicitações
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # miniatura padrão a ser usada nos vídeos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy para acessar o youtube-dl em áreas georrestritas
    # Obtenha seu próprio proxy de https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # comprimento máximo da mensagem no Telegram
    MAX_MESSAGE_LENGTH = 4096
    # definir tempo limite para o subprocesso
    PROCESS_MAX_TIMEOUT = 3600
    # arquivo de marca d'água
    DEF_WATER_MARK_FILE = ""
    # URL do banco de dados
    DB_URI = os.environ.get("DATABASE_URL", "")
    
