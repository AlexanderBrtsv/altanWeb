from hashlib import sha256

def hashing(pwd: str, salt: str, num_char: str='-') -> str:
    # кодирование
    str_sum = pwd + salt
    byte_str = str_sum.encode()
    # хеширование
    hash_str = sha256(byte_str)
    # преобразование в hex-строку
    # if num_char == '-':
    #     hex_str = hash_str.hexdigest()
    # else:
    #     hex_str = hash_str.hexdigest()[:int(num_char)]
    hex_str = hash_str.hexdigest()
    if num_char != '-':
        hex_str = hex_str[:int(num_char)]
        return hex_str
    # возврат значения
    return hex_str