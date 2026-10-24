import torch
import gradio as gr
from transformers import pipeline
from pathlib import Path
from transformers import pipeline

pipe = pipeline("text-generation", model="MemTensor/MemT-1.0-Flash", trust_remote_code=True)


def summary(input):
    output = text_summary(input)
    return output[0]['summary_text']

gr.close_all()

demo=gr.Interface(fn=summary, inputs=[gr.Textbox(label="Input Text to Summarize", lines=6)], outputs=[gr.Textbox(label="Summarized Text", lines=4)], title="Project1 : Text Summarizer", description="This application will be used to summarize the text")
demo.launch()


 
