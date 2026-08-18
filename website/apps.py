from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "website"
    verbose_name = "Prefequity website"

    def ready(self):
        from .media_files import hydrate_media

        hydrate_media()
