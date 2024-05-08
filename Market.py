import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my assessment on Generating Marketing Content API'

class MarketingContentGenerator:
    def __init__(self):
        self.templates = {
            "linkedin": "Excited to share insights on {topic}! 🚀 With its innovative capabilities, {topic} is revolutionizing various industries, from creative arts to healthcare. Its potential to generate realistic images, text, and even music is reshaping the way we create and interact with technology. Let's explore the endless possibilities and opportunities this cutting-edge technology offers. #GenerativeAI #Innovation #TechRevolution 🤖💡",
            "tweet": "🎉 Just discovered {topic}! It's amazing how {topic} is changing the game in so many fields. From art to healthcare, {topic} is pushing boundaries and sparking creativity. Can't wait to see what the future holds! #GenerativeAI #Innovation",
            "blog": "New blog post alert! Dive into the world of {topic} with us. We explore how {topic} is disrupting industries and fueling innovation. From generating art to assisting in medical research, {topic} is a game-changer. Read more to learn about the latest developments and applications. #GenerativeAI #TechTrends",
            "email": "Hello Team, I'm excited to introduce you to {topic}! It's an incredible technology that's reshaping industries worldwide. Learn how {topic} is driving innovation and transforming businesses in our latest newsletter. Read more here: [Link] #GenerativeAI #Innovation",
            "presentation": "Good morning everyone! Today, I'll be discussing {topic}, a groundbreaking technology that's revolutionizing the way we create and interact with content. Join me as we explore the capabilities of {topic} and its impact on various industries. Let's dive in! #GenerativeAI #Innovation"
        }

        self.emotions = [
            "Excited",
            "Thrilled",
            "Inspired",
            "Passionate",
            "Curious",
            "Eager"
        ]

    def generate_content(self, topic, format_type, emotion=None):
        """
        Generates marketing content based on the input topic and format.

        Args:
            topic (str): The main topic for the content.
            format_type (str): The desired format (e.g., "linkedin").
            emotion (str, optional): Emotion to add to the content. Defaults to None.

        Returns:
            str: Generated marketing content.
        """
        if format_type not in self.templates:
            return "Invalid format type. Please choose a valid format."

        if emotion is None:
            emotion = random.choice(self.emotions)
        content = self.templates[format_type].format(topic=topic)

        return content

@app.route('/generate-content', methods=['POST'])
def generate_content():
    data = request.get_json()
    topic = data.get('topic')
    format_type = data.get('format')
    if not topic or not format_type:
        return jsonify({"error": "Topic or format missing"}), 400
    else:
        generator = MarketingContentGenerator()
        content = generator.generate_content(topic, format_type)
        return jsonify({"content": content})

if __name__ == "__main__":
    app.run(debug=True)
