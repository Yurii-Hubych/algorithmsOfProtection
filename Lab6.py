#Функція для зчитування з файлу таблиці-ключа
def load_key_table_from_file(filename):
    key_table = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            row = line.strip().split(" ")
            key_table.append(row)
    return key_table

def create_key_table():
    key_table = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'І', 'Ї'],
        ['К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф'],
        ['Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я', 'Є', 'Й', 'Ґ']
    ]
    return key_table

# Функція для зчитування з файлу зашифрованого тексту
def load_encripted_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
     return file.read()

# Функція для дешифрування тексту
def playfair_decrypt(ciphertext, key_table):
    plaintext = ''
    ciphertext = ciphertext.replace(' ', '').upper()  # Видалення пробілів та переведення в верхній регістр

    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i + 2]
        row1, col1 = None, None
        row2, col2 = None, None

        for row in range(len(key_table)):
            if pair[0] in key_table[row]:
                row1, col1 = row, key_table[row].index(pair[0])
            if pair[1] in key_table[row]:
                row2, col2 = row, key_table[row].index(pair[1])

        if row1 == row2:  # Правило 2: літери в одному рядку
            col1 = (col1 - 1) % len(key_table[row1])
            col2 = (col2 - 1) % len(key_table[row2])
        elif col1 == col2:  # Правило 3: літери в одному стовпці
            row1 = (row1 - 1) % len(key_table)
            row2 = (row2 - 1) % len(key_table)
        else:  # Правило 1: літери у різних рядках і стовпцях
            # Зберігаємо той самий порядок, але змінюємо стовпці
            col1, col2 = col2, col1

        plaintext += key_table[row1][col1] + key_table[row2][col2]

    return plaintext


def main():
    key_table = load_key_table_from_file("../Lab5/key_table.txt")
    ciphertext = load_encripted_text_from_file("../Lab5/cryptogram.txt")
    decrypted_text = playfair_decrypt(ciphertext, key_table)
    print(f"Розшифрований текст: {decrypted_text}")

if __name__=="__main__":
    main()