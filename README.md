# Text to Speech Converter (Edge TTS Web Interface)

一個簡單、免費且高質素的線上文字轉語音工具，使用 Microsoft Edge 的 TTS 引擎，支援粵語、國語、英文、日文等多種語言，具備 10000 字長文轉換功能。

A simple, free, and high-quality online text-to-speech tool powered by Microsoft Edge's TTS engine. Supports Cantonese, Mandarin, English, Japanese, and more, with support for long text conversion (up to 10,000 characters).

## 🌍 線上試用 / Live Demo

**[👉 點擊這裡使用 (Click Here)](https://person-edge-tts.onrender.com)**

---

## ✨ 特色 / Features

*   **完全免費 (Free)**: 無需 API Key，無隱藏收費。
*   **高品質語音 (High Quality)**: 使用微軟 Azure Neural TTS 技術 (Edge 瀏覽器同款)。
*   **多語言支援 (Multi-language)**:
    *   🇭🇰 粵語 (Cantonese - HiuGaai, WanLung)
    *   🇨🇳 國語 (Mandarin - Xiaoyi, Yunxi, etc.)
    *   🇹🇼 台灣國語 (Taiwanese Mandarin - HsiaoChen, YunJhe)
    *   🇺🇸🇬🇧 英語 (English - Aria, Sonia)
    *   🇯🇵 日語 (Japanese - Nanami)
*   **長文支援 (Long Text)**: 支援長達 10,000 字的轉換，自動分段處理。
*   **下載功能 (Download)**: 生成後可直接下載 MP3 檔案。
*   **響應式設計 (Responsive)**: 手機、平板、電腦皆可使用。

## 🛠️ 技術棧 / Tech Stack

*   **Backend**: Python (Flask)
*   **TTS Engine**: [edge-tts](https://github.com/rany2/edge-tts) library
*   **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
*   **Deployment**: Render (Web Service with Gunicorn)

## 🚀 本地執行 / Run Locally

如果你想在自己的電腦上運行：

1.  **Clone the repository**
    ```bash
    git clone https://github.com/JamesCheng625/person_edge-tts.git
    cd person_edge-tts
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    python app.py
    ```

4.  **Open in browser**
    Visit `http://localhost:5000`

## 📝 License

MIT
