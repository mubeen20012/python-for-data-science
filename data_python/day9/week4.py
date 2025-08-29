#Week 4 Problem Set – Practice Problems
"""def main():
    text=input("Text: ").strip()
    print(f"Output:{emoji(text)}")
def emoji(text):
    text=text.replace(":)","😄")
    text=text.replace(":(","😢")
    return text
main()
"""

"""from emoji import emojize
def emoji():
    emoji=input("Enter Emoji: ").strip()
    print(emojize(emoji,language='alias'))
    
emoji()"""
# Ask the user for a single letter
letter = input("Enter a single letter: ").strip().lower()

# Validate input
if len(letter) != 1 or not letter.isalpha():
    print("Invalid input! Please enter exactly one letter.")
else:
    # Ask the user for a word
    word = input("Enter a word: ").strip().lower()
    
    # Check if the letter is in the word
    if letter in word:
        print(True)
    else:
        print(False)
