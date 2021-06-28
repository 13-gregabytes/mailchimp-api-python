import configparser
config = configparser.RawConfigParser()
config.read('config.properties')

host = config.get('database',     'db.host')
port = config.get('database',     'db.port')
username = config.get('database', 'db.user')
password = config.get('database', 'db.password')
database = config.get('database', 'db.database')


def get_host():
    return host


def get_port():
    return port


def get_username():
    return username


def get_password():
    return password


def get_database():
    return database

