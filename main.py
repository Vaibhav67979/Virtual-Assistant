import pyttsx3

# Initialize the pyttsx3 engine with the eSpeak driver
engine = pyttsx3.init('espeak')

# Get the list of available voices
voices = engine.getProperty('voices')

# Print the list of available voices
for voice in voices.values():
    print(voice.id)
