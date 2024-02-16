from construct import Struct, Enum, Hex, Int8ul, Int32ul

filedate = Struct()

dcuformat = Struct(
    "major" / Hex(Int8ul),
    "platform" / Enum(Int8ul, win32=0),
    "minor" / Hex(Int8ul),
    "compiler" / Enum(Int8ul, delphi6=14),
    "size" / Int32ul,
    # "compiled" / Timestamp(Int32ul, "msdos", "msdos"), # Don't work correctly.
    "compiled" / Hex(Int32ul),
    "crc" / Hex(Int32ul),
)


def decompile(filename):
    print(f"Processing {filename}...")
    with open(filename, "rb") as f:
        dcu = dcuformat.parse_stream(f)
        print(dcu)
