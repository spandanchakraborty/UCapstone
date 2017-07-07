import pandas as pd


def init():
	global folderloc, g_file_names, g_file_details_dict, g_file_details_df,g_sr_global,g_mel_coeff_dict,g_mel_dict_pk
	#location of all labeled *.wav files
	folderloc='/Users/spandan.chakraborty/Documents/UML/Capstone/HS/Mycode/Mels/Input_labeled_audio/'
	# pickle file names
	g_mel_dict_pk='labeled_mel_dict.p'
	# All File Names List 
	g_file_names=[]
	# Audio details for all Files : Dict 
	g_file_details_dict={}
	# Audio details for all Files : DataFrame 
	g_file_details_df=pd.DataFrame
	# Librosa FrameRate
	g_sr_global=44100
	# Mel-Coeffs , keys would be the File name
	g_mel_coeff_dict={}
