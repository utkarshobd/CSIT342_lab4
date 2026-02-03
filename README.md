# 2D DFT Implementation Lab

## Overview
Complete implementation of 2D Discrete Fourier Transform without using ready-made DFT/FFT functions.

## Features
1. **2D DFT Basis Generation**: Creates and displays 8×8 2D DFT basis functions as 64×64 image
2. **Binary Rectangle Creation**: Interactive input for rectangle position and dimensions
3. **Custom 2D DFT Computation**: Manual implementation using nested loops
4. **Centered Image Processing**: Applies (-1)^(x+y) multiplication and computes DFT

## Requirements
- Python 3.6+
- numpy
- matplotlib

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python dft_2d_implementation.py
```

## Interactive Inputs
When prompted, enter:
- Top-left corner X position (0-63)
- Top-left corner Y position (0-63)  
- Rectangle width in pixels
- Rectangle height in pixels

## Output
- 8×8 DFT basis functions visualization
- Binary rectangle image
- DFT magnitude and phase plots for original image
- Centered image visualization
- DFT magnitude and phase plots for centered image

## Implementation Details
- No use of numpy.fft or scipy.fft functions
- Pure mathematical implementation using complex exponentials
- Progress tracking for DFT computation
- Log-scale visualization for better magnitude display