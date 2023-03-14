import nltk
import re



#Tokenizer function. You can add here different preprocesses.
def preprocess(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting, 
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''
    # Place your code here
    # Keep in mind that sentence splitting affectes the number of sentences
    # and therefore, you should replicate labels to match.
    return sentence,labels



def preprocess1(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting,
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    # iterating through all the texts
    for i, text in sentence.iteritems():
        # removing the symbols and numbers
        text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
        text = re.sub(r'[[]]', ' ', text)
        # appending to data_list
        sentence[i] = text

    return sentence,labels

def preprocess2(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting,
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    # iterating through all the texts
    for i, text in sentence.iteritems():
        # converting the text to lower case
        text = text.lower()
        # appending to data_list
        sentence[i] = text

    return sentence,labels


def preprocess3(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting,
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    # iterating through all the texts
    for i, text in sentence.iteritems():
        # removing the symbols and numbers
        text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
        text = re.sub(r'[[]]', ' ', text)
        # converting the text to lower case
        text = text.lower()
        # appending to data_list
        sentence[i] = text

    return sentence,labels


def preprocess4(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting,
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    # iterating through all the texts
    for i, text in sentence.iteritems():
        # removing the symbols and numbers
        # japanese
        if re.search("[\u3040-\u30ff]", text):
            text = ",".join(list(text))
        # chinese
        if re.search("[\u4e00-\u9FFF]", text):
            text = ",".join(list(text))

        # appending to data_list
        sentence[i] = text

    return sentence,labels

