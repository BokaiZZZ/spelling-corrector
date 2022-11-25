# Spelling Corrector Microservice

This is the 4th individual project of IDS706 in Duke University.


## Project Introduction

This project is a spelling corrector based on the Levenshtein distance. It is implemented as a Flask microservice, which is deployed using Google App Engine. Continuous delivery is implemented by Cloud Bulid in GCP.

Access the deployed website [here](https://spelling-corrector-flask.ue.r.appspot.com/)

## Functionality 

The microservice can correct a mis-spelling word and return the corrected word. If the input word has no spelling errors, it will just return the original word. 

To use the microservice, just add "/correct" and a input word after the url. 
![image](https://user-images.githubusercontent.com/97444802/204042252-b693c294-8fc6-4da8-ad26-8aa472d97889.png)
