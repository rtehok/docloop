class Config:
    UPLOAD_FOLDER = 'uploads'
    IMAGES_FOLDER = 'images'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
