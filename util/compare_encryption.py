from pathlib import Path

def compare_enc(pre_avalanche_file:Path, post_avalanche_file:Path) -> dict:

    with open(pre_avalanche_file, "rb") as pre_avalanche_file:
        pre_avalanche_data = pre_avalanche_file.read()

    with open(post_avalanche_file, "rb") as post_avalanche_file:
        post_avalanche_data = post_avalanche_file.read()


    different_bits = sum((a ^ b).bit_count() for a, b in zip(pre_avalanche_data, post_avalanche_data))
    percentage = (different_bits / (len(pre_avalanche_data) * 8)) * 100


    return {
        "different_bits":different_bits,
        "difference_percentage": percentage
    }