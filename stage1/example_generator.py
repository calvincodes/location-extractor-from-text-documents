import re
from examples import Examples


def generate_examples(word_list):

    stupid_words = ["stupid"];
    examples = Examples()

    for i, word in enumerate(word_list):

        # word = re.sub("\'s", "", word)  # We should NOT be needing this. We have not tagged this.
        # word = re.sub("\’s", "", word)

        # As "loc" can commonly occur even in normal words like al'loc'ation, hence checking for presence of <loc>
        if '<loc>' in word:
            # For the same reason as above, explicitly checking for one occurrence of both opening and closing tags.
            if word.count("<loc>") == 1 and word.count("</loc>") == 1:
                extracted_word = re.sub('<[^>]*>', '', word)
                examples.positive.append([i, extracted_word])
            # else:  # If the label spans across muliple words, like <car>Honda Accord</car>.
            # For us, we will iterate till we find the closing tag.
            #     temp = word + " " + word_list[i + 1]
            #     temp = re.sub('<[^>]*>', '', temp)
            #     pos_examples.append([i, temp])
            #     word_list[i + 1] = "__"
        else:
            # Only the words with first letter upper, and not in the rule list will be used for unigram formation.
            # The formation of bi-gram will be on the basis of the second word. If second word is not carmake
            # and is not a rule word, then the bi-gram is created.
            if word[0].isupper() and word.lower() not in stupid_words and not (any(ch.isdigit() for ch in word)):
                examples.negative.append([i, word])
                # temp2 = word_list[i + 1] if i < len(
                #     word_list) - 1 else "__"  # If condition to define temp2, depending on current word is last or not.
                # if temp2.lower() not in stupid_words and 'carMake' not in temp2 and not (
                # any(ch.isdigit() for ch in temp2)):
                #     if random.random() < 1:  # USELESS IF STATEMENT. This is always true.
                #         neg_examples.append([i, word + " " + temp2])

    return examples

