import pickle

import settings as st_conf
st_conf.init()  ### Initialize Config Files

import Extract_HS_Features as ehs
ehs.readfiles()

pickle.dump(st_conf.g_mel_coeff_dict, open(st_conf.g_mel_dict_pk, "wb"))
