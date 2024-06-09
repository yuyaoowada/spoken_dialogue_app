import requests


class Voicevox:
    def __init__(self, host="127.0.0.1", port=50021):
        self.host = host
        self.port = port

    def get_voicevox_audio(self, text=None, speaker=1):  # VOICEVOX:ずんだもん
        query_payload = {"text": text, "speaker": speaker}
        query_response = requests.post(
            f"http://{self.host}:{self.port}/audio_query",
            params=query_payload)
        if query_response.status_code != 200:
            raise Exception("Audio query failed.")
        audio_query = query_response.json()

        synthesis_payload = {"speaker": speaker}
        synthesis_response = requests.post(
            f"http://{self.host}:{self.port}/synthesis",
            params=synthesis_payload, json=audio_query)
        if synthesis_response.status_code != 200:
            raise Exception("Audio synthesis failed.")

        return synthesis_response.content

    # def speak(self, text=None, speaker=1):  # VOICEVOX:ずんだもん
    #
    #     params = (
    #         ("text", text),
    #         ("speaker", speaker)  # 音声の種類をInt型で指定
    #     )
    #
    #     init_q = requests.post(
    #         f"http://{self.host}:{self.port}/audio_query",
    #         params=params
    #     )
    #
    #     res = requests.post(
    #         f"http://{self.host}:{self.port}/synthesis",
    #         headers={"Content-Type": "application/json"},
    #         params=params,
    #         data=json.dumps(init_q.json())
    #     )
    #

