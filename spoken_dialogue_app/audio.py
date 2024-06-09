import time
import wave
import io
import pyaudio
import simpleaudio as sa


class Audio:
    def __init__(self, audio_data):
        self.audio_data = audio_data

    def play(self):
        wave_obj = sa.WaveObject(self.audio_data, 1, 2, 24000)  # チャンネル数、サンプル幅、サンプルレート
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def speak(self):
        # メモリ上で展開
        audio = io.BytesIO(self.audio_data)

        with wave.open(audio, 'rb') as f:
            # 以下再生用処理
            p = pyaudio.PyAudio()

            def _callback(in_data, frame_count, time_info, status):
                data = f.readframes(frame_count)
                return data, pyaudio.paContinue

            stream = p.open(format=p.get_format_from_width(width=f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True,
                            stream_callback=_callback)

            # Voice再生
            stream.start_stream()
            while stream.is_active():
                time.sleep(0.1)

            stream.stop_stream()
            stream.close()
            p.terminate()
