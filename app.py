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
            prompt = f"You are a helpful legal assistant. Answer the following question in a clear, concise, and friendly way. If the question is about Indian law, answer specifically for India.\nQuestion: {user_input}\nAnswer:"
            with torch.no_grad():
                inputs = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
                outputs = model.generate(inputs, max_length=256, do_sample=True, temperature=0.7, top_p=0.95, top_k=40, pad_token_id=tokenizer.eos_token_id)
                chatbot_reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
            reply = chatbot_reply.split('Answer:')[-1].strip()
            if not reply or reply == '?' or len(reply) < 3:
                reply = "I'm sorry, I couldn't find a good answer. Please try rephrasing your question or ask something else."
            return jsonify({"reply": reply})
        except Exception as e:
            return jsonify({"error": "Failed to process your request. Please try again later."}), 500
    return render_template('chatbot.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/api/latest-news')
def api_latest_news():
    try:
        api_key = 'pub_87464e44d51463f4267291cca86f58791b889'
        url = 'https://newsdata.io/api/1/news'
        params = {
            'apikey': api_key,
            'q': 'law OR legal OR court OR supreme court OR case',
            'language': 'en',
            'category': 'top,politics,world',
            'country': 'us,gb,ca,au'
        }
        resp = requests.get(url, params=params, timeout=10)
        news = resp.json()
        articles = [
            {
                'title': a.get('title', ''),
                'url': a.get('link', ''),
                'description': a.get('description', ''),
                'source': a.get('source_id', '')
            }
            for a in news.get('results', []) if a.get('title') and a.get('link')
        ]
        if not articles:
            articles = [
                {'title': 'Supreme Court Delivers Landmark Ruling on Privacy Rights', 'url': 'https://example.com/news1', 'description': 'The Supreme Court has issued a major decision expanding privacy protections.', 'source': 'Example News'},
                {'title': 'New International Treaty on Cybercrime Signed', 'url': 'https://example.com/news2', 'description': 'Countries around the world have agreed to new standards for fighting cybercrime.', 'source': 'Global Law Times'},
                {'title': 'Major Employment Law Changes Take Effect', 'url': 'https://example.com/news3', 'description': 'New employment regulations are now in force, affecting millions of workers.', 'source': 'Workplace Daily'},
                {'title': 'Landmark Environmental Case Heads to Court', 'url': 'https://example.com/news4', 'description': 'A high-profile environmental lawsuit is set to begin this week.', 'source': 'Eco Legal'},
                {'title': 'Consumer Protection Laws Strengthened', 'url': 'https://example.com/news5', 'description': 'Lawmakers have passed new rules to protect consumers from fraud.', 'source': 'Consumer Watch'},
                {'title': 'Women’s Rights Advocates Celebrate New Legislation', 'url': 'https://example.com/news6', 'description': 'A new law aims to improve workplace equality for women.', 'source': 'Equality Now'},
                {'title': 'Court Rules on Tenant Rights in Eviction Dispute', 'url': 'https://example.com/news7', 'description': 'A recent court decision clarifies tenant protections in eviction cases.', 'source': 'Housing Law Review'},
                {'title': 'Tech Giants Face Antitrust Lawsuit', 'url': 'https://example.com/news8', 'description': 'Major technology companies are under scrutiny in a new antitrust case.', 'source': 'Tech Law Journal'},
                {'title': 'International Human Rights Tribunal Issues Report', 'url': 'https://example.com/news9', 'description': 'A new report highlights global human rights challenges.', 'source': 'Human Rights Today'},
                {'title': 'Legal Aid Funding Increased in New Budget', 'url': 'https://example.com/news10', 'description': 'The government has announced more funding for legal aid services.', 'source': 'Justice News'}
            ]
        return jsonify({'articles': articles})
    except Exception as e:
        return jsonify({'articles': [], 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)