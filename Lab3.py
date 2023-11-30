import re
import collections

alphabet = {
    " " : [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
    "а" : [115, 116, 117, 118, 119, 120],
    "б" : [121, 122],
    "в" : [123, 124, 125, 126],
    "г" : [127, 128],
    "ґ" : [129],
    "д" : [130, 131, 132],
    "е" : [133, 134, 135, 136],
    "є" : [137],
    "ж" : [138],
    "з" : [139, 140],
    "и" : [141, 142, 143, 144, 145],
    "і" : [146, 147, 148, 149],
    "ї" : [150],
    "й" : [151],
    "к" : [152],
    "л" : [153, 154, 155],
    "м" : [156, 157, 158],
    "н" : [159, 160, 161, 162, 163, 164],
    "о" : [165, 166, 167, 168, 169, 170, 171, 172],
    "п" : [173, 174],
    "р" : [179, 180, 181, 182],
    "с" : [183, 184, 185, 186],
    "т" : [187, 188, 189, 190],
    "у" : [191, 192, 193],
    "ф" : [194],
    "х" : [195],
    "ц" : [196],
    "ч" : [197],
    "ш" : [198],
    "щ" : [199],
    "ь" : [200, 201],
    "ю" : [202],
    "я" : [203]
}

def decryption(text):
    decryptedText = ""
    count_dict = collections.Counter(int(text[i:i + 3]) for i in range(0, len(text), 3))
    for i in range(0, len(text), 3):
        number = int(text[i:i + 3])
        for letter, numbers in alphabet.items():
            if number in numbers:
                decryptedText += letter

    total = sum(count_dict.values())
    count_dict = sorted(count_dict.items(), key=lambda x: x[0])
    for number, count in count_dict:
        print("Елемент:", number, " | Кількість:", count, " | (", count / total * 100, "%)", sep="")

    return decryptedText

def count_letters_and_spaces(text):
    letters = re.findall(r"[а-яА-Я]", text)
    spaces = re.findall(r"\s", text)
    d = {}
    for letter in letters:
        d[letter] = d.get(letter, 0) + 1
    for space in spaces:
        d[space] = d.get(space, 0) + 1
    return d

with open("../Lab2/write.txt", "r", encoding="utf-8") as f:
    encryptedText = f.read()

print(encryptedText)
decryptedText = decryption(encryptedText)
print(decryptedText)

d = count_letters_and_spaces(decryptedText)
print("Таблиця кількості кожної букви та пробілів:")
print("| Елемент | Кількість |")
print("|---|---|---|")
for letter, count in d.items():
    count = count * 34 / 100
    print("|", letter, "|", count, "|")