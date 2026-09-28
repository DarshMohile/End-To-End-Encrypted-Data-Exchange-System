from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from pathlib import Path



def init_DES(input_file_path:Path, des_key:bytes, des_iv:bytes, avalanche:bool, mode:int) -> Path:
    
    # Initialize output file path
    if avalanche:
        output_file_path_des = Path("./data/encrypted/access_log_encrypted_avalanche.des")
    else:
        output_file_path_des = Path("./data/encrypted/access_log_encrypted.des")


    if(mode == 0):
        # Initialize main cipher object
        des_cipher = DES.new(des_key, DES.MODE_CBC, des_iv)

        if(input_file_path.suffix == ".jpg" or input_file_path.suffix == ".jpeg" or input_file_path.suffix == ".png"):
            output_file_path_des = Path("./data/encrypted/encrypted_image_CBC.des")
    else:
        des_cipher = DES.new(des_key, DES.MODE_ECB)
        
        if(input_file_path.suffix == ".jpg" or input_file_path.suffix == ".jpeg" or input_file_path.suffix == ".png"):
            output_file_path_des = Path("./data/encrypted/encrypted_image_ECB.des")


    # Read the input file
    with open(input_file_path, "rb") as input_file:
        data = input_file.read()


    # Encrypt the data we read from the file.
    des_encrypted = des_cipher.encrypt(pad(data, DES.block_size))   # Encrypt data from file using DES algo


    # Make / Overwrite a new encrypted file that contains DES Encryption
    with open(output_file_path_des, "wb") as output_file:
        output_file.write(des_encrypted)


    print("DES/> Encryption done.")

    return output_file_path_des