#pip install -q -U google-genai
from google import genai

# Set/Get API Key in Google Studio
client = genai.Client(api_key="AIzaSyCyNgdkVYHSfoDfJ7UaX85uwgiZ_dnWkek")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
#AI learns from data to find patterns and make decisions or predictions.