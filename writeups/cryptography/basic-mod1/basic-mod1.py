message = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
decrypted = ""

for num in message:
    num %= 37
    if num < 26:
        decrypted += chr(num + ord('A'))
    elif num < 36:
        decrypted += str(num - 26)
    else:
        decrypted += "_"

flag = "picoCTF{" + decrypted + "}"
print(flag)
