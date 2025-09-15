# Render Deployment Guide

## Quick Deploy to Render

### Method 1: Connect GitHub Repository (Recommended)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Name:** `openai-flask-demo`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
     - **Plan:** Free

3. **Set Environment Variables:**
   - In Render dashboard, go to your service
   - Click "Environment" tab
   - Add: `OPENAI_API_KEY` = your actual API key

### Method 2: Direct Deploy (Alternative)

1. **Create render.yaml** (already created)
2. **Upload files to Render:**
   - Go to render.com
   - Click "New +" → "Blueprint"
   - Upload your project folder
   - Set environment variables

## Environment Variables Required

- `OPENAI_API_KEY` - Your OpenAI API key

## Post-Deployment

1. **Test your app** at the provided Render URL
2. **Update your demo instructions** with the new public URL
3. **Share the link** for class demonstration

## Troubleshooting

- **Build fails:** Check Python version compatibility
- **App crashes:** Check environment variables are set
- **API errors:** Verify OpenAI API key is correct
- **Static files:** Ensure all files are in the repository

## Free Tier Limits

- **750 hours/month** (enough for continuous running)
- **512MB RAM**
- **Automatic sleep** after 15 minutes of inactivity
- **Cold start** takes ~30 seconds after sleep

Your app will be available at: `https://your-app-name.onrender.com`
