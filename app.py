from transformers import AutoModelForCausalLM, AutoTokenizer

import torch
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "No input provided"}), 400
        try:
            inputs = tokenizer.encode(user_input, return_tensors="pt").to(model.device)
            outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=0.7)
            chatbot_reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return jsonify({"reply": chatbot_reply})
        except Exception as e:
            return jsonify({"error": "Failed to process your request. Please try again later."}), 500
    return render_template('chatbot.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/api/latest-news')
def api_latest_news():
    try:
        # Example: Use Bing News Search API or another news API
        # For demonstration, we'll use Bing News Search (requires API key)
        # Replace 'YOUR_BING_API_KEY' with your actual key
        api_key = 'YOUR_BING_API_KEY'
        url = 'https://api.bing.microsoft.com/v7.0/news/search'
        params = {
            'q': 'legal OR law OR court OR supreme court OR case',
            'mkt': 'en-US',
            'count': 8,
            'sortBy': 'Date'
        }
        headers = {'Ocp-Apim-Subscription-Key': api_key}
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        news = resp.json()
        articles = [
            {
                'title': a['name'],
                'url': a['url'],
                'description': a.get('description', ''),
                'source': a['provider'][0]['name'] if a.get('provider') else ''
            }
            for a in news.get('value', [])
        ]
        return jsonify({'articles': articles})
    except Exception as e:
        return jsonify({'articles': [], 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)