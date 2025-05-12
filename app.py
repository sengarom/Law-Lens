from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from flask import Flask, render_template, request, jsonify
from huggingface_hub import login

app = Flask(__name__)

# Authenticate with Hugging Face
login("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")

# Load the Hugging Face LLaMA model and tokenizer after authentication
model_name = "meta-llama/Llama-2-7b-chat-hf"  # Replace with the desired LLaMA model

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Generate response using Hugging Face LLaMA model
        try:
            inputs = tokenizer(f"You are a legal assistant chatbot. Provide accurate legal information.\nUser: {user_input}\nAssistant:", return_tensors="pt")
            inputs = {key: value.to(model.device) for key, value in inputs.items()}

            outputs = model.generate(**inputs, max_length=200, temperature=0.7)
            chatbot_reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract the assistant's response
            chatbot_reply = chatbot_reply.split("Assistant:")[-1].strip()

            return jsonify({"reply": chatbot_reply})
        except Exception as e:
            return jsonify({"error": "Failed to process your request. Please try again later."}), 500

    return render_template('chatbot.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)