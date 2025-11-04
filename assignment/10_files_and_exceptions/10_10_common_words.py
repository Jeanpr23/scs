# 10_10_common_words.py

filename = "sample_text.txt"

try:
    with open(filename) as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
