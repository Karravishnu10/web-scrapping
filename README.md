# 📄 Text Summarizer & Web Scraping Application

A **Flask-based NLP application** that performs **automatic text summarization** using the **TextRank algorithm**, with support for both **web scraping (URL input)** and **direct text input**.  

The system integrates **Natural Language Processing (NLP)**, **TF-IDF vectorization**, and **graph-based ranking (PageRank)** to generate concise summaries, along with evaluation metrics like **ROUGE score and accuracy**.

---

## 📁 Project Structure


---

## 🚀 Tech Stack

| Layer         | Technology                                              |
|---------------|---------------------------------------------------------|
| Backend       | Flask (Python)                                          |
| Text Extraction | `requests`, `BeautifulSoup4`                         |
| NLP Processing | `nltk` (tokenization, stopwords)                       |
| Summarization | `scikit-learn` (TF-IDF), `networkx` (PageRank)         |
| Evaluation    | `rouge` (ROUGE scores), custom token overlap accuracy  |
| Frontend      | HTML5, CSS3, Bootstrap 5                                |

---

## ✨ Features

- 🔗 **URL Summarization** – Extracts article text from a given URL (via `<p>` tags) and summarizes it.
- 📝 **Direct Text Summarization** – Users can paste or type their own text and get a summary.
- 🧠 **TextRank Algorithm** – Uses TF‑IDF and PageRank to rank sentences and select the top ones.
- 📊 **Evaluation Metrics** – ROUGE scores (precision, recall, F1) and an overlap-based accuracy are printed in the terminal.
- 🔢 **Word Count Comparison** – Shows word counts for original text and generated summary.
- 🎨 **Clean Web Interface** – Built with Bootstrap, responsive cards, and separate CSS for results.

---

## 🛠️ Prerequisites

Make sure the following are installed on your system:

- [Python 3.7+](https://www.python.org/downloads/)
- `pip` package manager
- Required Python libraries (see installation steps)
- NLTK data (`punkt`, `stopwords`)

---

## 📦 Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer

## ▶️ Running Locally

### Start the CAP Service

```bash
cds watch
```

> In VS Code: go to **Terminal → Run Task → cds watch**

The CAP service will be available at: `http://localhost:4004`

### Run the Python PDF Separation Script

```bash
cd app/python
python main.py
```

Place your source PDFs in the `data/sources/` directory before running the script.

---

## 🔧 How It Works

1. PDF files are placed in the `data/sources/` folder.
2. The Python script in `app/python/` reads and processes the PDFs.
3. PDFs are separated/split based on defined logic (by page, section, or keyword).
4. The CAP service layer (`srv/`) exposes the processed data or results as OData APIs.
5. The application can be deployed to SAP BTP for cloud access.

---


2. **Login to Cloud Foundry:**
```bash
   cf login
```

3. **Deploy:**
```bash
   cf push
```

---

## 📂 Key Files Explained

| File/Folder         | Purpose                                               |
|---------------------|-------------------------------------------------------|
| `app/python/`       | Python scripts for PDF splitting/separation logic     |
| `data/sources/`     | Input PDF files to be processed                       |
| `srv/`              | CAP CDS service definitions and API handlers          |
| `package.json`      | Node.js project config and CAP dependencies           |
| `eslint.config.mjs` | ESLint rules for JavaScript code quality              |

---

## 📖 Learn More

- [SAP CAP Documentation](https://cap.cloud.sap/docs/get-started/)
- [SAP BTP Developer Guide](https://developers.sap.com/tutorials/btp-cockpit-setup.html)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [pypdf Documentation](https://pypdf.readthedocs.io/)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source. Feel free to use and modify it for your own learning and projects.

---

## 👤 Author

**Karravishnu10**  
GitHub: [@Karravishnu10](https://github.com/Karravishnu10)
