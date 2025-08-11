from fastapi import FastAPI, Body
from . import storage, llm, summarizer

app = FastAPI()

@app.post("/targets")
def add_target(target: dict):
    storage.save_target(target)
    suggestion = llm.suggest_attack_steps(target)
    return {"saved": target, "suggestion": suggestion}

@app.post("/summarize")
def summarize(text: str = Body(..., embed=True)):
    return {"summary": summarizer.to_report(text)}

@app.get("/report")
def generate_report():
    findings = storage.fetch_findings()
    return {"report": llm.generate_report(findings)}
