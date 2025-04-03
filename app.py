
# demo app for gradio
# Name intesity generator, run file with 'python3 app.py' in terminal and connect to link

# import gradio as gr

# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)

# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "slider"],
#     outputs=["text"],
# )

# demo.launch()


import gradio as gr
from transformers import pipeline

# Create a summarization pipeline using a pre-trained model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define a function to summarize text
def summarize_text(input_text):
    summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

# Build and launch Gradio interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter your text here...", label="Input Text"),
    outputs=gr.Textbox(label="Summarized Text"),
    title="AI Text Summarizer",
    description="Enter a block of text and get a concise summary using AI."
)

interface.launch()
