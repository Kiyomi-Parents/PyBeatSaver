from .base_enum import BaseEnum


class EMapState(BaseEnum):
    UPLOADED = "Uploaded"
    TESTPLAY = "Testplay"
    PUBLISHED = "Published"
    FEEDBACK = "Feedback"
    SCHEDULED = "Scheduled"
