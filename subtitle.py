#!/usr/bin/env python3

import os
from pathlib import Path
import requests
import time

import click
import colorama
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

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


if __name__ == "__main__":
    cli()
