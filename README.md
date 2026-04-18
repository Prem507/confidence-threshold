Markdown
# 📄 Advanced NLP – Document Question Answering System

This project is a **Document Question Answering System** built using Python and NLP techniques.  
It allows users to ask questions from multiple PDF documents and returns the **most relevant answers with confidence scores**.

---

## 🚀 Features

- 📥 Extracts text from multiple PDF files  
- ✂️ Converts text into sentences  
- 🧹 Applies text preprocessing:
  - Tokenization  
  - Stopword removal  
  - Stemming  
- 📊 Uses TF-IDF for vectorization  
- 🔍 Uses Cosine Similarity for matching  
- 📈 Returns **Top-K (Top 3) relevant answers**  
- 🎯 Applies **confidence threshold filtering** to avoid incorrect results  

---

## 🛠️ Technologies Used

- Python  
- NLTK  
- NumPy  
- Pandas  
- Scikit-learn  
- PyPDF2  

---

## ⚙️ How It Works

1. Load multiple PDF documents  
2. Extract text from each document  
3. Split text into sentences  
4. Preprocess text:
   - Lowercasing  
   - Tokenization  
   - Stopword removal  
   - Stemming  
5. Convert sentences into vectors using **TF-IDF**  
6. Take user query as input  
7. Compute similarity using **Cosine Similarity**  
8. Rank results and return **Top 3 answers**  
9. Apply **confidence threshold** to filter low-quality results  

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Prem507/Advanced-NLP.git
cd Advanced-NLP
Install dependencies:
Bash
pip install nltk numpy pandas scikit-learn PyPDF2
Run the program:
Bash
python main.py
Enter your question.
💡 Example
Input:

Ask Question: What is leave policy?
Output:

Top matching Answers:

Answer: Employees are entitled to leave as per company policy.
Confidence Score: 0.89

Answer: Leave rules are defined in the employee handbook.
Confidence Score: 0.76
If no relevant answer is found:

Sorry, I could not find answer in the documents.
📂 Project Structure

Advanced-NLP/
│── data/ (PDF files)
│── main.py
│── README.md
📈 Future Improvements
Use Sentence Transformers / BERT for better accuracy
Implement semantic search with FAISS
Build a web interface using Streamlit
Deploy using AWS / Streamlit Cloud
👨‍💻 Author
Prem Kumar
B.Tech CSE (Final Year)
⭐ Conclusion
This project demonstrates how NLP techniques can be used to build a simple yet practical question answering system with ranking and confidence filtering, similar to real-world search systems.
