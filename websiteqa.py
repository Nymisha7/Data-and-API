from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

class WebsiteQAService:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/wiki/Generative_artificial_intelligence"

    def find_answer(self, url, question):
        try:
            full_url = self.base_url + url
            response = requests.get(full_url)
            soup = BeautifulSoup(response.content, "html.parser")
            relevant_content = soup.find_all("p")
            for content in relevant_content:
                if question.lower() in content.text.lower():
                    return content.text.strip()
            return "I don't know the answer."
        except Exception as e:
            return f"Error: {str(e)}"

@app.route('/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    url = data.get('url')
    question = data.get('question')
    if not url or not question:
        return jsonify({"error": "URL or question missing."}), 400
    service = WebsiteQAService()
    answer = service.find_answer(url, question)
    return jsonify({"answer": answer})

@app.route('/')
def index():
    return """
    <h1>Webpage Question Answering API</h1>
    <p>Submit a POST request to /answer with JSON data containing the URL and question to get the answer.</p>
    <p>Example usage:</p>
    <pre>
    {
        "url": "Generative_artificial_intelligence",
        "question": "What are the concerns around Generative AI?"
    }
    </pre>
    """

if __name__ == "__main__":
    app.run(debug=True)
