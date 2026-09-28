from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from pathlib import Path
    

def init_AES(input_file_path:Path, aes_key:bytes, aes_iv:bytes, avalanche:bool, mode:int) -> Path:

    # Initialize output file path
    if(avalanche):
        output_file_path_aes = Path("./data/encrypted/access_log_encrypted_avalanche.aes")
    else:
        output_file_path_aes = Path("./data/encrypted/access_log_encrypted.aes")

    
    if(mode == 0):
        # Initialize main cipher object
        aes_cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)

        if(input_file_path.suffix == ".jpg" or input_file_path.suffix == ".jpeg" or input_file_path.suffix == ".png"):
            output_file_path_aes = Path("./data/encrypted/encrypted_image_CBC.jpg")
    else:
        aes_cipher = AES.new(aes_key, AES.MODE_ECB)

        if(input_file_path.suffix == ".jpg" or input_file_path.suffix == ".jpeg" or input_file_path.suffix == ".png"):
            output_file_path_aes = Path("./data/encrypted/encrypted_image_ECB.jpg")


    # Read the input file
    with open(input_file_path, "rb") as input_file:
        data = input_file.read()

    
    # Encrypt the data we read from the file.
    aes_encrypted = aes_cipher.encrypt(pad(data, AES.block_size))   # Encrypt data from file using AES algo


    # Make / Overwrite a new encrypted file that contains AES Encryption
    with open(output_file_path_aes, "wb") as output_file:
        output_file.write(aes_encrypted)

    print("AES/> Encryption done.")
    
    return output_file_path_aes