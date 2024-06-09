from spoken_dialogue_app.audio import Audio
from spoken_dialogue_app.voicevox import Voicevox


def main():
    user_input = "こんにちは"

    synthesizer = Voicevox()
    audio_data = synthesizer.get_voicevox_audio(user_input)

    player = Audio(audio_data)

    # simpleaudioだとエラーが発生したため一旦コメントアウト
    # player.play(audio_data)
    player.speak()
    print("Voicevox: 音声を再生しました。")


if __name__ == "__main__":
    main()
