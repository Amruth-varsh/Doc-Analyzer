import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Ensure the punkt tokenizer model is downloaded
nltk.download("punkt")

def chunk_text(text, max_tokens=300):
    # Use the Punkt tokenizer directly
    tokenizer = PunktSentenceTokenizer()
    sentences = tokenizer.tokenize(text)

    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(chunk.split()) + len(sentence.split()) <= max_tokens:
            chunk += " " + sentence
        else:
            chunks.append(chunk.strip())
            chunk = sentence

    if chunk:
        chunks.append(chunk.strip())

    return chunks
