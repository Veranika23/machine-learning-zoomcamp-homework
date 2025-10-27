    #!/usr/bin/env python
    # coding: utf-8

    # Question 1

    # In[1]:


import pickle
import wget
from fastapi import FastAPI
import uvicorn
import requests


from typing import Dict, Any
    # uv --version

    # uv 0.9.5

    #Question 2
    #sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e

    #Question 3
url =  'https://github.com/DataTalksClub/machine-learning-zoomcamp/raw/refs/heads/master/cohorts/2025/05-deployment/pipeline_v1.bin'
downloaded_file = wget.download(url)

with open (downloaded_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

print('model downloaded')

    # person = {
    #     "lead_source": "paid_ads",
    #     "number_of_courses_viewed": 2,
    #     "annual_income": 79276.0
    # }

    # def predict_single(person):
    #     result = pipeline.predict_proba(person) [0,1]
    #     return float(result)

    # def predict(person):
    #     convert = predict_single(person)
    #     return {
    #         "convert_probability": convert,
    #         "convert": bool(convert >= 0.5)
    #     }

    # print(predict(person))  

    #{'convert_probability': 0.5336072702798061, 'convert': True}

    #Question 4

app = FastAPI(title="05-deployment-hw")


def predict_single(person):
    result = pipeline.predict_proba(person) [0,1]
    return float(result)

@app.post("/05-deployment-hw")    
def predict(person: Dict[str, Any]):
    convert = predict_single(person)
    return {
        "convert_probability": convert,
        "convert": bool(convert >= 0.5)
        }

if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=9696)

