from .human_enum import HumanEnum


class ECharacteristic(HumanEnum):
    STANDARD = "Standard"
    ONE_SABER = "OneSaber"
    NO_ARROWS = "NoArrows"
    DEGREE_90 = "_90Degree"
    DEGREE_360 = "_360Degree"
    LIGHTSHOW = "Lightshow"
    LAWLESS = "Lawless"

    def human_readable(self) -> str:
        return self.value.remove("_")

    @property
    def api_request_value(self) -> str:
        return self.human_readable()
