import language_exercises


generator = language_exercises.Exercise_Generator()

listening = generator.get_listening_exercise()
print(listening)

ordering = generator.get_ordering_exercise()
print(ordering)

fill = generator.get_fill_the_blank()
print(fill)

translate_lt = generator.get_translate(True)
print(translate_lt)

translate_ua = generator.get_translate(False)
print(translate_ua)

print(len(listening["question"]))

with open("output.mp3", "wb") as out:
    out.write(listening["question"])