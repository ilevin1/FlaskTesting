#!/usr/bin/env python3
"""
Startup script for the OpenAI Flask Demo Application
"""

import os
import sys
from dotenv import load_dotenv

def check_api_key():
    """Check if API key is properly configured"""
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key or api_key == 'your_openai_api_key_here':
        print("❌ OPENAI_API_KEY not configured!")
        print("\nTo fix this:")
        print("1. Get your API key from https://platform.openai.com/")
        print("2. Create a .env file with: OPENAI_API_KEY=your_key_here")
        print("3. Or set the environment variable: export OPENAI_API_KEY=your_key_here")
        return False
    
    print("✅ OpenAI API key configured")
    return True

def main():
    """Main startup function"""
    print("🤖 OpenAI Flask Demo Application")
    print("=" * 40)
    
    # Check API key
    if not check_api_key():
        print("\n⚠️  You can still run the app, but API features won't work.")
        response = input("\nContinue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    print("\n🚀 Starting Flask application...")
    print("📱 Open your browser to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    # Import and run the app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
