import os
import sys

sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "creative-cubes.settings"

#sys.path.insert(0, join(settings.DIRNAME, "apps"))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
