from gtts import gTTS
import io
import pygame

def speak_text(text):

    tts = gTTS(text=text, lang='ne')
    # Save the audio to an in-memory file
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)


    pygame.mixer.init()


    pygame.mixer.music.load(mp3_fp, 'mp3')


    pygame.mixer.music.play()

    # Wait until the sound finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

#Example text in Nepali
text = "२५ जेठ,काठमाडौं । प्रधानमन्त्री पुष्पकमल दाहाल प्रचण्डले जनतालाई राम्रो सुविधा दिएर मात्र संघीयता बलियो हुने बताएका छन् ।"
speak_text(text)