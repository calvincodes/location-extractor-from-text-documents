# [Location Extractor from Text Documents](https://sites.google.com/view/data-science-project/home) 

## Setup & Requirements

```shell
pip3 install -r requirements.txt
```

## Running the project

```shell
python3 driver.py
```

## Introduction
This project attempts to detect words representing locations from natural text documents using a supervised learning algorithm.

For example, in the following sentence, our extractor will attempt to **POSITIVELY classify** the instances in bold as locations. 
It will also attempt to ~DISCARD the instance in ~~Strikethrough~~, which look like locations but are actually not as per the context of the sentence.

**WASHINGTON** — Smartphone users in **Russia** can no longer download the LinkedIn app on iPhone or Android devices, following a similar move in **China** to block The ~~New York~~ Times app on iPhones.

## DataSet Used
[Kaggle News DataSet](https://www.kaggle.com/snapcrack/all-the-news) which contains well-formed sentences. Also, documents contain only plain text in English.

## Project Website
[https://sites.google.com/view/data-science-project/home](https://sites.google.com/view/data-science-project/home)

## Authors

* **[Anshu Verma](https://github.com/anshuv99)**
* **[Srujana](https://github.com/SrujanaN)**
* **[Arpit Jain](https://github.com/calvincodes)**