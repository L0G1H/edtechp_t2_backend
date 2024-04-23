import get_listening
import get_ordering


sentences_client = get_ordering.Ordering_Client()

exercise = sentences_client.get_ordering_exercise()

audio_client = get_listening.Listening_Client()

exercise_2 = audio_client.get_listening_exercise()

print(exercise)

print(exercise_2)