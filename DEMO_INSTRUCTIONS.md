# Demo Instructions for OpenAI Flask Application

## Quick Start

1. **Set up your API key:**
   ```bash
   echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open in browser:**
   - Local: http://localhost:5000
   - Public: Your deployed URL

## Demo Features to Show

### 1. Text Generation
- **Demo**: "Write a short story about a robot learning to paint"
- **Show**: Real-time text generation with GPT-3.5
- **Highlight**: Custom prompts, creative writing

### 2. Image Generation
- **Demo**: "A futuristic city with flying cars and neon lights"
- **Show**: DALL-E 3 image generation
- **Highlight**: High-quality, creative image creation

### 3. Structured Data
- **Demo**: "Generate product information for a smartphone"
- **Show**: JSON formatted output
- **Highlight**: Structured, parseable data

### 4. Image Analysis
- **Demo**: Upload a photo (any image)
- **Show**: AI vision analysis
- **Highlight**: Detailed image description

### 5. Audio Processing
- **Speech to Text**: Record or upload audio
- **Text to Speech**: Convert text to audio with different voices
- **Translation**: Speak in English, get audio in another language

## Deployment Options

### Heroku (Recommended)
1. Install Heroku CLI
2. Create new app: `heroku create your-app-name`
3. Set environment variable: `heroku config:set OPENAI_API_KEY=your_key`
4. Deploy: `git push heroku main`

### Railway
1. Connect GitHub repository
2. Set environment variables in dashboard
3. Deploy automatically

### PythonAnywhere
1. Upload files via web interface
2. Configure web app to use `app.py`
3. Set environment variables in web app settings

## Technical Highlights

- **Modern UI**: Bootstrap 5 with responsive design
- **Error Handling**: Graceful API key validation
- **File Upload**: Support for images and audio
- **Real-time Feedback**: Loading states and progress indicators
- **Multiple AI Models**: GPT-3.5, DALL-E 3, Whisper, TTS
- **Production Ready**: Gunicorn configuration included

## Troubleshooting

- **API Key Issues**: Check .env file and environment variables
- **File Upload**: Ensure file types are supported
- **Network Issues**: Check internet connection and API access
- **Deployment**: Verify environment variables are set on hosting platform

## File Structure
```
FlaskHW1/
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies
├── Procfile              # Heroku deployment
├── templates/
│   └── index.html        # Main UI
├── static/
│   ├── css/style.css     # Custom styles
│   └── js/app.js         # Frontend logic
└── README.md             # Documentation
```

The application is ready for demonstration and deployment!
