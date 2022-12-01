from django.apps import AppConfig


class FavouriteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favourite'

    def ready(self):
        import favourite.signals