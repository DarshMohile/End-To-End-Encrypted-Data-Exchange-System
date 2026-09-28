from pathlib import Path


def create_avalanche(input_file_path:Path) -> Path:
    
    avalanche_file_path = Path("./data/source/avalanche_access_log.log")

    with open(input_file_path, "rb") as input_file:
        data = bytearray(input_file.read())


    avalanche = data.copy()
    avalanche[0] ^= 0x01


    with open(avalanche_file_path, "wb") as avalanche_file:
        avalanche_file.write(avalanche)

    return avalanche_file_path