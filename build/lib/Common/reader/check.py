import os
import struct


def check_parquet_file(filepath):
    with open(filepath, 'rb') as f:
        f.seek(-4, os.SEEK_END)  # Go to the last 4 bytes of the file
        magic_number = f.read()
    return struct.unpack('4s', magic_number)[0] == b'PAR1'


file_path = r"C:\Users\ahafsi\project beta\myfiles\.part-00002-18a6b474-33f8-43a8-acc3-bfd6fab2b46e-c000.snappy.parquet.crc"
print(check_parquet_file(file_path)) 
