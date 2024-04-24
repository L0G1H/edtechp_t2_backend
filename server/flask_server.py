from flask import Flask, jsonify
from language_exercises import Exercise_Generator


app = Flask(__name__)
exercise_generator = Exercise_Generator()

@app.route("/listening")
def get_listening_exercise():
    exercise = exercise_generator.get_listening_exercise()
    return jsonify(exercise)

@app.route("/ordering")
def get_ordering_exercise():
    exercise = exercise_generator.get_ordering_exercise()
    return jsonify(exercise)

@app.route("/fill_the_blank")
def get_fill_the_blank_exercise():
    exercise = exercise_generator.get_fill_the_blank()
    return jsonify(exercise)

@app.route("/translate_lt")
def get_translate_lt():
    exercise = exercise_generator.get_translate(answer_in_lt=True)
    return jsonify(exercise)

@app.route("/translate_ua")
def get_translate_ua():
    exercise = exercise_generator.get_translate(answer_in_lt=False)
    return jsonify(exercise)

if __name__ == "__main__":
    app.run(debug=True)
