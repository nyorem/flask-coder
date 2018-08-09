import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, "static")

class Config:
    # flatpages
    FLATPAGES_ROOT = "content"
    FLATPAGES_EXTENSION = ".md"

    # paginate
    PER_PAGE = 10
