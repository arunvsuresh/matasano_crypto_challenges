import binascii
def fixed_xor(s1, s2):
    decoded_s1 = s1.decode(encoding="hex")
    decoded_s2 = s2.decode(encoding="hex")
    int_rep_of_s1 = [ord(letter) for letter in decoded_s1]
    int_rep_of_s2 = [ord(letter) for letter in decoded_s2]

    res = []

    for i in range(len(int_rep_of_s1)):
        res.append(int_rep_of_s1[i] ^ int_rep_of_s2[i])

    res = "".join([chr(l) for l in res])

    return binascii.hexlify(res)
