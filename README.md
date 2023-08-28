# TRANSFORMER BASED TEXT SUMMARIZER

[![Python 3.10.12](https://img.shields.io/badge/python-3.10.12-blue.svg)](https://www.python.org/downloads/release/python-31012/)
![Static Badge](https://img.shields.io/badge/Hugging_Face-Transformer-orange.svg)


This repository contains the code and resources for building an advanced text summarization system using the powerful Transformer model from Hugging Face's Transformers library.

## Project Overview

Text summarization is a crucial task in natural language processing and information retrieval. This project demonstrates the implementation of a Transformer-based model for generating concise and coherent summaries from longer text documents.

The main components of the project include:

- Data preprocessing: Prepare your text data for training and evaluation.
- Model configuration: Choose and configure the appropriate Transformer model for text summarization.
- Training: Train the model on your dataset to learn the summarization task.
- Evaluation: Assess the quality of generated summaries using various metrics.
- Inference: Utilize the trained model to generate summaries for new text inputs.

## Features

- **Transformer Model**: Harness the power of the Transformer architecture, which has revolutionized many natural language processing tasks.
- **Easy-to-Use**: The project codebase is designed to be user-friendly, making it simple to train, evaluate, and use the summarization model.
- **Customization**: Fine-tune the model on your specific domain or dataset for better summarization results.
- **State-of-the-Art**: Implement a cutting-edge text summarization solution using the Hugging Face Transformers library, which provides pre-trained models and easy-to-use APIs.

## **Tools & Techniques**

- `Code versioning` using Git
- `Modular coding` with separate files for data ingestion, training, evaluation, Configuration, constants, secret keys, artifacts etc
- Training and Prediction pipelines
- `CI / CD Pipeline` using GitHub Actions
- `Docker` for creating container
- Custome `logger`
- Custom `Exception Handler`
- `Package building`
- `Deplyment` tested on **AWS EC2 instance CI/CD** using Github Action Runner


## **Deployment Tested**

*   AWS EC2

## Getting Started

Follow these steps to get started with the project:

1. Clone this repository to your local machine.
2. Install the required dependencies using the provided `requirements.txt` file.
3. Prepare your dataset for training and evaluation. You might need to preprocess your text data and create suitable data loaders.
4. Configure the model hyperparameters and architecture according to your requirements.
5. Train the model using the prepared dataset.
6. Evaluate the model's performance using appropriate metrics and visualization tools.
7. Use the trained model to generate summaries for new input text.

## Project Structure



```text
NLP-DL-07-Text_Summarizer
├─ .git
├─ .github
│  └─ workflows
│     ├─ .gitkeep
│     └─ main.yaml
├─ .gitignore
├─ app.py
├─ artifacts
├─ config
│  └─ config.yaml
├─ Dockerfile
├─ LICENSE
├─ logs
├─ main.py
├─ params.yaml
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ requirements_updated.txt
├─ research
│  ├─ 01_data_ingestion.ipynb
│  ├─ 02_data_validation.ipynb
│  ├─ 03_data_transformation.ipynb
│  ├─ 04_model_trainer.ipynb
│  ├─ 05_Model_evaluation.ipynb
│  ├─ Text_Summarization.ipynb
│  └─ trials.ipynb
├─ SampleDataset
│  └─ data.zip
├─ src
│  └─ TextSummarizer
│     ├─ config
│     │  ├─ configuration.py
│     │  └─ __init__.py
│     ├─ conponents
│     │  ├─ data_ingestion.py
│     │  ├─ data_transformation.py
│     │  ├─ data_validation.py
│     │  ├─ model_evaluation.py
│     │  ├─ model_trainer.py
│     │  └─ __init__.py
│     ├─ constants
│     │  └─ __init__.py
│     ├─ entity
│     │  └─ __init__.py
│     ├─ exception
│     │  └─ __init__.py
│     ├─ logger
│     │  └─ __init__.py
│     ├─ pipeline
│     │  ├─ prediction.py
│     │  ├─ stage_01_data_ingestion.py
│     │  ├─ stage_02_data_validation.py
│     │  ├─ stage_03_data_transformation.py
│     │  ├─ stage_04_model_trainer.py
│     │  ├─ stage_05_model_evaluation.py
│     │  └─ __init__.py
│     ├─ utils
│     │  ├─ utils.py
│     │  └─ __init__.py
│     └─ __init__.py
└─ template.py

```