# Wave module provides a convenient interface to the WAV sound format.
import wave, os
import threading
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))

class Text_in_audio_lsb:

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
        string = self.data
        
        # Append dummy data to fill out rest of the bytes. 
        # Receiver shall detect and remove these characters.
        string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
        
        # Convert text to bit array
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

        # Replace LSB of each byte of the audio data by one bit from the text bit array
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
                    
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

        # Convert byte array back to string
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

        # Cut off the filler characters
        decoded = string.split("###")[0]

        # Print the extracted text
        print("Sucessfully decoded: "+decoded)
        song.close()
        return decoded