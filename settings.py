import os


class Settings():
    USERNAME = os.getenv('USERNAME', '')
    PASSWORD = os.getenv('PASSWORD', '')
    PUBLIC_KEY = os.getenv('PUBLIC_KEY', '')
    MAX_TRIES = os.getenv('MAX_TRIES', 5)


settings = Settings()
