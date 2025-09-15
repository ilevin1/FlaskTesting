#!/usr/bin/env python3
"""
Test script to verify the Flask application setup
"""

import os
import sys
from dotenv import load_dotenv

def test_environment():
    """Test if environment variables are properly set"""
    print("Testing environment setup...")
    
    # Load environment variables
    load_dotenv()
    
    # Check for OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment variables")
        print("   Please create a .env file with your OpenAI API key")
        return False
    elif api_key == 'your_openai_api_key_here':
        print("❌ OPENAI_API_KEY is set to placeholder value")
        print("   Please replace with your actual OpenAI API key")
        return False
    else:
        print("✅ OPENAI_API_KEY is set")
    
    return True

def test_imports():
    """Test if all required packages can be imported"""
    print("\nTesting package imports...")
    
    required_packages = [
        'flask',
        'openai',
        'PIL',
        'requests',
        'dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                import PIL
            else:
                __import__(package)
            print(f"✅ {package} imported successfully")
        except ImportError:
            print(f"❌ {package} not found")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    return True

def test_flask_app():
    """Test if Flask app can be imported and initialized"""
    print("\nTesting Flask application...")
    
    try:
        from app import app
        print("✅ Flask app imported successfully")
        
        # Test if app has required routes
        routes = [str(rule) for rule in app.url_map.iter_rules()]
        required_routes = [
            '/',
            '/generate_text',
            '/generate_image',
            '/generate_structured_data',
            '/analyze_image',
            '/speech_to_text',
            '/text_to_speech',
            '/translate_audio'
        ]
        
        missing_routes = []
        for route in required_routes:
            if not any(route in r for r in routes):
                missing_routes.append(route)
        
        if missing_routes:
            print(f"❌ Missing routes: {', '.join(missing_routes)}")
            return False
        else:
            print("✅ All required routes found")
        
        return True
        
    except Exception as e:
        print(f"❌ Error importing Flask app: {e}")
        return False

def main():
    """Run all tests"""
    print("Flask OpenAI Demo - Setup Test")
    print("=" * 40)
    
    tests = [
        test_environment,
        test_imports,
        test_flask_app
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo run the application:")
        print("  python app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
