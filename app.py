from flask import Flask, request, send_file, Response, jsonify
import edge_tts
import asyncio
import io
import os

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return send_file('文字轉語音轉換器.html')

@app.route('/api/speak', methods=['POST'])
def speak():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400
        
    text = data.get('text')
    voice = data.get('voice', 'zh-HK-HiuGaaiNeural')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    async def _generate_audio():
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data

    try:
        audio_content = asyncio.run(_generate_audio())
        return Response(audio_content, mimetype='audio/mpeg')
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
