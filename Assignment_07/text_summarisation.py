#!/usr/bin/env python
# coding: utf-8



from transformers import pipeline

class TextSummarisation():
    def __init__(self,model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)
    def give_summary(self,text):
        max_length = int(input("Enter the desired Maximum lenght of summary "))
        min_length = int(input("Enter the desired Minimum lenght of summary "))
        return self.summarizer(text, max_length=max_length, min_length=min_length)





