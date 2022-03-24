from dateutil import parser
from dataclasses import field, Field
from datetime import datetime
from typing import *

from dataclasses_json import config
from marshmallow import fields

from .enum import ECharacteristic, EDifficulty, EAccountType


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


def characteristic_decoder(value: any) -> ECharacteristic:
    if value == "360Degree":
        return ECharacteristic.DEGREE_360
    elif value == "90Degree":
        return ECharacteristic.DEGREE_90

    if ECharacteristic.has_value(value):
        return ECharacteristic(value)

    raise RuntimeError(f"Could not convert value {value} to ECharacteristic")


def characteristic_encoder(characteristic: ECharacteristic) -> str:
    return characteristic.value


def characteristic_field(json_field_name: Optional[str] = None) -> Field:
    return field(
        default=None,
        metadata=config(
            encoder=characteristic_encoder,
            decoder=characteristic_decoder,
            field_name=json_field_name
        )
    )


def difficulty_decoder(value: any) -> EDifficulty:
    if EDifficulty.has_value(value):
        return EDifficulty(value)

    raise RuntimeError(f"Could not convert value {value} to EDifficulty")


def difficulty_encoder(difficulty: EDifficulty) -> int:
    return difficulty.value


def difficulty_field(json_field_name: Optional[str] = None) -> Field:
    return field(
        default=None,
        metadata=config(
            encoder=difficulty_encoder,
            decoder=difficulty_decoder,
            field_name=json_field_name
        )
    )


def account_type_decoder(value: any) -> EAccountType:
    if EAccountType.has_value(value):
        return EAccountType(value)

    return EAccountType.UNKNOWN


def account_type_encoder(account_type: EAccountType) -> int:
    return account_type.value


def account_type_field(json_field_name: Optional[str] = None) -> Field:
    return field(
        default=None,
        metadata=config(
            encoder=account_type_encoder,
            decoder=account_type_decoder,
            field_name=json_field_name
        )
    )
