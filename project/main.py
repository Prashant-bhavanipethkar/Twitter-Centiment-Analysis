from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
import os

# Load model + vectorizer
model_path = r"C:\Users\hp\Desktop\test_twitter_sentiment\project\src\logistic_model.pkl"
vectorizer_path = r"C:\Users\hp\Desktop\test_twitter_sentiment\project\src\tfidf-vectorizer.pkl"

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# FastAPI
app = FastAPI()

# Static + Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict(request: Request, text: str = Form(...)):

    cleaned = text  # if you want, apply your clean_text() here

    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    sentiment = "Positive" if prediction == 1 else "Negative"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": sentiment,
            "input_text": text
        }
    )
