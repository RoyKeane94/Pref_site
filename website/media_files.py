from pathlib import Path
import os
import shutil

from django.conf import settings


def bundled_media_root():
    """Directory of committed uploads that survive a volume mount over MEDIA_ROOT."""
    configured = os.environ.get("MEDIA_BUNDLE_ROOT", "").strip()
    candidates = []
    if configured:
        candidates.append(Path(configured))
    candidates.extend(
        [
            Path(settings.BASE_DIR) / "media_bundle",
            Path(settings.BASE_DIR) / "media",
        ]
    )
    for candidate in candidates:
        if candidate.is_dir() and any(candidate.iterdir()):
            return candidate
    return None


def hydrate_media(destination=None):
    """Copy bundled uploads into MEDIA_ROOT when the destination is missing files.

    Railway volumes mounted at /app/media hide the files baked into the image.
    A build-time copy in media_bundle stays readable, so production can restore
    logos and article images onto the volume without overwriting newer uploads.
    """
    source = bundled_media_root()
    dest = Path(destination or settings.MEDIA_ROOT)
    dest.mkdir(parents=True, exist_ok=True)
    if source is None or source.resolve() == dest.resolve():
        return 0

    copied = 0
    for src_file in source.rglob("*"):
        if not src_file.is_file():
            continue
        dest_file = dest / src_file.relative_to(source)
        if dest_file.exists():
            continue
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dest_file)
        copied += 1
    return copied
