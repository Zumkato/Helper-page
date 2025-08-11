import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def suggest_attack_steps(context):
    prompt = f"""
    Host info:\n{context}
    Suggest next attack steps and relevant CVEs/tools.
    """
    return client.responses.create(model="gpt-4o-mini", input=prompt).output[0].content[0].text

def generate_report(findings):
    prompt = f"Build an executive summary and remediation plan:\n{findings}"
    return client.responses.create(model="gpt-4o-mini", input=prompt).output[0].content[0].text

