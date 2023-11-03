# BatchP2FA-Python3

## About
The P2FA is a tool that automatically aligns audio recordings with their corresponding textual translations at the phoneme level. It works by using a Hidden Markov Model (HMM) to align each phoneme in the transcription with its corresponding segment in the audio waveform.

align.py is the Python script that is able to take in a singular input pair of an audio file and a transcription file of that audio and output a TextGrid file. TextGrid file is a format commonly used in the field of speech processing to represent and annotate the temporal alignment of segments within a textual translation. It is able to mark the boundaries of speech sounds, words, or other linguistic units. For the purpose of research conducted under the Language Acquisition and Processing Lab, we focus on _contrastive stress production_.

## Modifications
This is a modified version of P2FA for Python3 compatibility. This version of the P2FA was created by [jaekookang](https://github.com/jaekookang/p2fa_py3) on Github! In addition to the original functionality of producing a **singular** TextGrid file via terminal, this modified BatchP2FA includes the ability to simply **run** two additional scripts that automate the production of **batches** of data sets.

In essence, BatchP2FA is most useful for research purposes. I made these modifications as a Research Assistant under the Language Acquisition and Processing Lab run by Dr. Karin Stromswold and Sten Knutsen. I automated the P2FA by reducing the manual task of writing textual transcriptions and coding out the phonetic segments for each audio file.

**1) csv_transcriber.py:** File that that imports pandas to enable the production of transcription files (.txt) using .csv file. .csv file contains written transcriptions of all the audio files (.wav) labeled p14, which are the contrastive stress production cases collected by the Language Acquisition and Processing Lab. All transcription files (.txt) will be stored in P2FA's input_txt directory so that align.py can be run for this data.

_Most useful when transcriptions for audio is already available._

**2) text_grid_batch.py:** File that compiles the essential speech processing data in the input_txt and input_wav directories and automates P2FA's align.py to generate 500+ batches of data sets. We use **OpenAI's Whisper** model to transcribe an audio file and create its transcription file which is stored in P2FA's input_txt directory. We then use both the audio and transcription file as a singular input pair to generate its TextGrid file. Each input pair should have the same exact name, specifically participant#_p14_trial#.txt; Must be labeled p14 to signify cases detailing contrastive stress production collected by the Language Acquisition and Processing Lab.

_Most useful when transcriptions for audio is not available; It allows the user to simply run align.py using just the audio file._

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
