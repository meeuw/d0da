# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: d0da_report.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11\x64\x30\x64\x61_report.proto"}\n\nBrightness\x12$\n\x07payload\x18\x01 \x01(\x0b\x32\x13.Brightness.Payload\x1aI\n\x07Payload\x12\x12\n\nbrightness\x18\x01 \x01(\r\x12\t\n\x01\x61\x18\x02 \x01(\r\x12\t\n\x01\x62\x18\x03 \x01(\r\x12\t\n\x01\x63\x18\x04 \x01(\r\x12\t\n\x01\x64\x18\x05 \x01(\r"D\n\x07RGBRows\x12!\n\x07payload\x18\x01 \x03(\x0b\x32\x10.RGBRows.Payload\x1a\x16\n\x07Payload\x12\x0b\n\x03row\x18\x01 \x01(\x0c\x62\x06proto3'
)


_BRIGHTNESS = DESCRIPTOR.message_types_by_name["Brightness"]
_BRIGHTNESS_PAYLOAD = _BRIGHTNESS.nested_types_by_name["Payload"]
_RGBROWS = DESCRIPTOR.message_types_by_name["RGBRows"]
_RGBROWS_PAYLOAD = _RGBROWS.nested_types_by_name["Payload"]
Brightness = _reflection.GeneratedProtocolMessageType(
    "Brightness",
    (_message.Message,),
    {
        "Payload": _reflection.GeneratedProtocolMessageType(
            "Payload",
            (_message.Message,),
            {
                "DESCRIPTOR": _BRIGHTNESS_PAYLOAD,
                "__module__": "d0da_report_pb2"
                # @@protoc_insertion_point(class_scope:Brightness.Payload)
            },
        ),
        "DESCRIPTOR": _BRIGHTNESS,
        "__module__": "d0da_report_pb2"
        # @@protoc_insertion_point(class_scope:Brightness)
    },
)
_sym_db.RegisterMessage(Brightness)
_sym_db.RegisterMessage(Brightness.Payload)

RGBRows = _reflection.GeneratedProtocolMessageType(
    "RGBRows",
    (_message.Message,),
    {
        "Payload": _reflection.GeneratedProtocolMessageType(
            "Payload",
            (_message.Message,),
            {
                "DESCRIPTOR": _RGBROWS_PAYLOAD,
                "__module__": "d0da_report_pb2"
                # @@protoc_insertion_point(class_scope:RGBRows.Payload)
            },
        ),
        "DESCRIPTOR": _RGBROWS,
        "__module__": "d0da_report_pb2"
        # @@protoc_insertion_point(class_scope:RGBRows)
    },
)
_sym_db.RegisterMessage(RGBRows)
_sym_db.RegisterMessage(RGBRows.Payload)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BRIGHTNESS._serialized_start = 21
    _BRIGHTNESS._serialized_end = 146
    _BRIGHTNESS_PAYLOAD._serialized_start = 73
    _BRIGHTNESS_PAYLOAD._serialized_end = 146
    _RGBROWS._serialized_start = 148
    _RGBROWS._serialized_end = 216
    _RGBROWS_PAYLOAD._serialized_start = 194
    _RGBROWS_PAYLOAD._serialized_end = 216
# @@protoc_insertion_point(module_scope)