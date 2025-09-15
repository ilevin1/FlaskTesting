# Quick Setup Instructions

## 1. Set up your OpenAI API Key

Create a `.env` file in the project root with your OpenAI API key:

```bash
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
```

Replace `your_actual_api_key_here` with your real OpenAI API key.

## 2. Run the application

```bash
python app.py
```

## 3. Access the application

Open your browser and go to: http://localhost:5000

## 4. Test the setup

Run the test script to verify everything is working:

```bash
python test_setup.py
```

## Getting an OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy the key and add it to your `.env` file

## Deployment

For public deployment, you'll need to set the environment variable on your hosting platform:

- **Heroku**: Set in the dashboard under Settings > Config Vars
- **Railway/Render**: Set in the environment variables section
- **PythonAnywhere**: Set in the Web app configuration

The application is ready to deploy with the included `Procfile` for Heroku/Railway.
