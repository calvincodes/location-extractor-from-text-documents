import re
import random
from examples import Examples

# TODO: UPDATE THIS LIST OF BLACKLISTED RULE WORDS
blacklisted_rule_words = \
    ['a', 'an', 'the', 'have', 'has', 'been', 'was', 'is', 'by', 'to', 'at', 'for', 'in', 'of', 'from', 'like', 'with',
     'were', 'are', 'what', 'where', 'how', 'why', 'who', 'it', "it's", 'and', 'but', 'on', "its", 'we', 'our', 'over',
     'under', "about", "upon", "these", "those", "this", "that", "i", "they", "them"]


def generate_examples(word_list):

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
                        tagged_substring_list = word_list[i:tag_closing_index+1]
                        tagged_substring = ''.join(str(e + " ") for e in tagged_substring_list)
                        extracted_word = re.sub('<[^>]*>', '', tagged_substring).strip()
                        examples.positive.append([i, extracted_word])
                        for x in range(i+1, tag_closing_index+1):
                            word_list[x] = "__"
                        break
        else:
            # **************** Create uni-gram examples ****************
            # Only the words with first letter upper, and not in the rule list will be used for uni-gram formation.
            # The formation of bi-gram will be on the basis of the second word. If second word is not loc
            # and is not a rule word, then the bi-gram is created.
            if word[0].isupper() \
                    and word.lower() not in blacklisted_rule_words \
                    and not (any(ch.isdigit() for ch in word)):
                # Adding probabilistic pickup to ensure negatives do not overshoot positives by a significant number
                if random.random() < 0.12:
                    examples.negative.append([i, word])

                # **************** Create bi-gram examples ****************
                # If condition to define next_word, depending on current word is last or not.
                next_word = word_list[i + 1] if i < len(word_list) - 1 else "__"
                if next_word.lower() not in blacklisted_rule_words \
                        and '<loc>' not in next_word \
                        and not (any(ch.isdigit() for ch in next_word)):
                    if random.random() < 0.1:
                        examples.negative.append([i, word + " " + next_word])

    return examples

