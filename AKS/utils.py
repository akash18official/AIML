import os

import requests


def call_llm(text: str) -> str:
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise ValueError("OPENAI_API_KEY is not set")

	base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
	model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
	endpoint = f"{base_url.rstrip('/')}/chat/completions"

	response = requests.post(
		endpoint,
		headers={
			"Authorization": f"Bearer {api_key}",
			"Content-Type": "application/json",
		},
		json={
			"model": model,
			"messages": [
				{"role": "user", "content": text},
			],
		},
		timeout=60,
	)
	response.raise_for_status()

	data = response.json()
	try:
		return data["choices"][0]["message"]["content"].strip()
	except (KeyError, IndexError, AttributeError) as exc:
		raise ValueError("Unexpected response from the LLM endpoint") from exc

