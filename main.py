from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr
import os

load_dotenv()


class Myassistant:
    def __init__(self, pdf_path: str):
        self.client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )
        self.about_me = self._load_pdf(pdf_path)
        self.system_prompt = self._build_system_prompt()

    def _load_pdf(self, path: str) -> str:
        reader = PdfReader(path)
        text = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
        return "\n".join(text)

    def _build_system_prompt(self) -> str:
        return (
            "You are representing Akash and always speak as Akash. "
            "Use the information below to answer questions professionally.\n\n"
            f"{self.about_me}"
        )

    def chat(self,message,history):
        messages = [{"role": "system", "content": self.system_prompt}] + [{"role": "user", "content": message}]
        done = False
        while not done:

            # This is the call to the LLM - see that we pass in the tools json

            response = self.client.chat.completions.create(model="llama3.2:1b", messages=messages)

            finish_reason = response.choices[0].finish_reason
            
            # If the LLM wants to call a tool, we do that!
            
            if finish_reason=="tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                results = handle_tool_calls(tool_calls)
                messages.append(message)
                messages.extend(results)
            else:
                done = True
        return response.choices[0].message.content


agent =  Myassistant("docs/Akash-resume.pdf")

gr.ChatInterface(agent.chat).launch()

# result =agent.chat("who are you?")
# print(result)
