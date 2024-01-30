# Define vowels
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

# Read the file and store each line in an array
with open('pg2701.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Flag to indicate if counting should start
start_counting = False
total_consonants = 0
total_words = 0

# Iterate over each line in the array
for line in lines:
    # Check if the line starts with the marker
    if line.startswith("CHAPTER 1. Loomings."):
        start_counting = True
        continue

    # Count consonants for each word
    if start_counting:
        words = line.split()
        for word in words:
            word_consonants = 0
            for char in word:
                # Consider only alphabetic characters
                if char.isalpha():
                    # Convert to lowercase for comparison
                    char_lower = char.lower()
                    # Check if the character is a consonant
                    if char_lower not in vowels:
                        word_consonants += 1
            total_consonants += word_consonants
            total_words += 1

# Calculate the average number of consonants per word
if total_words != 0:
    average_consonants_per_word = total_consonants / total_words
else:
    average_consonants_per_word = 0

print(f'Average number of consonants per word: {average_consonants_per_word: .2f}')
