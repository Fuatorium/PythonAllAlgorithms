def rle_encode(data):
    encoding = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoding += str(count) + data[i]
        i += 1
    return encoding

def rle_decode(data):
    decode = ""
    i = 0
    while i < len(data):
        count = int(data[i])
        i += 1
        decode += data[i] * count
        i += 1
    return decode

if __name__ == "__main__":
    data = "AAABBBCCDAA"
    encoded_data = rle_encode(data)
    print(f"Encoded: {encoded_data}")
    decoded_data = rle_decode(encoded_data)
    print(f"Decoded: {decoded_data}")
