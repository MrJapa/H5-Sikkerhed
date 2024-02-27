import unittest

DANISH_FREQUENCIES = {
    'a': 6.01, 'b': 1.41, 'c': 0.29,'d': 7.24,'e': 16.70,'f': 2.27,'g': 4.56,'h': 1.88,'i': 5.55,
    'j': 1.11,'k': 3.07,'l': 4.85,'m': 3.40,'n': 7.55,'o': 4.14,'p': 1.33,'q': 0.01,'r': 7.61,'s': 5.67,
    't': 7.03,'u': 1.85,'v': 2.88,'w': 0.02,'x': 0.02,'y': 0.72,'z': 0.02,'æ': 0.93,'ø': 0.84, 'å': 1.03
}


def main():
    cæsar = input("Enter the text to be encrypted: ")
    ceasarResult = caesar(cæsar, 1)
    print("Ceasar Result: " + ceasarResult)
    hackerResult = hacker(ceasarResult)
    max_frequency = 0
    max_item = None
    for i in range(26):
        item = hackerResult[i]
        item_frequency = calculate_frequencies(item.lower())
        total_frequency = sum(item_frequency.get(letter, 0) * DANISH_FREQUENCIES.get(letter, 0) for letter in DANISH_FREQUENCIES)
        if total_frequency > max_frequency:
            max_frequency = total_frequency
            max_item = item
    print("Text with highest frequency: " + max_item)

def caesar(text, shift):
    result = ""
    for char in text:
        if char == ' ':
            result += char
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def hacker(text):
    results = []
    for i in range(26):
        result = ""
        for char in text:
            if char == ' ':
                result += char
            elif char.isupper():
                result += chr((ord(char) + i - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + i - 97) % 26 + 97)
            else:
                result += char
        results.append(result)
    return results

def calculate_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

    
class TestCaesar(unittest.TestCase):
    def test_caesar(self):
        self.assertEqual(caesar("HELLO WORLD", 3), "KHOOR ZRUOG")
        self.assertEqual(caesar("hello world", 3), "khoor zruog")
        self.assertEqual(caesar("Hello World", 3), "Khoor Zruog")
        self.assertEqual(caesar("abc xyz", 3), "def abc")

if __name__ == "__main__":
    main()
    #unittest.main()