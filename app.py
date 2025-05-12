from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch  # for device handling
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# No authentication needed for public GPT-2 model

# Load the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Generate response using GPT-2 model
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