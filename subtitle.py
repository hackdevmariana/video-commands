#!/usr/bin/env python3

import os
from pathlib import Path
import re
import requests
import time

import click
import colorama
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip
import nltk

load_dotenv()
nltk.download('punkt')

ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')

@click.group()
def cli():
    pass

def print_success(output):
    click.echo(f"The file has been created {colorama.Fore.GREEN} successfully {colorama.Style.RESET_ALL}: {output}")

def print_error(output):
    click.echo(f"An {colorama.Fore.RED} error {colorama.Style.RESET_ALL} occurred creating the file {output}.")

def handle_output(output, output_path):
    if output_path.is_file():
        print_success(output)
    else:
        print_error(output)

def split_line(line):
    pattern = r'(\.\.\.|[.,;])'
    parts = re.split(pattern, line)
    result = []
    temp = ""

    for part in parts:
        if part in [',', ';']:
            temp += part
            result.append(temp.strip())
            temp = ""
        elif part == '...':
            temp += part
            result.append(temp.strip())
            temp = ""
        elif part == '.':
            temp += part
            result.append(temp.strip())
            result.append("")  # Add blank line after a period.
            temp = ""
        elif part.strip():
            if temp:
                result.append(temp.strip())
            temp = part.strip()
    if temp:
        result.append(temp.strip())
    return result

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def toaudio(input, output):
    """Extract audio from a video."""

    if not output:
        output = f"{Path(input).stem}.mp3"

    try:
        video = VideoFileClip(input)
        video.audio.write_audiofile(output)
    except Exception as e:
        print(f"Error extracting audio: {e}")
        print_error(output)
        return

    output_path = Path(output)
    handle_output(output, output_path)

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def totext(input, output):
    """Extract text from an audio."""

    if not output:
        output = f"{Path(input).stem}.txt"

    headers = {
        "authorization": ASSEMBLYAI_API_KEY,
        "content-type": "application/json"
    }

    def upload_file(file_path):
        upload_url = "https://api.assemblyai.com/v2/upload"
        with open(file_path, "rb") as f:
            response = requests.post(upload_url, headers=headers, files={"file": f})
        response.raise_for_status()
        return response.json()["upload_url"]

    def get_transcription(audio_url):
        transcript_url = "https://api.assemblyai.com/v2/transcript"
        response = requests.post(transcript_url, json={"audio_url": audio_url, "language_code": "es"}, headers=headers)
        response.raise_for_status()
        return response.json()["id"]

    def get_transcript_result(transcript_id):
        transcript_url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
        while True:
            response = requests.get(transcript_url, headers=headers)
            response.raise_for_status()
            result = response.json()
            if result["status"] == "completed":
                return result["text"]
            elif result["status"] == "failed":
                raise Exception("Transcription failed")
            time.sleep(5)

    try:
        audio_url = upload_file(input)
        transcript_id = get_transcription(audio_url)
        text = get_transcript_result(transcript_id)
        click.echo(text)
        with open(output, 'w') as f:
            f.write(text)
    except Exception as e:
        print(f"Error processing audio: {e}")
        print_error(output)
        return

    output_path = Path(output)
    handle_output(output, output_path)

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def uppercase(input, output):
    """Convert text to uppercase."""

    if not output:
        output = f"{Path(input).stem}_uppercase.txt"

    try:
        with open(input, 'r') as f:
            text = f.read()
        text_upper = text.upper()
        with open(output, 'w') as f:
            f.write(text_upper)
        click.echo(text_upper)
    except Exception as e:
        print(f"Error processing text: {e}")
        print_error(output)
        return

    output_path = Path(output)
    handle_output(output, output_path)

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sentences(input, output):
    """Split text into sentences."""

    if not output:
        output = f"{Path(input).stem}_sentences.txt"

    try:
        with open(input, 'r') as f:
            text = f.read()
        sentences = nltk.sent_tokenize(text)
        with open(output, 'w') as f:
            for sentence in sentences:
                f.write(sentence + '\n')
        click.echo('\n'.join(sentences))
    except Exception as e:
        print(f"Error processing text: {e}")
        print_error(output)
        return

    output_path = Path(output)
    handle_output(output, output_path)

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--max-length', '-m', default=40, help='Maximum line length')
@click.option('--output', '-o', default='', help='Output file path')
def lines(input, max_length, output):
    """Split text into lines with a maximum length."""

    if not output:
        output = f"{Path(input).stem}_lines.txt"

    try:
        with open(input, 'r') as f:
            text = f.read()
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 <= max_length:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        if current_line:
            lines.append(' '.join(current_line))

        with open(output, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        click.echo('\n'.join(lines))
    except Exception as e:
        print(f"Error processing text: {e}")
        print_error(output)
        return

    output_path = Path(output)
    handle_output(output, output_path)

@cli.command()
@click.argument('video', type=click.Path(exists=True))
@click.option('--max-length', '-m', default=40, help='Maximum line length')
@click.option('--output', '-o', default='', help='Output text file path')
def preparetext(video, max_length, output):
    """Prepare text from video: uppercase, split into sentences, and max line length."""
    if not output:
        output = f"{Path(video).stem}_prepared.txt"

    try:
        # Step 1: Extract audio from video
        audio_path = f"{Path(video).stem}.mp3"
        video_clip = VideoFileClip(video)
        video_clip.audio.write_audiofile(audio_path)

        # Step 2: Transcribe audio to text
        headers = {
            "authorization": ASSEMBLYAI_API_KEY,
            "content-type": "application/json"
        }

        def upload_file(file_path):
            upload_url = "https://api.assemblyai.com/v2/upload"
            with open(file_path, "rb") as f:
                response = requests.post(upload_url, headers=headers, files={"file": f})
            response.raise_for_status()
            return response.json()["upload_url"]

        def get_transcription(audio_url):
            transcript_url = "https://api.assemblyai.com/v2/transcript"
            response = requests.post(transcript_url, json={"audio_url": audio_url, "language_code": "es"}, headers=headers)
            response.raise_for_status()
            return response.json()["id"]

        def get_transcript_result(transcript_id):
            transcript_url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
            while True:
                response = requests.get(transcript_url, headers=headers)
                response.raise_for_status()
                result = response.json()
                if result["status"] == "completed":
                    return result["text"]
                elif result["status"] == "failed":
                    raise Exception("Transcription failed")
                time.sleep(5)

        audio_url = upload_file(audio_path)
        transcript_id = get_transcription(audio_url)
        text = get_transcript_result(transcript_id)

        # Step 3: Process text - Uppercase, split into sentences, and split into lines
        text_upper = text.upper()

        words = text_upper.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 <= max_length:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        if current_line:
            lines.append(' '.join(current_line))

        with open(output, 'w') as f:
            for line in lines:
                if all(char not in line for char in ['.', ',', ';']):
                    f.write(line + '\n')
                    click.echo(line)
                else:
                    parts = split_line(line)
                    for part in parts:
                        f.write(part + '\n')
                        click.echo(part)

    except Exception as e:
        click.echo(f"Error processing text: {e}")
        print_error(output)
        return

    output_path = Path(output)
    handle_output(output, output_path)
    os.remove(audio_path)

if __name__ == "__main__":
    cli()
