
import openai

def generate_intro(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher Bewerbungsexperte."},
                {"role": "user", "content": f"Formuliere eine einleitende Motivation für meinen Traumjob: {prompt}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Fehler bei der GPT-Anfrage: {e}"
