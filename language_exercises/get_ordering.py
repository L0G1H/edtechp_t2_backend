import random

class Ordering_Client:
    def __init__(self) -> None:
        with open("../data/untranslated_sentences.txt", encoding="utf-8") as f:
            self.sentences = f.read().splitlines()

    def get_ordering_exercise(self) -> dict:
        sentence = random.choice(self.sentences).split()

        shuffled_sentence = sentence.copy()

        random.shuffle(shuffled_sentence)

        return {"type": "ordering", "question": shuffled_sentence, "answer": sentence}
