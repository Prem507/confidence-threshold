import PyPDF2
import nltk
import numpy as np
import pandas as pd

from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

files = [
    r"D:\Desktop\CSV\AnnualHealthCheck.pdf",
    r"D:\Desktop\CSV\LeavePolicy.pdf",
    r"D:\Desktop\CSV\NoticePeriod.pdf",
    r"D:\Desktop\CSV\OfficeTime.pdf",
    r"D:\Desktop\CSV\Separation.pdf",
    r"D:\Desktop\CSV\Travel.pdf",
    r"D:\Desktop\CSV\USA_Employee_Handbook-Freely_Available.pdf"
]

document = []

for file in files:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    document.append(text)
print("Documents loaded: ", len(document))

sentences = []

for doc in document:
    sents = sent_tokenize(doc)
    for s in sents:
        sentences.append(s)

print("Total senetences: " ,len(sentences))

stopwords = set(stopwords.words("english"))
stemmer = PorterStemmer()

def preprocess(text):
    tokens = word_tokenize(text)
    clean_tokens = []
    for word in tokens:
        if word.isalpha() and word not in stopwords:
            stem = stemmer.stem(word)
            clean_tokens.append(stem)
        return " ".join(clean_tokens)

processes_senetences = []

for s in sentences:
    processes_senetences.append(preprocess(s))

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(processes_senetences)

query = input("Ask Quetion:")

processed_query = preprocess(query)

query_vector = vectorizer.transform([processed_query])

similarities = cosine_similarity(query_vector, tfidf_matrix)

scores = similarities[0]


top_k = 3
thershold = 0.20
score_series = pd.Series(scores)

top_indices = score_series.nlargest(top_k).index.tolist()

if scores[top_indices[0]] < thershold:
    print("\nSorry, I could not find answer in the documents.\n")

else:
    print("\nTop Top matching Answers:\n")
    for idx in top_indices:
        if scores[idx] >= thershold:
            print("Answer:",sentences[idx])
            print("confidence Score:",scores[idx])
            print("------------------------------")

