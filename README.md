# Sahayak AI

Private Hindi document guidance designed for Snapdragon-powered HP PCs.

## Overview

Sahayak AI helps users understand important documents in simple Hindi. Users can upload or photograph documents such as government notices, electricity bills, medical reports, bank letters, and forms.

The app identifies important details, creates a Hindi summary, highlights dates and amounts, suggests next actions, and supports voice-based questions.

## Problem

Many documents use formal or technical language that is difficult to understand. Cloud-based AI tools may also create privacy concerns because users must upload sensitive medical, financial, or personal documents.

## Solution

Sahayak AI is designed to process documents locally on Snapdragon-powered HP PCs.

Users can:

- Upload a PDF or document image
- Get a simple Hindi summary
- Extract important dates, amounts, and deadlines
- Receive an action checklist
- Ask questions in Hindi through voice
- Keep sensitive document data on the device

## Snapdragon and Qualcomm AI Hub Integration

Sahayak AI is designed for on-device AI inference on Snapdragon-powered HP PCs.

Planned AI components:

- OCR for extracting document text
- Vision-language model for document understanding
- Local language model for Hindi explanations
- Whisper speech-to-text for Hindi voice questions
- Qualcomm AI Hub optimized models using Qualcomm AI Runtime or GenieX

This on-device approach improves privacy, reduces dependence on internet connectivity, and uses the Snapdragon NPU for efficient AI processing.

## Prototype Flow

1. User uploads a PDF or document image.
2. The app extracts and understands document content.
3. Sahayak AI generates a Hindi summary.
4. Important deadlines, amounts, and next actions are shown.
5. The user asks a follow-up question by voice or text.
6. The assistant provides a clear Hindi response.

## Tech Stack

- Python
- Streamlit
- PDF and image processing
- Qualcomm AI Hub
- Qualcomm AI Runtime / GenieX
- Snapdragon X NPU
- Vision-language model
- Qwen or another compact local LLM
- Whisper speech recognition
