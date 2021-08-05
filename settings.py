import os


class Settings():
    USERNAME = os.getenv('USERNAME', '')
    PASSWORD = os.getenv('PASSWORD', '')
    PUBLIC_KEY = os.getenv('PUBLIC_KEY', 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKf9iZkA5HEFw4zt7MRBkcmgUiz5+r5eqDOKbaurEbScmXd3ZZTtyzirqkYKRIH5mQ+8hq+Wd/pTZNXHS8L0+88CAwEAAQ==')
    MAX_TRIES = os.getenv('MAX_TRIES', 5)


settings = Settings()
