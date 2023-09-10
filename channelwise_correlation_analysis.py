#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:12:19 2023

@author: apple
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import torch
import numpy as np


mel_raw = open('mel_exp_ana_raw.txt')
lines_raw = mel_raw.read().splitlines()


#----------------------------correlation with bin1----------------------------
mel_b1= open('mel_exp_ana_b1.txt')
#mel_b1= open('mel_analysis_r2_b1.txt')
lines_b1= mel_b1.read().splitlines()

#discard the first
r_bin1_1 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    #第一个file本身的mel
    mel_bin1 = torch.load(lines_b1[i]).numpy()
    mel_bin1 = mel_bin1[: , 1:]
    #第一个file合成语音的mel的mel
    for channel_n in range(mel_bin1.shape[0]):
        r_bin1_1[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin1[channel_n, : ])[0,1]
                           
        
#discard the last
r_bin1_2 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin1 = torch.load(lines_b1[i]).numpy()
    mel_bin1 = mel_bin1[: , :-1]
    for channel_n in range(mel_bin1.shape[0]):
        r_bin1_2[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin1[channel_n, : ])[0,1]
       
# Calculate the mean and std
m1 = r_bin1_2.mean(axis=0)
sd1 = r_bin1_2.std(axis=0)

# Create a plot
plt.figure(figsize=(10, 6))
plt.errorbar(np.arange(1, 81), m1, yerr=sd1, fmt='o', color='blue', markersize=4, capsize=3, ecolor='blue', linestyle='dashed', elinewidth=1)
plt.xlabel('Channel', fontsize=12)
plt.ylabel('Mean Pearson Correlation', fontsize=12)
plt.title('Correlation with band1: Channel vs Mean Correlation', fontsize=14)
plt.grid(True)
plt.show()

#----------------------------correlation with bin2----------------------------
mel_b2= open('mel_exp_ana_b2.txt')
lines_b2= mel_b2.read().splitlines()

#discard the first
r_bin2_1 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin2 = torch.load(lines_b2[i]).numpy()
    mel_bin2 = mel_bin2[: , 1:]
    for channel_n in range(mel_bin2.shape[0]):
        r_bin2_1[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin2[channel_n, : ])[0,1]
                           
        
#discard the last
r_bin2_2 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin2 = torch.load(lines_b2[i]).numpy()
    mel_bin2 = mel_bin2[: , :-1]
    for channel_n in range(mel_bin2.shape[0]):
        r_bin2_2[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin2[channel_n, : ])[0,1]


# Calculate the mean and std
m2 = r_bin2_2.mean(axis=0)
sd2 = r_bin2_2.std(axis=0)


# Create a plot
plt.figure(figsize=(10, 6))
plt.errorbar(np.arange(1, 81), m2, yerr=sd2, fmt='o', color='blue', markersize=4, capsize=3, ecolor='blue', linestyle='dashed', elinewidth=1)
plt.xlabel('Channel', fontsize=12)
plt.ylabel('Mean Pearson Correlation', fontsize=12)
plt.title('Correlation with band2: Channel vs Mean Correlation', fontsize=14)
plt.grid(True)
plt.show()


#----------------------------correlation with bin3----------------------------
mel_b3= open('mel_exp_ana_b3.txt')
lines_b3= mel_b3.read().splitlines()

#discard the first
r_bin3_1 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin3 = torch.load(lines_b3[i]).numpy()
    mel_bin3 = mel_bin3[: , 1:]
    for channel_n in range(mel_bin3.shape[0]):
        r_bin3_1[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin3[channel_n, : ])[0,1]
                           
        
#discard the last
r_bin3_2 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin3 = torch.load(lines_b3[i]).numpy()
    mel_bin3 = mel_bin3[: , :-1]
    for channel_n in range(mel_bin3.shape[0]):
        r_bin3_2[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin3[channel_n, : ])[0,1]
        
        
# Calculate the mean and std
m3 = r_bin3_2.mean(axis=0)
sd3 = r_bin3_2.std(axis=0)


