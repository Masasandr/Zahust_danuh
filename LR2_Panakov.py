import sys
import math

def shift_text(text, shift_amount):
    shifted_text = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            shifted_text.append(new_char)
        else:
            shifted_text.append(char)
    return ''.join(shifted_text)

def english_text_probability(text):
    letter_probabilities = {
        0: 8.08, 1: 1.67, 2: 3.18, 3: 3.99, 4: 12.56, 5: 2.17,
        6: 1.80, 7: 5.27, 8: 7.24, 9: 0.14, 10: 0.63, 11: 4.04,
        12: 2.60, 13: 7.38, 14: 7.47, 15: 1.91, 16: 0.09, 17: 6.42,
        18: 6.59, 19: 9.15, 20: 2.79, 21: 1.00, 22: 1.89, 23: 0.21,
        24: 1.65, 25: 0.07
    }
    frequencies = [0] * 26
    text = text.lower()
    
    for char in text:
        index = ord(char) - ord('a')
        if 0 <= index < 26:
            frequencies[index] += 1
            
    total_length = len(text)
    score = 0.0
    
    for i in range(26):
        percentage = (frequencies[i] / total_length) * 100 if total_length > 0 else 0
        score += (letter_probabilities[i] - percentage) ** 2
        
    return math.sqrt(score)


message = input()

min_score = sys.maxsize
best_decoded_text = ""

for shift in range(26):
    candidate_text = shift_text(message, shift)
    current_score = english_text_probability(candidate_text)
    if current_score < min_score:
        min_score = current_score
        best_decoded_text = candidate_text

print(best_decoded_text)