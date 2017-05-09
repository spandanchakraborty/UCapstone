
# coding: utf-8

# In[51]:

import wave
import contextlib
import glob
import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
#import tensorflow as tf
from matplotlib.pyplot import specgram
import IPython.display
from IPython.display import Image
#get_ipython().magic(u'matplotlib inline')


import wave
import contextlib


#from pydub import AudioSegment
#song = AudioSegment.from_wav("audio.wav")
#new = song.low_pass_filter(5000)



### Get File Duration/Frame Rates details 
def get_File_Details(file_paths):  ## file_paths
    
    for fname in file_paths:
        fname = folderloc+fname
        with contextlib.closing(wave.open(fname,'r')) as filesx:
            frames = filesx.getnframes()
            rate = filesx.getframerate()
            duration = frames / float(rate)
            print('duration',duration,'Rate',rate,'Frames',frames)


# In[52]:


def load_sound_files_for_each(file_path,fname):
    file_path=folderloc+file_path
    print(file_path)
    X,sr = librosa.load(file_path,sr=44100, offset=0.5,duration=4.0)
    ### printSpecShow(X, sr,file_path,fname)
    printMfcc(X, sr,file_path,fname)



def printSpecShow(X, sr,file_path,fname):
    D = librosa.logamplitude(np.abs(librosa.stft(X))**2, ref_power=np.max)
    fig = plt.figure(figsize=(20,15))# figsize=(300,60), dpi = 900
    librosa.display.specshow(D,x_axis='time' ,y_axis='log',sr=sr)
    plt.colorbar()
    plt.title(file_path.title())
    fpath='/Users/spandan.chakraborty/Documents/UML/Capstone/HS/Mycode/pngs/'+fname+'.png'
    plt.savefig(fpath)

def printMfcc(X, sr,file_path,fname):
    fig = plt.figure(figsize=(20,15))# figsize=(300,60), dpi = 900
    S = librosa.feature.melspectrogram(y=X, sr=sr, n_mels=256, fmax=3000)
    librosa.display.specshow(S,x_axis='time' ,y_axis='mel',sr=sr)
    plt.colorbar()
    plt.title(file_path.title())
    fpath='/Users/spandan.chakraborty/Documents/UML/Capstone/HS/Mycode/pngs_mfcc/'+fname+'.png'
    plt.savefig(fpath)


def load_sound_files_in_one(file_paths):
    raw_sounds = []
    #
    for fp in file_paths:
        X,sr = librosa.load(folderloc+fp,sr=44100, offset=0.5,duration=4.0)
        raw_sounds.append(X)
        file_names.append(fp)
    return raw_sounds

def plot_log_power_specgram_in_one(sound_names,raw_sounds):
    i = 1
    fig = plt.figure(figsize=(100,60))# figsize=(300,60), dpi = 900
    for n,f in zip(file_names,raw_sounds):
    #for f in raw_sounds:
        plt.subplot(50,1,i)
        plt.tight_layout()
        #plt.subplot(50,1,i)
        D = librosa.logamplitude(np.abs(librosa.stft(f))**2, ref_power=np.max)
        librosa.display.specshow(D,x_axis='time' ,y_axis='log',sr=44100)
        plt.title(n.title())
        #plt.autoscale_view(True,True,True)
        #subplt.autoscale_view(True,True,True)
        i += 1
    plt.title("Figure 3: Log power spectrogram",x=0.5, y=0.915,fontsize=18, loc='right')
    plt.savefig('/Users/spandan.chakraborty/Documents/UML/Capstone/HS/Mycode/LogSpecGram1.png')

def find_onset_in_one(raw_sounds,file_names):
    i = 1
    fig = plt.figure(figsize=(25,60))#, dpi = 900
    for n,f in zip(file_names,raw_sounds):
        plt.subplot(50,1,i)
        oenv = librosa.onset.onset_strength(y=f, sr=sr)
        # Detect events without backtracking
        onset_raw = librosa.onset.onset_detect(onset_envelope=oenv,backtrack=False)
        # Backtrack the events using the onset envelope
        onset_bt = librosa.onset.onset_backtrack(onset_raw, oenv)
        # Backtrack the events using the RMS energy
        #rmse = librosa.feature.rmse(S=np.abs(librosa.stft(y=y)))
        #onset_bt_rmse = librosa.onset.onset_backtrack(onset_raw, rmse[0])
        # Plot the results
        plt.plot(oenv, label='Onset strength')
        plt.vlines(onset_raw, 0, oenv.max(), label='Raw onsets')
        plt.vlines(onset_bt, 0, oenv.max(), label='Backtracked', color='r')
        plt.legend(frameon=True)#, framealpha=0.75
        plt.title(n.title())
        i += 1
    plt.title("OnSet Detection",x=0.5, y=0.915,fontsize=18, loc='right')
    plt.savefig('/Users/spandan.chakraborty/Documents/UML/Capstone/HS/Mycode/OnSetDetect1.png')




# In[ ]:
folderloc='/Users/spandan.chakraborty/Documents/UML/Capstone/HS/set_a/'

sr=44100
sound_file_paths=[]
file_names=[]
for fptemp in os.listdir(folderloc):
    if os.path.isfile(os.path.join(folderloc,fptemp)) and 'normal_' in fptemp:  ### Select WHat kind of File to read 
        file_names.append(os.path.splitext(fptemp)[0])
        sound_file_paths.append(fptemp)

### print(sound_file_paths)

### sound_file_paths = ["normal__201108011112.wav","normal__201108011114.wav","normal__201108011115.wav","normal__201108011118.wav"]

duration = []
cnt=0
for fp in sound_file_paths:
    load_sound_files_for_each(fp,file_names[cnt])
    cnt=cnt+1

### raw_sounds = load_sound_files(sound_file_paths)
### print('Start File loading...')
### plot_log_power_specgram(sound_names,raw_sounds)

#plot_waves(sound_names,raw_sounds)
#plot_specgram(sound_names,raw_sounds)
#plot_log_power_specgram(sound_names,raw_sounds)
### find_onset(raw_sounds,file_names)
### get_File_Details(sound_file_paths)
### print the Raw Sound Array
### np.savetxt('/Users/spandan.chakraborty/Documents/UML/Capstone/HS/Mycode/test.out',raw_sounds)
### print(raw_sounds)



# In[45]:

# y, sr = librosa.load('/Users/spandan.chakraborty/Documents/UML/Capstone/HS/set_a/normal__201108011112.wav')
# plt.figure(figsize=(20,16))
# plt.plot(y[22700:22800])
# plt.plot(y[67500:67600])
# plt.plot(y[112300:112400])
# plt.plot(y[157850:157950])
# plt.plot(y[202637:202737])
# plt.plot(y[247426:247526])
# plt.plot(y[292214:292314])
# plt.plot(y[23483:23583])
# print(y.shape)
# #IPython.display.Audio(data=y, rate=sr)


# In[44]:

# mfcc = librosa.feature.mfcc(y, sr)
# #librosa.display.specshow(mfcc)
# R = librosa.segment.recurrence_matrix(mfcc)
# librosa.display.specshow(R, x_axis='time', y_axis='time')


# In[42]:

# chroma=librosa.feature.chroma_stft(y=y, sr=sr)
# librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
# plt.colorbar()
# plt.title('Chromagram')
# plt.tight_layout()


# In[49]:

# y1, sr1 = librosa.load('/Users/spandan.chakraborty/Documents/UML/Capstone/HS/set_a/extrahls__201101091153.wav')
# plt.figure(figsize=(25,16))
# plt.plot(y1)

