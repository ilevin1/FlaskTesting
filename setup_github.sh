#!/bin/bash

# Setup script for GitHub deployment to Render

echo "🚀 Setting up GitHub repository for Render deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git branch -M main
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: OpenAI Flask Demo with all features"

echo "✅ Git repository ready!"
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub (https://github.com/new)"
echo "2. Copy the repository URL"
echo "3. Run these commands:"
echo "   git remote add origin YOUR_GITHUB_REPO_URL"
echo "   git push -u origin main"
echo ""
echo "4. Then deploy to Render:"
echo "   - Go to https://render.com"
echo "   - Connect your GitHub repository"
echo "   - Use the settings from RENDER_DEPLOYMENT.md"
echo "   - Don't forget to set OPENAI_API_KEY environment variable!"
