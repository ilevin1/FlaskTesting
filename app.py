import os
import json
import base64
import io
from flask import Flask, render_template, request, jsonify, send_file
from openai import OpenAI
from PIL import Image
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
if not api_key or api_key == 'your_openai_api_key_here':
    print("Warning: OPENAI_API_KEY not set. Please set your OpenAI API key in the .env file")
    client = None
else:
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"Warning: Error initializing OpenAI client: {e}")
        client = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        response = client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        
        generated_text = response.choices[0].message.content
        return jsonify({'generated_text': generated_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_image', methods=['POST'])
def generate_image():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        data = request.get_json()
        description = data.get('description', '')
        
        if not description:
            return jsonify({'error': 'Image description is required'}), 400
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=description,
            size="1024x1024",
            quality="standard",
            n=1
        )
        
        image_url = response.data[0].url
        return jsonify({'image_url': image_url})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_structured_data', methods=['POST'])
def generate_structured_data():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        response = client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[
                {"role": "user", "content": f"Generate structured data for: {prompt}. Return the response as a valid JSON object with appropriate fields."}
            ],
            response_format={"type": "json_object"}
        )
        
        structured_data = json.loads(response.choices[0].message.content)
        return jsonify({'structured_data': structured_data})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({'error': 'No image file selected'}), 400
        
        # Read and encode image
        image_data = image_file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        
        response = client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this image and provide a detailed description of what you see."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        )
        
        analysis = response.choices[0].message.content
        return jsonify({'analysis': analysis})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No audio file selected'}), 400
        
        # Transcribe audio - convert FileStorage to proper file object
        audio_file.seek(0)
        import io
        audio_data = audio_file.read()
        audio_io = io.BytesIO(audio_data)
        audio_io.name = audio_file.filename
        
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_io
        )
        
        return jsonify({'transcript': transcript.text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        data = request.get_json()
        text = data.get('text', '')
        voice = data.get('voice', 'alloy')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        
        # Save audio to temporary file
        audio_data = response.content
        audio_file = io.BytesIO(audio_data)
        
        return send_file(
            audio_file,
            mimetype='audio/mpeg',
            as_attachment=True,
            download_name='speech.mp3'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/translate_audio', methods=['POST'])
def translate_audio():
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file.'}), 400
            
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        target_language = request.form.get('target_language', 'Spanish')
        
        if audio_file.filename == '':
            return jsonify({'error': 'No audio file selected'}), 400
        
        # Transcribe audio - convert FileStorage to proper file object
        audio_file.seek(0)
        import io
        audio_data = audio_file.read()
        audio_io = io.BytesIO(audio_data)
        audio_io.name = audio_file.filename
        
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_io
        )
        
        # Translate text
        translation_prompt = f"Translate the following text to {target_language}: {transcript.text}"
        translation_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": translation_prompt}
            ],
        )
        
        translated_text = translation_response.choices[0].message.content
        
        # Generate speech in target language
        speech_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=translated_text
        )
        
        audio_data = speech_response.content
        audio_file = io.BytesIO(audio_data)
        
        return send_file(
            audio_file,
            mimetype='audio/mpeg',
            as_attachment=True,
            download_name=f'translation_{target_language.lower()}.mp3'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