# Create a plot
plt.figure(figsize=(10, 6))
plt.errorbar(np.arange(1, 81), m3, yerr=sd3, fmt='o', color='blue', markersize=4, capsize=3, ecolor='blue', linestyle='dashed', elinewidth=1)
plt.xlabel('Channel', fontsize=12)
plt.ylabel('Mean Pearson Correlation', fontsize=12)
plt.title('Correlation with band3: Channel vs Mean Correlation', fontsize=14)
plt.xlim([1, 80])  # setting x-axis limits
plt.ylim([0, 1])   # setting y-axis limits
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)
plt.show()


#----------------------------correlation with bin4----------------------------
mel_b4= open('mel_exp_ana_b4.txt')
lines_b4= mel_b4.read().splitlines()

#discard the first
r_bin4_1 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin4 = torch.load(lines_b4[i]).numpy()
    mel_bin4 = mel_bin4[: , 1:]
    for channel_n in range(mel_bin4.shape[0]):
        r_bin4_1[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin4[channel_n, : ])[0,1]
                           
        
#discard the last
r_bin4_2 = np.empty((251,80))
for i in range(len(lines_raw)):
    mel_raw = torch.load(lines_raw[i]).numpy()
    mel_bin4 = torch.load(lines_b4[i]).numpy()
    mel_bin4 = mel_bin4[: , :-1]
    for channel_n in range(mel_bin4.shape[0]):
        r_bin4_2[i, channel_n] = np.corrcoef(mel_raw[channel_n,:], mel_bin4[channel_n, : ])[0,1]

# Calculate the mean and std
m4 = r_bin4_2.mean(axis=0)
sd4 = r_bin4_2.std(axis=0)


# Create a plot
plt.figure(figsize=(10, 6))
plt.errorbar(np.arange(1, 81), m4, yerr=sd4, fmt='o', color='blue', markersize=4, capsize=3, ecolor='blue', linestyle='dashed', elinewidth=1)
plt.xlabel('Channel', fontsize=12)
plt.ylabel('Mean Pearson Correlation', fontsize=12)
plt.title('Correlation with Bin 4: Channel vs Mean Correlation', fontsize=14)
plt.xlim([1, 80])  # setting x-axis limits
plt.ylim([0, 1])   # setting y-axis limits
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)
plt.show()

# ---------------4 plot in one----------------------

fig, axs = plt.subplots(2, 2, figsize=(16, 9), sharex=True, sharey=True)
#fig.suptitle('Mean Correlation with Different Bins', fontsize=16)

errorbar_kwargs = dict(fmt='o', markersize=4, capsize=3, elinewidth=1, ecolor='lightsteelblue')

axs[0, 0].errorbar(np.arange(1, 81), m1, yerr=sd1, **errorbar_kwargs, color="#00BFC4")
#axs[0, 0].grid(True)

axs[0, 1].errorbar(np.arange(1, 81), m2, yerr=sd2, **errorbar_kwargs, color="#00BFC4")
#axs[0, 1].grid(True)

axs[1, 0].errorbar(np.arange(1, 81), m3, yerr=sd3, **errorbar_kwargs, color="#00BFC4")
#axs[1, 0].grid(True)

axs[1, 1].errorbar(np.arange(1, 81), m4, yerr=sd4, **errorbar_kwargs, color="#00BFC4")


for ax in axs.flat:
    ax.label_outer()
    # Add vertical dashed lines at each 20 channels
    for x in np.arange(20, 81, 20):
        ax.axvline(x, color='grey', linestyle='dashed')

fig.text(0.5, 0.08, 'Mel Channel', ha='center', va='center', fontsize=16)
fig.text(0.09, 0.5, 'Mean Pearson correlation', ha='center', va='center', rotation='vertical', fontsize=16)

plt.xticks(np.arange(0, 81, 10), fontsize=12)
plt.yticks(np.arange(0, 1.1, 0.1), fontsize=14)
plt.ylim([0.31, 1.05])  # change these values as needed
plt.xlim([0.8, 82])

# Adjust subplot parameters to give specified padding
plt.subplots_adjust(wspace=0, hspace=0)

plt.show()

y
