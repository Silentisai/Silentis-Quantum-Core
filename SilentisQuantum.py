# Silentis AI - Silentis Quantum Core
# Developed by: Silentis Team
# MIT License | Version 1.0

# Documentation: https://silentis.ai
# Website: https://silentis.ai
# Github: https://github.com/Silentisai

# X: https://x.com/silentisproject
# Telegram: https://t.me/SilentisAi

# Support our mission: https://springboard.pancakeswap.finance/bsc/token/0x8a87562947422db0eb3070a5a1ac773c7a8d64e7
import sys
import os
import subprocess
import argparse
import traceback

def get_quant_types():
    """Returns a list of supported quantization types."""
    return [
        "Q2_K", "Q3_K_S", "Q3_K_M", "Q3_K_L", "Q4_0", "Q4_1", "Q4_K_S", "Q4_K_M"
    ]

def main():
    """
    Main function to parse arguments and run the quantization process.
    """
    # --- Argument Parser Setup ---
    quant_types = get_quant_types()
    parser = argparse.ArgumentParser(
        description="Silentis Quantum: A command-line tool for model quantization.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_file", help="Path to the input GGUF model file.")
    parser.add_argument("output_file", help="Path for the quantized output GGUF model file.")
    parser.add_argument("quant_type", choices=quant_types, help="The quantization type to apply.")

    args = parser.parse_args()

    # --- Pathing Logic ---
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    LLAMA_CPP_PATH = os.path.join(application_path, 'llama.cpp')

    # --- Executable Check ---
    executable_name = 'quantize'
    if sys.platform == "win32":
        executable_name += ".exe"
    executable_path = os.path.join(LLAMA_CPP_PATH, executable_name)

    if not os.path.exists(executable_path):
        print(f"ERROR: Main executable not found at '{executable_path}'", file=sys.stderr)
        print(f"Please place '{executable_name}' and its DLLs in the '{LLAMA_CPP_PATH}' folder.", file=sys.stderr)
        sys.exit(1)

    # --- Command Execution ---
    command = [executable_path, args.input_file, args.output_file, args.quant_type]
    print("--- Starting Quantization ---")
    print(f"Command: {' '.join(command)}")
    print("-" * 30)

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace',
            bufsize=1
        )

        for line in iter(process.stdout.readline, ''):
            print(line, end='')

        process.stdout.close()
        return_code = process.wait()

        print("-" * 30)
        if return_code:
            print(f"--- Quantization failed with exit code {return_code} ---", file=sys.stderr)
        else:
            print(f"--- Quantization successful! Output at: {args.output_file} ---")

    except Exception as e:
        print(f"\nCRITICAL: An exception occurred during quantization: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
