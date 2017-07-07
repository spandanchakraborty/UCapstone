## Get File Duration/Frame Rates details 
# Global Varaibales file
import settings as st
# Library to process files
import os
# Import context manager to support "with" statements
import contextlib
# To read wav files
import wave
# import pandas
import pandas as pd
import numpy as np
import librosa


def get_File_Details(file_path):  ## file_paths
    file_path=st.folderloc+file_path
    #print file_path
    with contextlib.closing(wave.open(file_path,'r')) as filesx:
        frames = filesx.getnframes()
        rate = filesx.getframerate()
        duration = frames / float(rate)
        st.g_file_details_dict[os.path.splitext(file_path)[0][len(st.folderloc):]]={'Framerate':rate, 'duration in s':duration, 'Frames':frames}


def load_Mel_coeffs(file_path):
    file_path=st.folderloc+file_path
    X,sr = librosa.load(file_path,sr=st.g_sr_global) # 22050, 44100 # , offset=0.05, ,duration=2
    print('sample rate:' ,sr)
    S = librosa.feature.melspectrogram(y=X, sr=sr, n_mels=128, fmax=2000)
    st.g_mel_coeff_dict[os.path.splitext(file_path)[0][len(st.folderloc):]]=S


def readfiles():
	# Store the filenames in a Global DataFrame with details of Duration/FrameRate etc
	for fptemp in os.listdir(st.folderloc):
	    #g_file_names.append(os.path.splitext(fptemp)[0])
	    #print fptemp
	    if fptemp.endswith('.wav'):
	    	### Get File Duration/Frames/FrameRate Details
	        get_File_Details(fptemp)
	        load_Mel_coeffs(fptemp)
	print(st.g_mel_coeff_dict)
