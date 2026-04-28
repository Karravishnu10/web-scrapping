# app.py

from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
from rouge import Rouge
from sklearn.feature_extraction.text import TfidfVectorizer
import networkx as nx

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        url = request.form['url']
        article_text = get_article_text(url)
        preprocessed_text = preprocess_text(article_text)
        generated_summary = textrank_summarization(preprocessed_text)

        # Use a reference summary for evaluation (you may replace it with a human-generated summary)
        reference_summary = preprocessed_text

        # Evaluate Rouge scores
        rouge_scores = evaluate_rouge(reference_summary, generated_summary)

        # Calculate accuracy
        accuracy = calculate_accuracy(reference_summary, generated_summary)

        # Print Rouge scores and accuracy to the terminal
        print("Rouge Scores:", rouge_scores)
        print("Accuracy:", accuracy)

        # Word counts
        article_word_count = count_words(article_text)
        summary_word_count = count_words(generated_summary)

        # Render the results page
        return render_template('result.html', article_text=article_text, article_word_count=article_word_count, generated_summary=generated_summary, summary_word_count=summary_word_count)

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    if request.method == 'POST':
        input_text = request.form['input_text']
        generated_summary = textrank_summarization(input_text)

        # Word counts
        input_text_word_count = count_words(input_text)
        summary_word_count = count_words(generated_summary)

        # Render the results page
        return render_template('result.html', article_text=input_text, article_word_count=input_text_word_count, generated_summary=generated_summary, summary_word_count=summary_word_count)

def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([paragraph.get_text() for paragraph in paragraphs])
    return text

def preprocess_text(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords or word in string.punctuation:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    return ' '.join(sentences)

def textrank_summarization(text, num_sentences=5):
    sentences = sent_tokenize(text)

    graph = nx.Graph()
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(sentences)
    similarity_matrix = matrix * matrix.T

    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            if similarity_matrix[i, j] > 0:
                graph.add_edge(sentences[i], sentences[j], weight=similarity_matrix[i, j])

    ranked_sentences = nx.pagerank(graph, weight='weight')
    top_sentences = sorted(ranked_sentences, key=ranked_sentences.get, reverse=True)[:num_sentences]

    return ' '.join(top_sentences)

def count_words(text):
    words = word_tokenize(text)
    return len(words)

def calculate_accuracy(reference, generated):
    reference_set = set(word_tokenize(reference.lower()))
    generated_set = set(word_tokenize(generated.lower()))

    # Calculate overlap and accuracy
    overlap = len(reference_set.intersection(generated_set))
    accuracy = overlap / len(reference_set) if len(reference_set) > 0 else 0

    return accuracy

def evaluate_rouge(reference, summary):
    rouge = Rouge()
    scores = rouge.get_scores(summary, reference)
    return scores[0]

if __name__ == '__main__':
    app.run(debug=True)
