# OpenAI Flask Demo Application

A comprehensive Flask web application demonstrating various OpenAI API capabilities including text generation, image creation, vision analysis, and audio processing.

## Features

### Core Features (Required)
1. **Text Generation** - Generate creative text content using GPT models
2. **Image Generation** - Create images using DALL-E 3
3. **Structured Data Output** - Generate JSON formatted responses
4. **Vision Capabilities** - Analyze and describe uploaded images
5. **Audio Processing** - Speech-to-text and text-to-speech conversion

### Bonus Features
- **Audio Translation** - Translate spoken audio to different languages
- **Modern UI** - Responsive Bootstrap-based interface
- **Real-time Processing** - Live feedback and loading states

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- pip (Python package manager)

### Installation

1. **Clone or download this repository**
   ```bash
   cd FlaskHW1
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - The application will be available on all network interfaces for public access

## Usage

### Text Generation
- Enter a prompt in the text area
- Click "Generate Text" or press Ctrl+Enter
- View the AI-generated text response

### Image Generation
- Describe the image you want to create
- Click "Generate Image"
- The generated image will be displayed

### Structured Data
- Enter a prompt for what structured data you want
- Click "Generate JSON Data"
- View the formatted JSON response

### Image Analysis
- Upload an image file
- Click "Analyze Image"
- Read the AI's description of the image

### Audio Processing
- **Speech to Text**: Upload an audio file and get transcribed text
- **Text to Speech**: Enter text and download the generated audio
- **Audio Translation**: Upload audio and get translated audio in another language

## API Endpoints

- `POST /generate_text` - Generate text content
- `POST /generate_image` - Generate images
- `POST /generate_structured_data` - Generate JSON data
- `POST /analyze_image` - Analyze uploaded images
- `POST /speech_to_text` - Convert audio to text
- `POST /text_to_speech` - Convert text to audio
- `POST /translate_audio` - Translate audio to different languages

## Deployment

For public deployment (required for class demo):

1. **Using Heroku**:
   - Install Heroku CLI
   - Create a `Procfile` with: `web: gunicorn app:app`
   - Deploy: `git push heroku main`

2. **Using PythonAnywhere**:
   - Upload files to your account
   - Configure web app to use your `app.py`
   - Set environment variables in the web app settings

3. **Using Railway/Render**:
   - Connect your GitHub repository
   - Set environment variables
   - Deploy automatically

## Environment Variables

Required:
- `OPENAI_API_KEY` - Your OpenAI API key

## File Structure

```
FlaskHW1/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Custom styles
    └── js/
        └── app.js        # Frontend JavaScript
```

## Troubleshooting

### Common Issues

1. **OpenAI API Key Error**
   - Ensure your API key is correctly set in the `.env` file
   - Verify the key has sufficient credits

2. **Module Not Found Errors**
   - Make sure you've installed all requirements: `pip install -r requirements.txt`
   - Check that you're using the correct Python environment

3. **File Upload Issues**
   - Ensure file types are supported (images: jpg, png, gif; audio: mp3, wav, m4a)
   - Check file size limits

4. **Network Errors**
   - Verify internet connection
   - Check if OpenAI API is accessible from your location

## Contributing

This is a class project. For questions or issues, please contact the course instructor.

## License

This project is for educational purposes only.
