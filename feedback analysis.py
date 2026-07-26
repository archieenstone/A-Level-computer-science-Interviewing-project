from google import genai
from google.genai import types

client = genai.Client(api_key="AQ.Ab8RN6LZa2jmY-lpucIY2xXegfaD0EDPlkWbPpHP7CYxn65fyw")


client = genai.Client()

doc_url = "conversation_log.txt"

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        types.Part.from_bytes(
            data=doc_url,
            mime_type='application/txt',
        ),
        prompt
    ]
)

print(response.text)