from django.apps import AppConfig


class CustomAuthenticationConfig(AppConfig):
    name = 'custom_authentication'

    def ready(self):
    	import custom_authentication.signals
