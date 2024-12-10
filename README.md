# Music Generator Web App

## Introduction
This project is a simple Music Generator Web Application where users can generate music by providing prompts and selecting keywords. 
The generated music can be played directly from the web interface, and a history of generated music is maintained for easy access.

## Features
- Generate music based on user prompts and keywords.
- Play generated music directly on the webpage.
- Maintain a list of previously generated music.
- Responsive design for user-friendly experience.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Music Model**: Audiocraft's MusicGen
- **Environment**: Google Colab


## Usage

Follow these steps to use the Music Generator Web App:

1. **Enter a music prompt**:
   - In the input box labeled "Enter a music prompt," type a description of the kind of music you want.
   - For example:
     - "Relaxing acoustic guitar melody."
     - "Epic orchestral soundtrack."
     - "Calm jazz piano background."

2. **Set the duration**:
   - Choose the duration for the generated music using the input box labeled "Duration (seconds)."
   - You can select a value between **5** and **30 seconds**.

3. **Choose optional keywords**:
   - Click on the provided keyword buttons (e.g., "Acoustic", "Jazz", "Relaxing") to add additional styles or characteristics to your music prompt.

4. **Generate music**:
   - Click the **"Generate Music"** button to create your music. The system will process your input and generate a music file.

5. **View and play generated music**:
   - Once the music is generated, it will appear in the **"Generated Music List."**
   - Click on the file name in the list to play it using the audio player.

6. **Clear the prompt** (optional):
   - If you want to reset the prompt input, click the **"Clear Prompt"** button.

---

### Example Workflow:
- **Prompt**: "Calm and relaxing piano melody."
- **Duration**: 15 seconds.
- **Keywords**: "Piano", "Relaxing."
- **Generated Result**: A calming piano track ideal for a meditative session.



