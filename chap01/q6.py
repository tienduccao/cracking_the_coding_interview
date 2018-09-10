

def compress_string(text):
    compressed_string = ''
    counter = 0
    current_character = ''
    max_length = len(text)
    for ch in text:
        if ch == current_character:
            counter += 1
        else:
            if current_character != '':
                compressed_string += current_character + str(counter)
                if len(compressed_string) >= max_length:
                    return text
            current_character = ch
            counter = 1

    compressed_string += current_character + str(counter)

    if len(compressed_string) >= max_length:
        return text
    return compressed_string
