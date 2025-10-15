import os, requests
from dotenv import load_dotenv

load_dotenv()

def generate_video(text: str) -> str:
    api_url = os.getenv("WEAVEIT_API_URL")
    api_key = os.getenv("WEAVEIT_API_KEY")

    payload = {"script": text}
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        res = requests.post(api_url, json=payload, headers=headers)
        data = res.json()
        return data.get("video_url", "https://weaveit.ai")
    except Exception as e:
        print("Video generation failed:", e)
        return "Error generating video"
