from pathlib import Path

from django.conf import settings as django_settings
from whitenoise.middleware import WhiteNoiseMiddleware

from website.media_files import hydrate_media


class PrefWhiteNoiseMiddleware(WhiteNoiseMiddleware):
    """Serve uploaded media from MEDIA_ROOT in production as well as static files."""

    def __init__(self, get_response=None, settings=django_settings):
        hydrate_media()
        super().__init__(get_response, settings)
        media_root = getattr(settings, "MEDIA_ROOT", None)
        media_url = getattr(settings, "MEDIA_URL", "")
        if media_root and media_url and Path(media_root).is_dir():
            self.add_files(str(media_root), prefix=media_url)
