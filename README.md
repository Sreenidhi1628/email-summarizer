# email-summarizer
AI-powered email summarizer built with Flask and Gemini API that condenses long email threads into concise, readable summaries.


# 📧 Email Summarizer

An AI-powered web application that automatically summarizes lengthy emails into concise, easy-to-read summaries, helping users quickly grasp key information without reading through entire threads.

## Features
- Summarizes long emails into short, digestible summaries
- Built with Flask for a lightweight, responsive backend
- Powered by Google's Gemini API for natural language understanding
- Simple, clean web interface for pasting/uploading email content

## Tech Stack
- **Backend:** Python, Flask
- **AI/NLP:** Gemini API
- **Frontend:** HTML, CSS, JavaScript

## How It Works
1. User inputs or uploads email content
2. The text is sent to the Gemini API with a summarization prompt
3. The app returns a concise summary highlighting key points

## Setup
\`\`\`bash
git clone https://github.com/Sreenidhi1628/email-summarizer.git
cd email-summarizer
pip install -r requirements.txt
python app.py
\`\`\`

## Future Improvements
- Support for batch email summarization
- Integration with Gmail API for direct inbox access
- Sentiment/priority tagging for summarized emails
