from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files.get('audio')
    
    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400
    
    # Save the file to a temporary location
    audio_path = '/tmp/audio.wav'
    audio_file.save(audio_path)
    
    # Transcribe the audio
    result = model.transcribe(audio_path)
    
    # Return the transcription
    return jsonify({"transcription": result['text']}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
