import os

class Config:
    """Configuración base común para todas las configuraciones."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')  # Clave secreta para sesiones y seguridad
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # La URI de la base de datos

class DevelopmentConfig(Config):
    """Configuración específica para desarrollo."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_DEV', 'mysql://dev_user:dev_password@localhost/dev_db')  # URL para la base de datos de desarrollo

class ProductionConfig(Config):
    """Configuración específica para producción."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_PROD', 'mysql://prod_user:prod_password@localhost/prod_db')  # URL para la base de datos de producción

class TestingConfig(Config):
    """Configuración específica para pruebas."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST', 'mysql://test_user:test_password@localhost/test_db')  # URL para la base de datos de pruebas
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar para pruebas

# Mapeo de configuraciones
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
