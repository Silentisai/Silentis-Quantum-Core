# Silentis AI - Silentis Quantum Core

**Developed by: Silentis Team | Version 1.0**

A simple, powerful command-line tool for quantizing GGUF model files, built on the robust foundation of `llama.cpp`.

**Official Links:**
[Documentation](https://silentis.ai) | [Website](https://silentis.ai) | [Github](https://github.com/Silentisai) | [X (Twitter)](https://x.com/silentisproject) | [Telegram](https://t.me/SilentisAi)

**Support our Mission:**
[PancakeSwap](https://springboard.pancakeswap.finance/bsc/token/0x8a87562947422db0eb3070a5a1ac773c7a8d64e7)

---

## ► About The Project

Silentis Quantum Core is a streamlined Python wrapper designed to simplify the model quantization process. It provides an intuitive interface for leveraging the `quantize` executable from the `llama.cpp` project, allowing users to easily reduce the size of their GGUF models while maintaining performance.

This tool is perfect for developers and researchers who need to optimize large language models for deployment on resource-constrained devices without delving into the complexities of the underlying C++ code.

## ► Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

The core functionality of this tool depends on the `quantize` executable from `llama.cpp`. You must have this executable compiled and ready.

1.  **Clone and build `llama.cpp`:**
    If you haven't already, clone the official `llama.cpp` repository and compile it.
    ```sh
    git clone
    cd llama.cpp
    make
    ```
    This will generate the `quantize` executable in the main directory.

### Setup

1.  **Download Silentis Quantum Core:**
    Download the `SilentisQuantum.py` script
    
3.  **Create the Folder Structure:**
    Place the `silentis_quantum_core` executable or script in a directory. Inside that same directory, create a folder named `llama.cpp`.

4.  **Place the Executable:**
    Copy the `quantize` executable (e.g., `quantize.exe` on Windows or `quantize` on Linux/macOS) and any associated DLLs from your `llama.cpp` build into the `llama.cpp` folder you just created.

Your final directory structure should look like this:

```
/your-working-directory/
├── SilentisQuantum_core.py  
└── llama.cpp/
    └── quantize              (or quantize.exe)
    └── ... (any other required DLLs)
```

## ► Usage

The tool is operated via the command line, requiring three arguments: the input file path, the output file path, and the desired quantization type.

### Command Syntax

```sh
python SilentisQuantum.py <input_file> <output_file> <quant_type>
```
Or, if using the compiled executable:
```sh
./silentis_quantum_core.exe <input_file> <output_file> <quant_type>
```

### Arguments

* `input_file`: The full path to the source GGUF model you want to quantize.
* `output_file`: The full path where the new, quantized GGUF model will be saved.
* `quant_type`: The specific quantization method to apply. See the list of supported types below.

### Example

Here is an example of how to quantize a model named `L3-8B-v1.5.gguf` to the `Q4_K_M` format:

```sh
python SilentisQuantum.py "C:\Models\L3-8B-v1.5.gguf" "C:\Models\L3-8B-v1.5-Q4_K_M.gguf" "Q4_K_M"
```

The script will call the `quantize` executable with the provided parameters and stream the output directly to your console.

## ► Supported Quantization Types

You can choose from any of the following quantization types supported by `llama.cpp`:

| Type      | Description (General)                               |
| :-------- | :-------------------------------------------------- |
| `Q2_K`    | 2-bit quantization with K-Means.                    |
| `Q3_K_S`  | 3-bit K-quants (Small).                             |
| `Q3_K_M`  | 3-bit K-quants (Medium).                            |
| `Q3_K_L`  | 3-bit K-quants (Large).                             |
| `Q4_0`    | 4-bit, original quantization.                       |
| `Q4_1`    | 4-bit, improved quantization.                       |
| `Q4_K_S`  | 4-bit K-quants (Small). Recommended for most uses.  |
| `Q4_K_M`  | 4-bit K-quants (Medium). Recommended for most uses. |


MIT License
Copyright (c) 2025 - Silentis AI

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWA
