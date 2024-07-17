from feliz.file_tools import read_yaml
import os

SERVER_CONFIG = read_yaml(f"{os.getcwd()}/configs/private/server_config.yaml")["content"]

bind = f"{SERVER_CONFIG['SERVER']['HOST']}:{SERVER_CONFIG['SERVER']['PORT']}"
workers = SERVER_CONFIG["SERVER"]["WORKERS"]

# gunicorn -c gconfig.py app:app
