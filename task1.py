import pymysql as mysql
from docx import Document
import nltk
import re
import ssl
import pickle

# Load tokenizer from custom path
tokenizer_path = '/home/samyak-dahalelinux/nltk_data/tokenizers/punkt/english.pickle'
with open(tokenizer_path, 'rb') as f:
    tokenizer = pickle.load(f)

# Config
DOCX_PATH = "sample1.docx"  # Path to your DOCX file
conn = mysql.connect(
    host="localhost",
    user="root",
    password="samyakSQL123",  # replace with your real password
    database="jnec",
    charset="utf8mb4",
    autocommit=True
)
cur = conn.cursor()

# Clean text
def clean(text):
    return re.sub(r"\s+", " ", text.strip())

# Use custom tokenizer instead of nltk.sent_tokenize()
def split_sentences(text):
    return [clean(s) for s in tokenizer.tokenize(text) if clean(s)]

# Main insert logic
def insert_sentences_to_db(docx_path):
    doc = Document(docx_path)

    insert_sql = """
    INSERT INTO sentences (`Index`, Sentence, ParagraphNo, ParagraphSentenceIdx)
    VALUES (%s, %s, %s, %s)
    """

    sentence_id = 1

    for para_num, para in enumerate(doc.paragraphs, start=1):
        paragraph_no = f"P{para_num}"
        sentences = split_sentences(para.text)
        for sent_num, sentence in enumerate(sentences, start=1):
            idx = f"S{sentence_id}"
            para_sent_idx = f"{paragraph_no}S{sent_num}"
            cur.execute(insert_sql, (idx, sentence, paragraph_no, para_sent_idx))
            sentence_id += 1

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {sentence_id - 1} sentences into 'sentences' table.")

# Run
if __name__ == "__main__":
    insert_sentences_to_db(DOCX_PATH)
