import os
from input_reader import read_file
import re


data_set_directory = 'all_labelled_data_set/'
dirname = os.path.dirname(__file__)

total_locations = [""]
whitelist_set = set(())

for file_no in range(117, 370):

    # Step 1: Create absolute path for the file and check if the file exists.
    filename = os.path.join(dirname, data_set_directory+str(file_no)+".txt")
    if not os.path.isfile(filename):
        continue

    # Step 2: Read the file and create a list of all words in the file.
    word_list = read_file(filename)

    for i, word in enumerate(word_list):

        # TODO: Remove this commented redundant code post confirmation.
        # We should NOT be needing these. We have not tagged this.
        # word = re.sub("\'s", "", word)
        # word = re.sub("\’s", "", word)

        # As "loc" can commonly occur even in normal words like al'loc'ation, hence checking for presence of <loc>
        if '<loc>' in word:
            # For the same reason as above, explicitly checking for one occurrence of both opening and closing tags.
            if word.count("<loc>") == 1 and word.count("</loc>") == 1:
                extracted_word = re.sub('<[^>]*>|[^a-zA-Z\d\s:]', '', word)
                whitelist_set.add(extracted_word)
                total_locations.append(extracted_word)
                print(str(word_list[i-2:i+1]) + " " + str(file_no))

            else:
                # If the label spans across multiple words, like <loc>United States of America</loc>.
                # Iterate till we find the closing tag.
                for tag_closing_index in range(i, len(word_list)):
                    if word_list[tag_closing_index].count("</loc>") == 1:
                        tagged_substring_list = word_list[i:tag_closing_index+1]
                        tagged_substring = ''.join(str(e + " ") for e in tagged_substring_list)
                        extracted_word = re.sub('<[^>]*>|[^a-zA-Z\d\s:]', '', tagged_substring).strip()
                        whitelist_set.add(extracted_word)
                        total_locations.append(extracted_word)
                        for x in range(i+1, tag_closing_index+1):
                            word_list[x] = "__"
                        break
print(whitelist_set)
