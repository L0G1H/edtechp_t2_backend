import os
from google.cloud import texttospeech_v1
import random
import base64


class Exercise_Generator:
    def __init__(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                                    "google_credentials/google_credentials.json")
        self.client = texttospeech_v1.TextToSpeechClient()

        with open("../data/untranslated_sentences.txt", encoding="utf-8") as f:
            self.untranslated_sentences = f.read().splitlines()

        self.fill_blank_sentences = []

        with open("../data/fill_blank_sentences.txt", encoding="utf-8") as f:
            for raw_sentence in f.read().splitlines():
                split_sentence = raw_sentence.split("|")

                self.fill_blank_sentences.append([*split_sentence])

        self.translated_words = []
              
        with open("../data/translated_words.txt", encoding="utf-8") as f:
            for raw_sentence in f.read().splitlines():
                split_sentence = raw_sentence.split("|")
                
                self.translated_words.append([*split_sentence])

    def get_listening_exercise(self) -> dict:
        exercise = random.choice(self.untranslated_sentences)

        synthesis_input = texttospeech_v1.SynthesisInput(text=exercise)

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

        return {"type": "listening", "question": response.audio_content, "options": None, "answer": exercise}

    def get_ordering_exercise(self) -> dict:
        exercise = random.choice(self.untranslated_sentences).split()

        shuffled_sentence = exercise.copy()

        random.shuffle(shuffled_sentence)

        return {"type": "ordering", "question": shuffled_sentence, "options": None, "answer": exercise}

    def get_fill_the_blank(self) -> dict:
        exercise = random.choice(self.fill_blank_sentences)

        options = exercise[1:].copy()

        random.shuffle(options)

        return {"type": "fill_the_blank", "question": exercise[0], "options": options, "answer": exercise[1]}


    def get_translate(self, answer_in_lt: bool = True) -> dict:
        answer_idx = random.randint(0, len(self.translated_words) - 1)
        answer = self.translated_words[answer_idx]

        translated_words_copy = [*self.translated_words[:answer_idx], *self.translated_words[answer_idx + 1:]]

        options = [answer] + random.sample(translated_words_copy, 3)

        random.shuffle(options)

        if answer_in_lt:
            question = answer[1]
            options = [option[0] for option in options]
            answer = answer[0]
            suffix = "lt"
        else:
            question = answer[0]
            options = [option[1] for option in options]
            answer = answer[1]
            suffix = "ua"


        return {"type": f"translate_{suffix}", "question": question, "options": options, "answer": answer}
