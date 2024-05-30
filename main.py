#!/usr/bin/env python3
##
# Modules
##


import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from utils import *



            
ELEVENLABS_API_KEY = Utils.getKeyAPI()

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)



def text_to_speech(text: str) -> str:
    response = client.text_to_speech.convert(
        voice_id="ZQe5CZNOzWyzPSCn5a3c", 
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.5,
            style=0.2,
            use_speaker_boost=True
        ),
    )

    # play(response)

    save_file_path = f"audio/{uuid.uuid4()}.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: Un nouveau fichier audio a été enregistré avec succès !")

    return save_file_path


texte = Utils.getText()


text_to_speech(text=texte)






