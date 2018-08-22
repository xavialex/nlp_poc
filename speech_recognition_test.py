import speech_recognition as sr

# r = sr.Recognizer()
# mic = sr.Microphone()

# try:
#     print("A moment of silence, please...")
#     with mic as source: r.adjust_for_ambient_noise(source)
#     print("Set minimum energy threshold to {}".format(r.energy_threshold))
#     while True:
#         print("Say something!")
#         with mic as source: audio = r.listen(source)
#         print("Got it! Now to recognize it...")
#         try:
#             # recognize speech using Google Speech Recognition
#             value = r.recognize_google(audio)

#             print("You said {}".format(value))

#         except sr.UnknownValueError:
#             print("Oops! Didn't catch that")
#         except sr.RequestError as e:
#             print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
# except KeyboardInterrupt:
#     pass

def audio_acquisition(r, mic):
    """Return an input audio from a microphone.

    Args:
        r: Recognizer instance.
        mic: Microphone instance.

    Returns:
        audio: Audio clip in the SpeechRecognition format.

    """
    print("Say something!")
    with mic as source: 
        audio = r.listen(source)

    return audio

def speech_recognition(r, audio):
    """Take a microphone recorded audio and process it.

    Args:
        r: Recognizer instance.
        audio: Properly converted audio from microphone by PyAudio.

    Returns:
        response (str): Feasible to text translation with the higher confidence.

    """
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_sphinx(audio)  # language='es-ES'
        print("You said {}".format(value))
        return value
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    # Apply and ambient noise adjustment for the microphone
    with mic as source: 
        r.adjust_for_ambient_noise(source)

    while True:
        try:
            audio = audio_acquisition(r, mic)
            response = speech_recognition(r, audio)
        except KeyboardInterrupt:
            print("Ending process")
            break

if __name__ == '__main__':
    main()