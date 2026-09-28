from encryption.aes_encryption import init_AES
from encryption.des_encryption import init_DES
from util.avalanche import create_avalanche
from util.compare_encryption import compare_enc
from Crypto.Random import get_random_bytes
from pathlib import Path


ip_file_path = Path("./data/source/access_log.log")
src_img_path = Path("./data/source/cat.jpg")


# Initialize AES key, block size(aka iv)
aes_key = get_random_bytes(16)      # 128-bit Key
aes_iv = get_random_bytes(16)       # 128-bit block
    
print(f"\nAES/> Generated AES Encryption Key: {str(aes_key.hex())}")  # print generated key for AES
print(f"AES/> Key Length: {str(len(aes_key) * 8)} bits")            # print length of key in bits


# Initialize DES key, block size(aka iv)
des_key = get_random_bytes(8)      # 64-bit Key
des_iv = get_random_bytes(8)       # 64-bit block (block = total )

print(f"\nDES/> Generated DES Encryption Key: {str(des_key.hex())}")    # print generated key for DES
print(f"DES/> Key Length: {str(len(des_key) * 8)} bits")          # print length of key in bits



print("\n/> Enryption of NORMAL FILE")
aes_output = init_AES(ip_file_path, aes_key, aes_iv, avalanche=False, mode=0)
des_output = init_DES(ip_file_path, des_key, des_iv, avalanche=False, mode=0)


print("\n/> Generating Avalanche Effect in original file")
avalanche_file_path = create_avalanche(ip_file_path)


print("\n\n/> Enryption of AVALANCHE FILE")
avalanche_aes_output = init_AES(avalanche_file_path, aes_key, aes_iv, avalanche=True, mode=0)
avalanche_des_output = init_DES(avalanche_file_path, des_key, des_iv, avalanche=True, mode=0)


print("\n/> Comparing encryption of both files")
result_aes = compare_enc(aes_output, avalanche_aes_output)
result_des = compare_enc(des_output, avalanche_des_output)

print(f"AES/> Bit Difference in avalanche VS original file: {result_aes['different_bits']}")
print(f"AES/> Bit Difference in avalanche VS original file (%): {result_aes['difference_percentage']}")

print(f"\nDES/> Bit Difference in avalanche VS original file: {result_des['different_bits']}")
print(f"DES/> Bit Difference in avalanche VS original file (%): {result_des['difference_percentage']}\n")


# Image encryption
print("\n/> Enryption of Image using ECB and CBC methods")
aes_output = init_AES(src_img_path, aes_key, aes_iv, avalanche=False, mode=1)
aes_output = init_AES(src_img_path, aes_key, aes_iv, avalanche=False, mode=0)