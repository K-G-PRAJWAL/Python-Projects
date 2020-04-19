# Wave module provides a convenient interface to the WAV sound format.
import sys
import wave, os
import threading
import numpy as np
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))

# np.set_printoptions(threshold=sys.maxsize)

class Audio_in_audio_lsb:
    
    def __init__(self, carrier, data):
        self.carrier = carrier
        self.data = data

    def encode(self):
        # We will use wave package available in native Python installation to read and write .wav audio file
        # read wave audio file

        # Enter the filename and open it in read-binary mode
        song = wave.open(self.carrier, mode='rb')
        
        # Get number of frames
        # Read the frames from the input file
        # Convert into a list
        # Convert list into bytearray
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))

        # Get the secret message
        in_fname = self.data

        in_bytes = np.fromfile(in_fname, dtype = "uint8")
        in_bits = np.unpackbits(in_bytes)
        bits = list(in_bits)
        #print(in_bytes, "\n", in_bits)
        
        # Replace LSB of each byte of the audio data by one1 bit from the text bit array
        for i, bit in enumerate(bits):
            try:
                frame_bytes[i] = (frame_bytes[i] & 254) | bit
            except IndexError:
                pass
        
        # Get the modified bytes
        frame_modified = bytes(frame_bytes)

        # Write bytes to a new wave audio file
        with wave.open('song_embedded.wav', 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        song.close()

    def decode(self, path):
        # Use wave package (native to Python) for reading the received audio file
        # song = wave.open(filedialog.askopenfilename(initialdir = dir_path,title = "Open carrier file",filetypes = (("WAV files","*.wav"),("all files","*.*"))), mode='rb')
        song = wave.open(path, mode='rb')
        # Convert audio to byte array
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))

        # Extract the LSB of each byte
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

        out_bits = np.array(extracted)
        out_bytes = np.packbits(out_bits)
        out_name = filedialog.asksaveasfilename(initialdir = "/",title = "Save file as",filetypes = (("WAV files","*.wav"),("all files","*.*")))+'.wav'
        out_bytes.tofile(out_name)
        os.startfile(out_name)

        print("Sucessfully decoded")
        song.close()
