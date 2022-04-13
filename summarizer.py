import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

sample_text = """Various organisations today, be it online shopping, private sector organisations, government, tourism and catering industry, or any other institute that offers customer services, they are all concerned to learn their customer's feedback each time their services are utilised. Now, consider that these companies are receiving an enormous amount of feedback and data every single day. It becomes quite a tedious task for the management to analyse each of these datapoints and come up with insights. However, we have reached a point in technological advancements where technology can help with the tasks and we ourselves do not need to perform them. One such field that makes this happen is Machine Learning. Machines have become capable of understanding human language with the help of NLP or Natural Language Processing. Today, research is being done with the help of text analytics. One application of text analytics and NLP is Text Summarization. Text Summarization Python helps in summarizing and shortening the text in the user feedback. It can be done with the help of an algorithm that can help in reducing the text bodies while keeping their original meaning intact or by giving insights into their original text."""

cleaned_text = sample_text.replace('\n', ' ')
doc = nlp(cleaned_text)
sents = [sent.text for sent in doc.sents]

def get_word_weights(doc):
    words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    word_counts = Counter(words)
    max_count = max(word_counts.values())
    word_weights = { key : value / max_count for key, value in word_counts.items() }
    return word_weights

def get_sentence_weights(doc, word_weights):
    sentence_weights = {}
    for idx, sentence in enumerate(doc.sents):
        cleaned_sentence = [token.lemma_.lower() for token in sentence if not token.is_stop and not token.is_punct]
        cleaned_length = len(cleaned_sentence)
        sentence_scores = [word_weights.get(word, 0) for word in cleaned_sentence]
        sentence_weights[idx] = sum(sentence_scores) / cleaned_length
    
    return sentence_weights

def get_top_n_sentences(sents, sentence_weights, n):
    sentence_weights = sorted(sentence_weights.items(), key=lambda x: -x[1])
    top_sentences_idx = [sentence[0] for sentence in sentence_weights[:n]]
    summary = []
    for idx in top_sentences_idx:
        summary.append(sents[idx])
    summary_text = " ".join(summary)
    print(summary_text)
 

word_weights = get_word_weights(doc)
sentence_weights = get_sentence_weights(doc, word_weights)
summary = get_top_n_sentences(sents, sentence_weights, 3)

print(summary)