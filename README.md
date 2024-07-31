# OE-VI2


OE-VI2 is an occlusion effect-based in-ear voice input interface for earphones that leverages inner microphones on the earphone to capture sound vibrations propagating along in-ear channels. The key idea of EarSpeech is that in-ear speech is less sensitive to ambient noise and exhibits a correlation with airborne speech which is sensitive to ambient noise. The goal of OE-VI2 is reconstructing the in-ear speech to improve the quality and intelligibility. Here, we release some audio demo samples to demonstrate the performance of OE-VI2. 



# 1. Description

Here we release four groups of examples, and each one includes 6 utterances:

***(1) ground truth airborne speech***

***(2) original in-ear speech***

***(3) reconstructed speech by our system: OE-VI2***

***(4) reconstructed speech by baseline1: GMM***

***(5) reconstructed speech by baseline2: CycelGAN-VC2***

***(6) reconstructed speech by baseline3: AutoVC***

[The model OE-VC is also available in [Model_OE-VC.py](./model_OE-VC.py) ]

# 2. Demo

The comparison of Mel spectrogram are displayed below.

|Method|Example1|Example2|Example3|Example4|
|------|--------|--------|--------|--------|
| In-ear | ![alt text](./Example1/Original_In_Ear_Mel_Spectrogram.png) | ![alt text](./Example2/Original_In_Ear_Mel_Spectrogram.png) | ![alt text](./Example3/Original_In_Ear_Mel_Spectrogram.png) | ![alt text](./Example4/Original_In_Ear_Mel_Spectrogram.png) |
| Airborne (Ground Truth) | ![alt text](./Example1/Ground_Truth_Airborne_Spectrogram.png) | ![alt text](./Example2/Ground_Truth_Airborne_Spectrogram.png) | ![alt text](./Example3/Ground_Truth_Airborne_Spectrogram.png) | ![alt text](./Example4/Ground_Truth_Airborne_Spectrogram.png) |
| OE-VI2 (Ours) | ![alt text](./Example1/Reconstructed_Spectrogram_OE-VI2.png) | ![alt text](./Example2/Reconstructed_Spectrogram_OE-VI2.png) | ![alt text](./Example3/Reconstructed_Spectrogram_OE-VI2.png) | ![alt text](./Example4/Reconstructed_Spectrogram_OE-VI2.png) |
| GMM | ![alt text](./Example1/Reconstructed_Spectrogram_GMM.png) | ![alt text](./Example2/Reconstructed_Spectrogram_GMM.png) | ![alt text](./Example3/Reconstructed_Spectrogram_GMM.png) | ![alt text](./Example4/Reconstructed_Spectrogram_GMM.png) |
| CycleGAN-VC2 | ![alt text](./Example1/Reconstructed_Spectrogram_CycleGAN-VC2.png) | ![alt text](./Example2/Reconstructed_Spectrogram_CycleGAN-VC2.png) | ![alt text](./Example3/Reconstructed_Spectrogram_CycleGAN-VC2.png) | ![alt text](./Example4/Reconstructed_Spectrogram_CycleGAN-VC2.png) |
| AutoVC | ![alt text](./Example1/Reconstructed_Spectrogram_AutoVC.png) | ![alt text](./Example2/Reconstructed_Spectrogram_AutoVC.png) | ![alt text](./Example3/Reconstructed_Spectrogram_AutoVC.png) | ![alt text](./Example4/Reconstructed_Spectrogram_AutoVC.png) |
