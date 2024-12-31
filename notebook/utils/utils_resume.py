from transformers import pipeline

#Model 
summary_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")


def generate_summary(text: str) -> str:

    if len(text.split()) > 1024:
        text = " ".join(text.split()[:1024])

    summary = summary_pipeline(text, max_length=130, min_length=30, do_sample=False)
    
    return summary[0]['summary_text']