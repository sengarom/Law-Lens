from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-chat-hf")

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

if __name__ == '__main__':
    app.run(debug=True)