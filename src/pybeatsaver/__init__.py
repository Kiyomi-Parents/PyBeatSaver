import logging

from .beatsaver import BeatSaver
from .beatsaver_api import BeatSaverAPI
from .beatsaver_provider import BeatSaverProvider
from .errors import *
from .models import *

handler = logging.StreamHandler()
logging.getLogger("PyBeatSaver").addHandler(handler)
