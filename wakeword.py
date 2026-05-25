import pvporcupine
import pyaudio
import struct


def detect_wake_word():

    porcupine = pvporcupine.create(
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Waiting for wake word...")

    try:
        while True:

            pcm = audio_stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )

            pcm = struct.unpack_from(
                "h" * porcupine.frame_length,
                pcm
            )

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Wake word detected!")
                return True

    finally:
        audio_stream.close()
        pa.terminate()
        porcupine.delete()