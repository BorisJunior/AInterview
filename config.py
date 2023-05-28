
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
