import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'SDFSWF3443TEFDSWTR34RDECTC45C3C3T344R34CDFS'
    SECRET_KEY = 'sdfghjkuytrewhjkl;lkjhgfdssdfghjkl;lkjfrtyui'


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://root:JwKICk8Jn7PiPeGcfVB1BPjY@gina.iran.liara.ir:30157/postgres"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(Config.BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
