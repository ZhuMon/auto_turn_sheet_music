#! /usr/bin/env python3

import sys
import math
import numpy as np
from aubio import tempo, source


def detect_tempo(file_name):
    win_s = 512         # fft size
    hop_s = win_s // 2    # hop size

    samplerate = 0 

    s = source(file_name, samplerate, hop_s)
    samplerate = s.samplerate

    o = tempo("default", buf_size = win_s, hop_size = hop_s, samplerate = samplerate)

    # tempo detection delay, in samples
    # default to 4 blocks delay to catch up with
    delay = 4. * hop_s

    # list of beats, in samples
    beats = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = int(total_frames - delay + is_beat[0] * hop_s)
            # print("%f" % (this_beat / float(samplerate)))
            beats.append(this_beat)
        total_frames += read
        if read < hop_s: break

    bpms = []
    for i in range(len(beats)-1):
        bpms.append(60 / ((beats[i+1] - beats[i]) / float(samplerate)))

    # bpm = np.mean(bpms)
    bpm = math.floor(np.median(bpms))
    print(bpm)
    return bpm

def gpx2wav(file_name):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename>")

    detect_tempo(sys.argv[1])
