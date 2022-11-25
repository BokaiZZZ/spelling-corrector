# Spelling Corrector Microservice
[![Python application test with Github Actions](https://github.com/BokaiZZZ/spelling-corrector/actions/workflows/main.yml/badge.svg)](https://github.com/BokaiZZZ/spelling-corrector/actions/workflows/main.yml)

This is the 4th individual project of IDS706 in Duke University.


## Project Introduction

This project is a spelling corrector based on the Levenshtein distance. It is implemented as a Flask microservice, which is deployed using Google App Engine. Continuous delivery is implemented by Cloud Bulid in GCP and Continuous Integration is reliazed through Github Actions.

Access the deployed website [here](https://spelling-corrector-flask.ue.r.appspot.com/)

Watch the video demo of this project [here](https://youtu.be/nDFUZ_FOGkI)

## Functionality 

The microservice can correct a mis-spelling word and return the corrected word. If the input word has no spelling errors, it will just return the original word. 

To use the microservice, just add "/correct" and a input word after the url. 
![image](https://user-images.githubusercontent.com/97444802/204042252-b693c294-8fc6-4da8-ad26-8aa472d97889.png)
