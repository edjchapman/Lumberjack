from .vars import BASE_DIR

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ["templates/staticfiles"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
