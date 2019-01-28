# text to speech
from gtts import gTTS

# The greeting to convert to audio 
greeting = 'GREETING TEXT GOES HERE'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the greeting and language to gtts at normal speed 
text_to_speech = gTTS(text=greeting, lang=language, slow=False) 
  
# Saving the converted audio as an mp3 file
text_to_speech.save("audio-files/greeting-file-name.mp3") 
  

