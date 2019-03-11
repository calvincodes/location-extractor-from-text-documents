import re
from examples import Examples
from constants import blacklist_words
from nltk.corpus import wordnet as wn

positive_feature_vector = []
negative_feature_vector = []


def generate_examples(word_list):
    lowered_blacklisted_words = [x.lower() for x in blacklist_words]
    examples = Examples()

    for i, word in enumerate(word_list):

        # TODO: Remove this commented redundant code post confirmation.
        # We should NOT be needing these. We have not tagged this.
        # word = re.sub("\'s", "", word)
        # word = re.sub("\’s", "", word)

        # As "loc" can commonly occur even in normal words like al'loc'ation, hence checking for presence of <loc>
        if '<loc>' in word:
            # For the same reason as above, explicitly checking for one occurrence of both opening and closing tags.
            if word.count("<loc>") == 1 and word.count("</loc>") == 1:
                extracted_word = re.sub('<[^>]*>', '', word)
                examples.positive.append([i, extracted_word])
            else:
                # If the label spans across multiple words, like <loc>United States of America</loc>.
                # Iterate till we find the closing tag.
                for tag_closing_index in range(i, len(word_list)):
                    if word_list[tag_closing_index].count("</loc>") == 1:
                        tagged_substring_list = word_list[i:tag_closing_index + 1]
                        tagged_substring = ''.join(str(e + " ") for e in tagged_substring_list)
                        extracted_word = re.sub('<[^>]*>', '', tagged_substring).strip()
                        examples.positive.append([i, extracted_word])
                        for x in range(i + 1, tag_closing_index + 1):
                            word_list[x] = "__"
                        break
        else:
            # **************** Create uni-gram examples ****************
            # Only the words with first letter upper, and not in the rule list will be used for uni-gram formation.
            # The formation of bi-gram will be on the basis of the second word. If second word is not loc
            # and is not a rule word, then the bi-gram is created.
            if i < len(word_list) - 1 and word[0].isupper():
                dictionary = wn.synsets(word_list[i + 1])
                if len(dictionary) > 0 and dictionary[0].pos() == 'v':
                    examples.negative.append([i, word + " " + word_list[i + 1]])
                elif i < len(word_list) - 2:
                    dictionary = wn.synsets(word_list[i + 2])
                    if len(dictionary) > 0 and dictionary[0].pos() == 'v':
                        examples.negative.append([i, word + " " + word_list[i + 1] + " " + word_list[i + 2]])

            # Handling months like my birthday is in July.
            if word[0].isupper() and (word in lowered_blacklisted_words or word[0:-1] in lowered_blacklisted_words):
                examples.negative.append(i)

    return examples
