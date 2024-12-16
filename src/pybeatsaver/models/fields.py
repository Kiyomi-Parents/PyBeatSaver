from dateutil import parser
from dataclasses import field, Field
from datetime import datetime
from typing import *

from dataclasses_json import config
from marshmallow import fields

def value_is_none(value: Any) -> bool:
    return value is None

def datetime_encoder_iso(dt: Optional[datetime]) -> Optional[str]:
    return dt.isoformat() if dt is not None else None

def datetime_decoder_iso(iso_string: Optional[str]) -> Optional[datetime]:
    return parser.isoparse(iso_string) if iso_string is not None else None

def datetime_field(json_field_name: Optional[str] = None) -> Field:
    if json_field_name is None:
        conf = config(
            encoder=datetime_encoder_iso,
            decoder=datetime_decoder_iso,
            mm_field=fields.DateTime(format='iso'),
            exclude=value_is_none
        )
    else:
        conf = config(
            encoder=datetime_encoder_iso,
            decoder=datetime_decoder_iso,
            mm_field=fields.DateTime(format='iso'),
            field_name=json_field_name,
            exclude=value_is_none
        )

    return field(default=None, metadata=conf)


def default(json_field_name: Optional[str] = None) -> Field:
    if json_field_name is None:
        conf = config(
            exclude=value_is_none
        )
    else:
        conf = config(
            field_name=json_field_name,
            exclude=value_is_none
        )

    return field(default=None, metadata=conf)