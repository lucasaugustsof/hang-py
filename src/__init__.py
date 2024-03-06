import random

from utils.programming_words import programming_words
from utils.inser_dashes import inser_dashes
from utils.find_index import find_index
from utils.logger import logger

class Game:
  def __init__(self):
    self.player_life = 6

  def get_word_category(self):
    c_categories = list(programming_words.keys())
    c_category_idx = random.randrange(len(c_categories))

    c_category_name = c_categories[c_category_idx]

    return c_category_name

  def get_keyword(self, category_name):
    c_category_words = programming_words.get(category_name)

    c_word_in_category_idx = random.randrange(len(c_category_words))
    c_keyword = c_category_words[c_word_in_category_idx].upper()

    return c_keyword

  def get_mapped_letters_keyword(self, keyword):
    c_keyword_letters = []

    for current_letter in keyword:
      c_keyword_letters.append(str(current_letter).upper())

    return c_keyword_letters

  def execute(self):
    c_keyword_category = self.get_word_category()
    print(f'The word is from category: {c_keyword_category}\n')

    c_keyword_preview = self.get_keyword(c_keyword_category)
    c_mapped_letters_keyword = self.get_mapped_letters_keyword(c_keyword_preview)

    hidden_letter_mapper = list(map(inser_dashes, tuple(c_mapped_letters_keyword)))

    while self.player_life > 0:
      hidden_word_preview = str().join(hidden_letter_mapper)
      print(hidden_word_preview)

      if (hidden_word_preview == c_keyword_preview):
        logger['success'](f'\n🏆 Congratulations, the correct word is {c_keyword_preview}.')
        break

      player_response = input('\nYour guess is: ').upper()
      quantity_letters_answer = len(player_response)

      if quantity_letters_answer < 0 or quantity_letters_answer > 1:
        continue

      if player_response in hidden_letter_mapper:
        logger['warn']('This letter has already been added.')

      elif (player_response not in c_mapped_letters_keyword):
        self.player_life -= 1
        logger['error'](
          f'The letter {player_response} is not present in the hidden word. Now you have {self.player_life} lives...'
        )

      else:
        c_letters_idx = find_index(lambda value: value == player_response, c_mapped_letters_keyword)

        for letter_idx in c_letters_idx:
          hidden_letter_mapper[letter_idx] = player_response


if (__name__ == '__main__'):
  Game().execute()
