def encode_Lee(input_string):
    """
    IPA 변환함수. 대응관계는 다음과 같다.\n
    E -> ə\n
    U -> ü\n
    O -> ö\n
    A -> ɛ\n
    I -> ɜ\n
    Z -> ʐ\n
    G -> ŋ\n
    """
    new_string = ''
    for char in input_string:
        if char == 'E':
            new_string += 'ə'
        elif char == 'U':
            new_string += 'ü'
        elif char == 'O':
            new_string += 'ö'
        elif char == 'A':
            new_string += 'ɛ'
        elif char == 'I':
            new_string += 'ɜ'
        elif char == 'Z':
            new_string += 'ʐ'
        elif char == 'G':
            new_string += 'ŋ'
        else:
            new_string += char
    
    return new_string