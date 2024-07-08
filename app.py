from flask import Flask, render_template, request, jsonify
from intelligent_text_completion import complete_text
from contextual_phrase_suggestions import suggest_phrases
from error_detection_correction import check_errors
from higher_level_writing_support import summarize_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complete', methods=['POST'])
def complete():
    prompt = request.json['prompt']
    completion = complete_text(prompt)
    return jsonify({'text': completion})

@app.route('/suggest', methods=['POST'])
def suggest():
    prompt = request.json['prompt']
    suggestions = suggest_phrases(prompt)
    return jsonify({'suggestions': suggestions})

@app.route('/check', methods=['POST'])
def check():
    text = request.json['text']
    corrections = check_errors(text)
    return jsonify({'corrections': corrections})

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    summary = summarize_text(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
