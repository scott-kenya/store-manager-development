import os


class config(object):
	DEBUG = False
	#CSRF_ENABLED - Trues
	SECRET = os.getenv('secret')


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(config):
	DEBUG = True

class TestingConfig(config):
	DEBUG = True
	TESTING = True

class StagingConfig(config):
	DEBUG = False
	TESTING = False

class ProductionConfig(config):
	DEBUG = False
	TESTING = False


app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig				
}
