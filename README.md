# UCapstone
Capstone Project To Identify S1 and S2 Heart Sounds from Kaggle Heart_Beat_Sound Project

Kaggle link:
	https://www.kaggle.com/kinguistics/heartbeat-sounds

The proposal is to build a model to locate precise heart sounds (HS) in a audio file (.wav) recorded via
Smart Phone app or Digiscope. 

My capstone only focuses on the 1st part of the challenge: Locating S1 and S2 heart sound in an audio file recorded from a phone app/Digital stethoscope, for normal heart sound.

Software and Libraries used in this Project:

	Python 2.7 (Anaconda Package):
		- 	Pandas, numpy, sklearn
	With default conda Python package I have additionally set up (pip install)

		-	Librosa:
				Version: 0.5.0
				Summary: Python module for audio and music processing
				Home-page: http://github.com/librosa/librosa

				Package to read audio files and extract Mel-frequency cepstral coefficients (MFCCs) from the audio files.
				used MFCC as features for training a Convnet model.
				For more info on Mels Ceptrum Co -eff : https://en.wikipedia.org/wiki/Mel-frequency_cepstrum

		-	tqdm : 
				Version : 4.14.0
				Summary: Fast, Extensible Progress Meter
			 	to see the progress of a loop: Since my training took almost an hour for 3000 epochs

	Tensorflow: Version 1.1.0

	Audacity: An open source audio file processing software to visualize the loaction of Heart Sounds in an audio file

The audio features are extracted using MFCC/ Librosa package

Input Files:	
	For this Set_A folder labeled Heart sound data is been used. In this Set_A flder there are 21 audio files, that starts with normal_ (denoting normal heart sound) which has HS1 and HS2 locations. 
	The labels can be found in set_a_timing.csv file

	Ignoring murmurs and extrahls files from Set_A 
	 and 
	Ignoring Set_B completely

	For normal_ labeled audio files In total there are 645 Heart Sound location labels.

	I have used 85% data for training and 15% for testing.

Flow of the program:
	Steps
	 1: Download all the normal_ labeled files from Set_A folders in a folder
	 	File count : There are in total 30 files
	 2: As per set_a_timing.csv file, only 21 normal_ files have labeles (meaning the location of HS1 and HS2 are marked)

	 3: So keep only those 21 labeled files for further processing

	 4: In Settings.py  enter the folder location where the audio (normal_ *.wav) files are downloaded
	 	the file initializes all other global variables used for audio feature extraction
	 5: Extract_HS_Features.py file uses python  Librosa library to extract MFCC audio features
	 6: Main.py reads settings and invoke Extract_HS_Features and dumps all the MFCC features in a pickle file for further 		processing
	 7: In Classify_Heart_Sound.pynb Jupyter notebook 
	 	a. Load the pickle file with Audio MFCC features
	 	b. map the MFCC that related to Heart Sound locations as per set_a_timing.csv
	 	c. there are some technical audio signal processing nuances for using Librosa
	 		- we are considering 128 mfcc features of sound recorded 
	 		- in the recording there are 44100 audio samples in 1 second of recording (it is a single channel recording)
	 		- Librosa uses default hop_legnth (window) of 512 frames 
	 		- So as an out of MFCC feature extraction, we are getting 128 MFCC coefficients for each segment which corresponds to roughly  (512/44100)=0.011 secs of audio recording
	 		- typical Heart sound lasts between 0.11-0.14 seconds. 
	 		- So we took 12 segments of audio recording around the labeled Heart sound location as our feature space.
	 			which means we have 128*12 matrix for each heart sound

	 8: Now an audio like Heart sound has a pattern in spacial arrangement like a similar images has same patterns. Since Conv. Nueral nets are very successful in image classification, I have followed the MNIST classification steps applied to audio claissification. Following the footsteps of Tensorflow example:
	 https://www.tensorflow.org/get_started/mnist/pros



With some playing around with simple Nueral net Vs Convnet of different Epochs.. got roughly 77% accuracy.
