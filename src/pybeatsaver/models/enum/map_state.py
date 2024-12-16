from enum import Enum


class EMapState(Enum):
    UPLOADED = "Uploaded"
    TESTPLAY = "Testplay"
    PUBLISHED = "Published"
    FEEDBACK = "Feedback"
    SCHEDULED = "Scheduled"
