# Helper functions will go here
from pydub import AudioSegment
import os

# Converter function
def convert_ogg_to_wav(input_path, output_path=None):
    """
    Convert an OGG or WEBM audio file to WAV format.
    
    Args:
        input_path (str): Path to input .ogg or .webm file record from whatsapp
        output_path (str, optional): Desired output path for the .wav file
    
    Returns:
        str: Path to the converted WAV file
    """
    # Automatically name output if not provided
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.wav"
    
    # Load and export
    audio = AudioSegment.from_file(input_path, format="ogg")
    audio.export(output_path, format="wav")
    
    print(f"Converted: {input_path} → {output_path}")
    return output_path

