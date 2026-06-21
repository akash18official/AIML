import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from utils import call_llm


app = FastAPI(title="Text to LLM API")


class TextRequest(BaseModel):
	text: str = Field(..., min_length=1, description="Input text to send to the LLM")


class TextResponse(BaseModel):
	result: str


@app.post("/generate", response_model=TextResponse)
def generate_text(payload: TextRequest) -> TextResponse:
	try:
		result = call_llm(payload.text)
	except Exception as exc:
		raise HTTPException(status_code=500, detail=str(exc)) from exc

	return TextResponse(result=result)


@app.get("/health")
def health() -> dict[str, str]:
	return {"status": "ok"}

