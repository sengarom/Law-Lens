<div align="center">
  <img src="placeholder_logo.png" alt="Law Lens Logo" width="200"/>
  <h1>Law Lens ⚖️</h1>
  <p>Your AI-Powered Legal Companion</p>
</div>

---

# 🚦 Before You Start: Essential Setup

> **To use Law Lens, you must set up a few things first!**

- **Hugging Face Account:**
  - Create a free account at [huggingface.co](https://huggingface.co/).
  - Run `huggingface-cli login` in your terminal and paste your access token to authenticate.
- **Hugging Face Model Cache Location:**
  - To save disk space and speed up downloads, set your cache location (optional but recommended):
    ```powershell
    $env:HF_HOME = "O:\hf_cache"
    # To make this permanent, add to your user environment variables.
    ```
- **newsdata.io API Key:**
  - Get a free API key at [newsdata.io](https://newsdata.io/).
  - Replace the placeholder in `app.py` with your API key if you want your own news quota.
- **Python & Node.js:**
  - Make sure you have Python 3.8+ and Node.js 16+ installed.

---

## 🌟 Why Law Lens?

- **Empower Yourself:** No more legal jargon confusion—get clear, concise answers.
- **Stay Updated:** Never miss important legal news or changes in the law.
- **Accessible to All:** Free, user-friendly, and designed for everyone.

---

## ✨ Features

*   📚 **Comprehensive Legal Information:** Dive into an extensive library of legal articles, guides, and resources.
*   📰 **Latest Legal News:** Stay informed with up-to-the-minute developments and trends in the legal world.
*   🤖 **AI Chatbot Assistant:** Get instant, insightful answers to your legal queries from our cutting-edge AI chatbot.

## 🚀 Technology Stack

*   **Backend:** Python (Flask)
*   **Frontend:** HTML, CSS, JavaScript
*   **Styling:** Tailwind CSS - Modern, beautiful, and responsive
*   **AI/Chatbot:** TinyLlama-1.1B (via Hugging Face Transformers)

---

## 🖥️ Quick Start (Windows)

1. **Clone the Repository:**
    ```powershell
    git clone https://github.com/your-username/LawLens.git
    cd LawLens
    ```
2. **Set Up Python Virtual Environment:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. **Install Python Dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```
4. **Install Node.js Dependencies (for Tailwind CSS):**
    ```powershell
    npm install
    ```
5. **Build Tailwind CSS:**
    ```powershell
    npm run build:css
    ```
6. **Run the App:**
    ```powershell
    python app.py
    ```
7. **Open in Browser:**
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ Installation & Setup (macOS/Linux)

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/LawLens.git
    cd LawLens
    ```
2.  **Set Up Python Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Install Node.js Dependencies (for Tailwind CSS):**
    ```bash
    npm install
    ```
5.  **Build Tailwind CSS:**
    ```bash
    npm run build:css
    ```
6.  **Run the App:**
    ```bash
    python app.py
    ```
7.  **Open in Browser:**
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Tips & Tricks

- **Model Download:** TinyLlama-1.1B is small and fast, but the first run will download weights (~1GB). Make sure you have a stable internet connection.
- **Authentication:** Always log in with `huggingface-cli login` before running the app.
- **Cache Location:** Set `HF_HOME` to move the Hugging Face cache to a fast drive (SSD recommended).
- **Customization:** Tweak the chatbot, add new legal resources, or style the frontend with Tailwind for a unique look!

---

## 🤝 Contributing

We love new ideas! Whether it's a bug fix, new feature, or design improvement, your contribution is welcome. See the steps below to get started.

1.  Fork the Project
2.  Create your Awesome Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📜 License

This project is licensed under the ISC License. See the [LICENSE](LICENSE) file for more details.

---

<p align="center" style="font-size:1.2em;">Made with ❤️, Python, and a passion for accessible justice.<br>Follow us for updates and join our mission!</p>
