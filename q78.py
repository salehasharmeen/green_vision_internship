from collections import Counter
import re

song_lyrics = input("Enter the lyrics of the song: ")
cleaned_lyrics = re.sub(r'[^\w\s]', '', song_lyrics.lower())
words = cleaned_lyrics.split()
word_count = Counter(words)
most_common_word, most_common_count = word_count.most_common(1)[0]

print(f"The most used word is '{most_common_word}' with {most_common_count} occurrences.")
