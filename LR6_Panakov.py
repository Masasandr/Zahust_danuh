def scanner(qrcode):
    qr_code_indices = [[0 for _ in range(21)] for _ in range(21)]
    
    for i, row in enumerate(qrcode):
        for j, val in enumerate(row):
            if (i + j) % 2 == 0:
                val = 1 - val
            qr_code_indices[i][j] = val

    # Зрізаємо перші 9 рядків
    qr_code = qr_code_indices[9:]

    odd, output = 0, []
    
    for i in [19, 17, 15, 13]:
        # Витягуємо дві колонки
        columns = [row[i:i + 2] for row in qr_code]

        # Визначаємо напрямок
        direction = 1 if odd == 1 else -1
        
        # Додаємо рядки в output
        for row in columns[::direction]:
            output.extend(row[::-1])
        
        odd = 1 - odd

    output = ''.join(map(str, output[4:]))
    letter_count = int(output[:8], 2)
    output = output[8:]
    
    word = ''
    print(letter_count)
    
    for i in range(0, (letter_count * 8) + 11, 8):
        word += chr(int(output[i:i + 8], 2))
        if len(word) == letter_count:
            return word

# Приклад використання
qrcode = [
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    # Додайте інші рядки тут
]
result = scanner(qrcode)
print(result)