#!/usr/bin/env python
# coding: utf-8

# In[3]:


from transformers import AutoTokenizer, AutoModelForCausalLM

token="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"
custom_cache_dir = "D:/gemini_model/"

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b", token=token)
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b", token=token)


# In[11]:


import gradio as gr


def gemma2(text):
    input_ids = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**input_ids)
    return tokenizer.decode(outputs[0])


demo = gr.Interface(
    gemma2,
    inputs="text",
    api_name='gemma2',
    outputs="text"
)


if __name__ == "__main__":
    demo.launch()

