
from flask import Flask, request, jsonify
import redis
import json
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Connect to Redis
redis_client = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], db=app.config['REDIS_DB'])

# In-memory FAQ data (replace with a more robust solution in a real application)
faq_data = {
    "What are your business hours?": "Our business hours are 9 AM to 5 PM, Monday to Friday.",
    "What is your return policy?": "You can return any item within 30 days of purchase for a full refund.",
    "How can I track my order?": "You can track your order using the tracking number provided in your shipping confirmation email.",
    "Do you offer international shipping?": "Yes, we offer international shipping to most countries. Shipping fees may vary.",
    "What payment methods do you accept?": "We accept all major credit cards, as well as PayPal and Apple Pay.",
    "How do I contact customer support?": "You can contact our customer support team by emailing support@example.com or by calling our toll-free number at 1-800-555-1234."
}

@app.route('/')
def index():
    return "Welcome to the Customer Support Chatbot!"


@app.route('/chat', methods=['POST'])
def chat():
    user_id = request.json.get('user_id')
    message = request.json.get('message')

    if not user_id or not message:
        return jsonify({"error": "user_id and message are required"}), 400

    # Retrieve chat history from Redis
    history_key = f"chat_history:{user_id}"
    chat_history = redis_client.get(history_key)
    if chat_history:
        chat_history = json.loads(chat_history)
    else:
        chat_history = []

    # Check for FAQ answer
    response = faq_data.get(message)

    if not response:
        response = "I'm sorry, I don't have an answer for that. Can I help with anything else?"

    # Update chat history
    chat_history.append({"user": message, "bot": response})
    redis_client.set(history_key, json.dumps(chat_history))

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
