from Crypto.Cipher import AES
from pathlib import Path


def init_img_AES(input_file_path: Path, aes_key: bytes, aes_iv: bytes, mode: int) -> Path:

    if(mode == 0):
        aes_cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        mode_name = "CBC"
    else:
        aes_cipher = AES.new(aes_key, AES.MODE_ECB)
        mode_name = "ECB"

    output_file_path = Path(f"./data/encrypted/encrypted_image_{mode_name}.bmp")

    with open(input_file_path, "rb") as input_file:
        data = input_file.read()

    # Location of BMP pixel data
    pixel_offset = int.from_bytes(data[10:14], byteorder="little")

    header = data[:pixel_offset]
    pixel_data = data[pixel_offset:]

    # Only encrypt complete AES blocks
    encrypted_length = (len(pixel_data) // AES.block_size) * AES.block_size

    data_to_encrypt = pixel_data[:encrypted_length]
    remaining_data = pixel_data[encrypted_length:]

    encrypted_data = aes_cipher.encrypt(data_to_encrypt)

    with open(output_file_path, "wb") as output_file:
        output_file.write(header)
        output_file.write(encrypted_data)
        output_file.write(remaining_data)

    print(f"AES/{mode_name} encryption done.")
    print(f"Output: {output_file_path}")

    return output_file_path