import string
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag


def get_wordnet_pos(word):
    """
    Map POS tag to first character accepted lemmatize().
    """
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


# Defines a custom vectorizer class
class CustomVectorizer(CountVectorizer):

    # overwrite the build_analyzer method, allowing one to
    # create a custom analyzer for the vectorizer
    def build_analyzer(self):

        # load stop words using CountVectorizer's built in method
        stop_words = self.get_stop_words()

        # create the analyzer that will be returned by this method
        def analyser(mess):
            # Remove punctuation, lowercase all letters            
            clean = mess.replace('-', '')
            clean = ''.join(
                [char if char not in string.punctuation or '0123456789' else ' ' for char in clean])
            clean = [word.lower() for word in clean.split()] 

            wordnet_lemmatizer = WordNetLemmatizer()
            lem_sentence = []
            
            for word in clean:
                lem_sentence.append(
                    wordnet_lemmatizer.lemmatize(word, get_wordnet_pos(word)))

            # use CountVectorizer's _word_ngrams built in method
            # to remove stop words and extract n-grams
            return(self._word_ngrams(lem_sentence, stop_words))
        return(analyser)
