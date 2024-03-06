import random

from utils.programming_words import programming_words
from utils.inser_dashes import inser_dashes
from utils.logger import logger
from utils.find_index import find_index

def main():
  # 1. Choosing the category and word to be discovered
  c_categories = list(programming_words.keys())
  c_category_idx = random.randrange(len(c_categories))

  c_category_name = c_categories[c_category_idx]
  c_category_words = programming_words.get(c_category_name)

  print(f'The word is from category: {c_category_name}\n')

  # 2. Hiding the chosen word
  c_word_in_category_idx = random.randrange(len(c_category_words))
  c_keyword_preview = c_category_words[c_word_in_category_idx]

  c_hidden_word_letters = []

  for current_letter in c_keyword_preview:
    c_hidden_word_letters.append(current_letter.lower())

  hidden_letter_mapper = list(map(inser_dashes, tuple(c_hidden_word_letters)))

  # 3. Game execution
  print(c_keyword_preview)
  player_life = 5

  while player_life > 0:
    hidden_word_preview = ''.join(hidden_letter_mapper)

    if (hidden_word_preview == c_keyword_preview.lower()):
      logger['success'](f'\n🏆 Congratulations, the correct word is {c_keyword_preview}.')
      break

    print(hidden_word_preview)
    player_response = input('\nYour guess is: ')

    if (player_response not in c_hidden_word_letters):
      player_life -= 1
      logger['error'](f'The letter {player_response} is not present in this word. Try again.')
    else:
      c_letters_idx = find_index(lambda value: value == player_response, c_hidden_word_letters)

      for letter_idx in c_letters_idx:
        hidden_letter_mapper[letter_idx] = player_response


if (__name__ == '__main__'):
  main()
