import logging

from .beatsaver import BeatSaver
from .errors import *
from .models import *

handler = logging.StreamHandler()
logging.getLogger("PyBeatSaver").addHandler(handler)
