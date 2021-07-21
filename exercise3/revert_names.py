"""
Exercise 3
Devise the necessary code in any language to receive from prompt your First and Last names
separated by a space and return it as a complete reverse string. Example: John Doe -> eoD nhoJ.
"""
import traceback
from exercise3.invalid_sequence_of_names_exception import InvalidSequenceOfNamesException


def reverse_string(string_to_reverse):
    if is_valid_sequence_of_words(string_to_reverse):
        return string_to_reverse[::-1]
    else:
        raise InvalidSequenceOfNamesException("This sequence of names is invalid!")


def is_valid_sequence_of_words(sequence_of_words):
    list_of_words = sequence_of_words.split(" ")
    return sequence_of_words.replace(' ', '').isalpha() and len(list_of_words) == 2 and "" not in list_of_words


if __name__ == '__main__':
    first_and_last_names = input("Type your first and last names separated by spaces: ")

    try:
        reversed_names = reverse_string(first_and_last_names)
        print(reversed_names)
    except InvalidSequenceOfNamesException as error:
        print(error)
    except Exception:
        traceback.print_exc()
