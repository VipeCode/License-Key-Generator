import random, string

alphabet = string.ascii_uppercase + string.digits

def verify(key):
    return (len(key) == 29) and (key.count(key[7]) == 3) and (key.count("-") == 4)

def generate():
    random_positions = [0, 1, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28]
    id_char = "".join(random.choice(alphabet))
    temp_alphabet = alphabet.replace(id_char, "")
    while True:
        key = ""
        for x in range(5):
            block = ''.join(random.choices(temp_alphabet, k=5))
            if len(key) > 0 and len(key) < 29:
                key = key + "-" + block
            else:
                key = key + block

        l = list(key)
        l[7] = id_char
        key = "".join(l)

        for x in range(2):
            pos = random.choice(random_positions)
            random_positions = [x for x in random_positions if x != pos]
            l = list(key)
            l[pos] = id_char
            key = "".join(l)

        if verify(key):
            return key

print(generate())