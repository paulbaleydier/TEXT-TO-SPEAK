#!/usr/bin/env python3
##
# Modules
##


# Import necessary libraries
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from elevenlabs import play


ELEVENLABS_API_KEY = "xxx"

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str) -> str:
    response = client.text_to_speech.convert(
        voice_id="ZQe5CZNOzWyzPSCn5a3c", 
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.2,
            use_speaker_boost=True
        ),
    )

    # play(response)

    save_file_path = f"{uuid.uuid4()}.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    return save_file_path

texte = "Maître Corbeau, sur un arbre perché,\nTenait en son bec un fromage.\nMaître Renard, par l'odeur alléché,\nLui tint à peu près ce langage :\nEt bonjour, Monsieur du Corbeau.\nQue vous êtes joli ! que vous me semblez beau !\nSans mentir, si votre ramage\nSe rapporte à votre plumage,\nVous êtes le Phénix des hôtes de ces bois.\nÀ ces mots, le Corbeau ne se sent pas de joie ;\nEt pour montrer sa belle voix,\nIl ouvre un large bec, laisse tomber sa proie.\nLe Renard s'en saisit, et dit : Mon bon Monsieur,\nApprenez que tout flatteur\nVit aux dépens de celui qui l'écoute.\nCette leçon vaut bien un fromage, sans doute.\nLe Corbeau honteux et confus\nJura, mais un peu tard, qu'on ne l'y prendrait plus."


text_to_speech_file(text=texte)






