# BatchP2FA-Python3
The P2FA is a tool that automatically aligns audio recordings with their corresponding transcriptions at the phoneme level. It works by using a Hidden Markov Model (HMM) to align each phoneme in the transcription with its corresponding segment in the audio waveform. align.py is the Python script that is able to take in a singular input pair of a sound file and a transcription file of that sound and output a TextGrid file. TextGrid file is a format used to store annotations of speech/audio recordings. It is the default P2FA output format.

This is a modified version of P2FA for Python3 compatibility. This version of the P2FA was created by [jaekookang](https://github.com/jaekookang/p2fa_py3) on Github! In addition to the original functionality of producing a singular TextGrid file via terminal, this modified BatchP2FA includes the ability to simply **run** two additional scripts and allows the user to process _batches_ of TextGrids, rather than one.

**1) text_file_batch.py:** File that allow users to open .csv file containing all transcriptions within a particular test case and generate .txt files for each transcript. This transcription should be saved in the p2fa_input directory for the next batch process. The p2fa_input directory should also contain the corresponding .wav files (sound files) of the transcriptions.

**2) text_grid_batch.py:** File that allows users to run align.py outside of the terminal and access all input files in the p2fa_input directory and produce batches of TextGrids for a particular test case.

BatchP2FA is most useful for research purposes and I made these modifications as a part of my Research Assistant position under the Language Acquisition and Processing Lab run by Dr. Karin Stromswold and Sten Knutsen.

## Install HTK
First, you need to download the HTK source code (http://htk.eng.cam.ac.uk/) which the P2FA. This HTK installation guide is retrieved from
[Link](https://github.com/prosodylab/Prosodylab-Aligner). The installation guidelines below is based on macOS Monterey.

Unzip HTK-3.4.1.tar.gz file.

```bash
$ tar -xvf HTK-3.4.1.tar.gz
```

After extracting the tar file, switch to htk directory.

```bash
$ cd htk
```

Compile HTK in the htk directory.

```bash
$ export CPPFLAGS=-UPHNALG
$ ./configure --disable-hlmtools --disable-hslab
$ make clean    # necessary if you're not starting from scratch
$ make -j4 all
$ sudo make -j4 install
```

**Note:** For macOS, you may need to follow these steps before compiling HTK:

```bash
# Add CPPFLAGS
$ export CPPFLAGS=-I/opt/X11/include

# If the above doesn't work, do 
$ ln -s /opt/X11/include/X11 /usr/local/include/X11

# Replace line 21 (#include <malloc.h>) of HTKLib/strarr.c as below
#   include <malloc/malloc.h> 

# Replace line 1650 (labid != splabid) of HTKLib/HRec.c as below
#   labpr != splabid
# This step will prevent "ERROR [+8522] LatFromPaths: Align have dur<=0"
# See: https://speechtechie.wordpress.com/2009/06/12/using-htk-3-4-1-on-mac-os-10-5/

# Compile with options if necessary
$ ./configure
$ make all
$ make install
```


## Install sox

```bash
$ sudo apt-get install sox

# or in Arch

$ sudo pacman -S sox

# or using brew

$ brew install sox
```

## Run

### Stand Alone

```bash
$ python align.py examples/ploppy.wav examples/ploppy.txt examples/ploppy.TextGrid
```

### Part of your code

You can invoke the aligner from your code:

```python
from p2fa import align

phoneme_alignments, word_alignments = align.align('WAV_FILE_PATH', 'TRANSCRIPTION_FILE_PATH')

# or 

phoneme_alignments, word_alignments, state_alignments = align.align('WAV_FILE_PATH', 'TRANSCRIPTION_FILE_PATH', state_align=True)
```
<p align="center">
<img width="500" height="300" src="https://github.com/jasmeanfernando/BatchP2FA/assets/98361155/a316d13b-2692-4391-85d4-3630c240c8bc" alt="HomePage" title="HomePage">
 <p>

## References
- http://www.ling.upenn.edu/phonetics/p2fa/
- https://github.com/jaekookang/p2fa_py3
