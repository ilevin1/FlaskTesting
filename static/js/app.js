// Global variables
let loadingModal;

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
});

// Utility function to show loading
function showLoading() {
    loadingModal.show();
}

// Utility function to hide loading
function hideLoading() {
    loadingModal.hide();
}

// Utility function to show error
function showError(elementId, message) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `<div class="alert alert-danger">${message}</div>`;
        element.style.display = 'block';
    } else {
        console.error(`Element with id '${elementId}' not found`);
        alert(`Error: ${message}`);
    }
}

// Text Generation
async function generateText() {
    const prompt = document.getElementById('textPrompt').value.trim();
    if (!prompt) {
        showError('textResult', 'Please enter a prompt for text generation.');
        return;
    }

    showLoading();
    
    try {
        const response = await fetch('/generate_text', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();
        
        if (response.ok) {
            const generatedElement = document.getElementById('generatedText');
            if (generatedElement) {
                generatedElement.textContent = data.generated_text;
                document.getElementById('textResult').style.display = 'block';
            }
        } else {
            showError('textResult', data.error || 'Error generating text');
        }
    } catch (error) {
        showError('textResult', 'Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Image Generation
async function generateImage() {
    const description = document.getElementById('imageDescription').value.trim();
    if (!description) {
        showError('imageResult', 'Please enter an image description.');
        return;
    }

    showLoading();
    
    try {
        const response = await fetch('/generate_image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description: description })
        });

        const data = await response.json();
        
        if (response.ok) {
            document.getElementById('generatedImage').src = data.image_url;
            document.getElementById('imageResult').style.display = 'block';
        } else {
            showError('imageResult', data.error || 'Error generating image');
        }
    } catch (error) {
        showError('imageResult', 'Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Structured Data Generation
async function generateStructuredData() {
    const prompt = document.getElementById('structuredPrompt').value.trim();
    if (!prompt) {
        showError('structuredResult', 'Please enter a prompt for structured data generation.');
        return;
    }

    showLoading();
    
    try {
        const response = await fetch('/generate_structured_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();
        
        if (response.ok) {
            const structuredElement = document.getElementById('structuredData');
            if (structuredElement) {
                structuredElement.textContent = JSON.stringify(data.structured_data, null, 2);
                document.getElementById('structuredResult').style.display = 'block';
            }
        } else {
            showError('structuredResult', data.error || 'Error generating structured data');
        }
    } catch (error) {
        showError('structuredResult', 'Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Image Analysis
async function analyzeImage() {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];
    
    if (!file) {
        showError('visionResult', 'Please select an image file.');
        return;
    }

    showLoading();
    
    try {
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch('/analyze_image', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        if (response.ok) {
            const analysisElement = document.getElementById('imageAnalysis');
            if (analysisElement) {
                analysisElement.textContent = data.analysis;
                document.getElementById('visionResult').style.display = 'block';
            }
        } else {
            showError('visionResult', data.error || 'Error analyzing image');
        }
    } catch (error) {
        showError('visionResult', 'Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Speech to Text
async function speechToText() {
    const fileInput = document.getElementById('audioUpload');
    const file = fileInput.files[0];
    
    if (!file) {
        showError('speechResult', 'Please select an audio file.');
        return;
    }

    showLoading();
    
    try {
        const formData = new FormData();
        formData.append('audio', file);

        const response = await fetch('/speech_to_text', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        if (response.ok) {
            const transcribedElement = document.getElementById('transcribedText');
            if (transcribedElement) {
                transcribedElement.textContent = data.transcript;
                document.getElementById('speechResult').style.display = 'block';
            }
        } else {
            showError('speechResult', data.error || 'Error transcribing audio');
        }
    } catch (error) {
        showError('speechResult', 'Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Text to Speech
async function textToSpeech() {
    const text = document.getElementById('ttsText').value.trim();
    const voice = document.getElementById('voiceSelect').value;
    
    if (!text) {
        alert('Please enter text to convert to speech.');
        return;
    }

    showLoading();
    
    try {
        const response = await fetch('/text_to_speech', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text, voice: voice })
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'speech.mp3';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        } else {
            const data = await response.json();
            alert('Error: ' + (data.error || 'Failed to generate speech'));
        }
    } catch (error) {
        alert('Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Audio Translation
async function translateAudio() {
    const fileInput = document.getElementById('translationAudio');
    const file = fileInput.files[0];
    const targetLanguage = document.getElementById('targetLanguage').value;
    
    if (!file) {
        alert('Please select an audio file to translate.');
        return;
    }

    showLoading();
    
    try {
        const formData = new FormData();
        formData.append('audio', file);
        formData.append('target_language', targetLanguage);

        const response = await fetch('/translate_audio', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `translation_${targetLanguage.toLowerCase()}.mp3`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        } else {
            const data = await response.json();
            alert('Error: ' + (data.error || 'Failed to translate audio'));
        }
    } catch (error) {
        alert('Network error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Add event listeners for Enter key
document.addEventListener('DOMContentLoaded', function() {
    // Text generation
    document.getElementById('textPrompt').addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
            generateText();
        }
    });

    // Image generation
    document.getElementById('imageDescription').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            generateImage();
        }
    });

    // Structured data
    document.getElementById('structuredPrompt').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            generateStructuredData();
        }
    });

    // Text to speech
    document.getElementById('ttsText').addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
            textToSpeech();
        }
    });
});

// File input validation
document.getElementById('imageUpload').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file && !file.type.startsWith('image/')) {
        alert('Please select a valid image file.');
        e.target.value = '';
    }
});

document.getElementById('audioUpload').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file && !file.type.startsWith('audio/')) {
        alert('Please select a valid audio file.');
        e.target.value = '';
    }
});

document.getElementById('translationAudio').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file && !file.type.startsWith('audio/')) {
        alert('Please select a valid audio file.');
        e.target.value = '';
    }
});
