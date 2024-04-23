import os
from google.cloud import texttospeech_v1
import random


class Listening_Client:
    def __init__(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                                    "google_credentials/google_credentials.json")
        self.client = texttospeech_v1.TextToSpeechClient()

        with open("../data/untranslated_sentences.txt", encoding="utf-8") as f:
            self.sentences = f.read().splitlines()

    def get_listening_exercise(self) -> dict:
        sentence = random.choice(self.sentences)

        synthesis_input = texttospeech_v1.SynthesisInput(text=sentence)

        voice = texttospeech_v1.VoiceSelectionParams(
            language_code="lt-LT",
            ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
        )

        audio_config = texttospeech_v1.AudioConfig(
            audio_encoding=texttospeech_v1.AudioEncoding.MP3
        )

        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        return {"type": "listening", "question": response.audio_content, "answer": sentence}
