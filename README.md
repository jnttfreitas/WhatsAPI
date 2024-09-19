# Transcription API

This is a simple API built with Flask and Whisper for transcribing audio files.

## Endpoints

### POST /transcribe

Transcribes an audio file.

**Request:**

- **Multipart/Form-Data**: An audio file with the field name `audio`.

**Response:**

- **200 OK**: JSON object with the transcription result.

- **400 Bad Request**: If no audio file is provided.