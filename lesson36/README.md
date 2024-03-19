# Documentation for lesson 34

## Overview
###### Deployed an interface for interacting with Gemma2b, a large language model developed by Google AI
#
## Deployment info
###### Ive utilized Gradio for the deployment, which provides a visual interface and allows interaction with the Gemma2b model by Gradio API
#
## Installation instruction with requirements.txt
###### To use this model, you need to install some libraries:
#
```bash
pip install -r requirements.txt
```
###### Python 3.11

### OR

##### Install Docker
##### Enter this:
```bash
docker build -t <name_image> -f .
```
##### AND this
```bash
docker run -it --rm -p <external_port>:<internal_port> <name_image>
```
## Modeling info
###### Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. They are text-to-text, decoder-only large language models, available in English, with open weights, pre-trained variants, and instruction-tuned variants.
#
## Interface description
- ###### Input: Text string, such as a question, a prompt, or a document to be summarized.
- ###### Output: Generated English-language text in response to the input, such as an answer to a question, or a summary of a document.

## Example
![Example](example.png)








