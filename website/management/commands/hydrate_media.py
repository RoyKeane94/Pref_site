from django.core.management.base import BaseCommand

from website.media_files import bundled_media_root, hydrate_media


class Command(BaseCommand):
    help = "Copy bundled media files into MEDIA_ROOT if they are missing."

    def handle(self, *args, **options):
        source = bundled_media_root()
        copied = hydrate_media()
        if source is None:
            self.stdout.write(self.style.WARNING("No bundled media directory found."))
            return
        self.stdout.write(
            self.style.SUCCESS(f"Hydrated {copied} media file(s) from {source}.")
        )
