import speechrecognition as sr

def recognizespeechfrommic(recognizer, microphone):
    """Transcribe speech from recorded audio."""
    # Check that recognizer and microphone arguments are of correct type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("recognizer must be speech_recognition.Recognizer instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("microphone must be speech_recognition.Microphone instance")

    # Record audio from the microphone
    with microphone as source:
        print("Say something in Nepali:")
        audio = recognizer.listen(source)

    # Set up the response
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Try recognizing the speech in the recording
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="ne-NP")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def main():
    # Create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Adjust for ambient noise once at the beginning
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce duration to minimize delay

    while True:
        command = input("Press Enter to start listening or type 'exit' to quit: ").lower().strip()
        if command == 'exit':
            break

        response = recognize_speech_from_mic(recognizer, microphone)

        if response["success"]:
            print("You said: {}".format(response["transcription"]))
        else:
            print("Error: {}".format(response["error"]))

if __name == "__main":
    main()