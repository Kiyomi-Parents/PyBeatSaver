from dateutil import parser
from dataclasses import field, Field
from datetime import datetime
from typing import *

from dataclasses_json import config
from marshmallow import fields

from .enum.base_enum import BaseEnum


def datetime_from_iso_format(time):
    if time:
        return parser.isoparse(time)

    return None


def datetime_field(json_field_name: Optional[str] = None) -> Field:
    if json_field_name is None:
        conf = config(
            encoder=datetime.isoformat,
            decoder=datetime_from_iso_format,
            mm_field=fields.DateTime(format='iso')
        )
    else:
        conf = config(
            encoder=datetime.isoformat,
            decoder=datetime_from_iso_format,
            mm_field=fields.DateTime(format='iso'),
            field_name=json_field_name,
        )

    return field(
        default=None,
        metadata=conf
    )


def default(json_field_name: Optional[str] = None) -> Field:
    if json_field_name is None:
        conf = config()
    else:
        conf = config(field_name=json_field_name)

    return field(
        default=None,
        metadata=conf
    )


T = TypeVar('T', bound=BaseEnum)


def get_enum_decoder(enum_type: Type[T]) -> Callable[[str], Optional[Union[T, List[T]]]]:
    def enum_decoder(value: Optional[Union[str, List[str]]]) -> Optional[Union[T, List[T]]]:
        if value is None:
            return None

        if isinstance(value, list):
            items = []

            for item in value:
                if enum_type.has_value(item):
                    items.append(enum_type.deserialize(item))

            return items

        if enum_type.has_value(value):
            return enum_type.deserialize(value)

        raise RuntimeError(f"Could not convert value {value} to {enum_type.__name__}")

    return enum_decoder


def get_enum_encoder() -> Callable[[T], str]:
    def enum_decoder(value: T) -> str:
        return value.serialize

    return enum_decoder


def enum_field(enum_type: Type[T], json_field_name: Optional[str] = None) -> field:
    return field(
        default=None,
        metadata=config(
            encoder=get_enum_encoder(),
            decoder=get_enum_decoder(enum_type),
            field_name=json_field_name
        )
    )
