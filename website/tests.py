from pathlib import Path
from tempfile import TemporaryDirectory

from django.conf import settings
from django.test import SimpleTestCase, override_settings

from website.media_files import hydrate_media


class MediaServingTests(SimpleTestCase):
    logo_path = "/media/portfolio/logos/NOWEducationAdjustedLogo.webp"
    article_path = "/media/news/Ilektra_banner.webp"

    def test_committed_logo_is_served_when_debug_is_off(self):
        with override_settings(DEBUG=False):
            response = self.client.get(self.logo_path)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response["Content-Type"].startswith("image/"))

    def test_committed_article_image_is_served_when_debug_is_off(self):
        with override_settings(DEBUG=False):
            response = self.client.get(self.article_path)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response["Content-Type"].startswith("image/"))

    def test_missing_media_file_returns_404(self):
        response = self.client.get("/media/does-not-exist.webp")
        self.assertEqual(response.status_code, 404)

    def test_hydrate_copies_missing_files_without_overwriting(self):
        source = Path(settings.BASE_DIR) / "media"
        self.assertTrue((source / "portfolio" / "logos" / "NOWEducationAdjustedLogo.webp").exists())

        with TemporaryDirectory() as raw_dest:
            dest = Path(raw_dest)
            existing = dest / "keep-me.txt"
            existing.write_text("local-upload", encoding="utf-8")

            copied = hydrate_media(destination=dest)

            self.assertGreater(copied, 0)
            self.assertTrue(
                (dest / "portfolio" / "logos" / "NOWEducationAdjustedLogo.webp").exists()
            )
            self.assertEqual(existing.read_text(encoding="utf-8"), "local-upload")
            self.assertEqual(hydrate_media(destination=dest), 0)
