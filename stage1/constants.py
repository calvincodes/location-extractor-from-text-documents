# Update labels as you add more features
labels = ['Word', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'Class']

neighboring_verbs_for_negative_examples = ['has', 'have', 'had', 'was', 'were', 'with', 'would', 'sea',
                                           'of', 'times', 'post', 'against', 'should', 'will', 'wont',
                                           'not', 'do', 'does']

blacklist_words = ['january', 'february', 'March',
                   'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December', 'Mr.', 'Trump']

possible_strong_prev_words = ['of', 'at', 'between', 'neighbouring', 'into', 'from',
                              'near', 'across', 'over', 'around', 'outside', 'to', 'in']

# TODO: UPDATE THIS LIST OF BLACKLISTED RULE WORDS
blacklisted_rule_words = \
    ['Mr.', 'May', 'American', 'Indian',
     'a', 'an', 'the', 'have', 'has', 'been', 'was', 'is', 'by', 'to', 'at', 'for', 'in', 'of', 'from', 'like', 'with',
     'were', 'are', 'what', 'where', 'how', 'why', 'who', 'it', "it's", 'and', 'but', 'on', "its", 'we', 'our', 'over',
     'under', "about", "upon", "these", "those", "this", "that", "i", "they", "them"]
