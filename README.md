# Text to Speech Converter

A simple web app that converts typed text into speech (audio) using [Streamlit](https://streamlit.io/) and [gTTS](https://gtts.readthedocs.io/) (Google Text-to-Speech).

## Features

- Enter any text and convert it to spoken audio
- Choose from multiple languages: English, Urdu, Hindi, Arabic, French, Spanish
- Listen to the generated audio directly in the browser
- Download the audio as an MP3 file

## Requirements

- Python 3.8+
- [streamlit](https://pypi.org/project/streamlit/)
- [gTTS](https://pypi.org/project/gTTS/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/text-to-voice.git
   cd text-to-voice
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install streamlit gTTS
   ```

## Usage

Run the app with Streamlit:

```bash
streamlit run app.py
```

This will open the app in your default browser (usually at `http://localhost:8501`).

1. Type or paste the text you want to convert.
2. Select the language.
3. Click **Convert to Speech**.
4. Play the generated audio or click **Download Audio** to save it as `speech.mp3`.

## Project Structure

```
.
├── app.py        # Main Streamlit application
└── README.md      # Project documentation
```

## License

This project is open source and available under the [MIT License](LICENSE).
