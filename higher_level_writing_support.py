from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text, max_length=50):
    summary = summarizer(text, max_length=max_length, min_length=25, do_sample=False)
    return summary[0]['summary_text']
