import os
import random
import numpy as np
import soundfile as sf


def read_audio_file(file_path):
    data, samplerate = sf.read(file_path)
    return data, samplerate

def downmix_to_mono(audio_data):
    if audio_data.ndim > 1:
        mono_data = np.mean(audio_data, axis=1)
    else:
        mono_data = audio_data
    return mono_data

def slice_audio(data, samplerate, slice_duration):
    samples_per_slice = samplerate * slice_duration
    num_slices = len(data) // samples_per_slice
    slices = np.array_split(data[:num_slices * samples_per_slice], num_slices)
    return slices

def save_audio_slices(slices, samplerate, output_dir, basename):
    os.makedirs(output_dir, exist_ok=True)
    for i, audio_slice in enumerate(slices):
        output_path = os.path.join(output_dir, f"{basename}_slice_{i}.wav")
        sf.write(output_path, audio_slice, samplerate)

def get_random_file_path(dir_path):
    files = os.listdir(dir_path)
    random_file = random.choice(files)
    file_path = os.path.join(dir_path, random_file)
    return file_path

def process_audio_files(input_dir, output_dir,slice_duration=10):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.wav', '.flac','.mp3','.ogg')):
            file_path = os.path.join(input_dir, filename)
            basename, _ = os.path.splitext(filename)
            data, samplerate = read_audio_file(file_path)
            mono_data = downmix_to_mono(data)
            slices = slice_audio(mono_data, samplerate, slice_duration)
            save_audio_slices(slices, samplerate, output_dir, basename)
    print("Number of slices = ", len([entry for entry in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, entry))]))