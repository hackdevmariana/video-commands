#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
import gmic



def process_image(command_name, instruction):
    def decorator(func):
        @click.command(name=command_name)
        @click.argument('input', type=click.Path(exists=True))
        @click.option('--output', '-o', default='', help='Output file path')
        def wrapper(input, output):
            if not output:
                output = f"{Path(input).stem}_{command_name}.png"

            gmic.run(f'{input} mix_channels ({instruction}) output {output}')

            output_path = Path(output)
            if output_path.is_file():
                click.echo(f"The image has been created{colorama.Fore.GREEN} successfully{colorama.Style.RESET_ALL}: {output}")
            else:
                click.echo(f"An{colorama.Fore.RED} error{colorama.Style.RESET_ALL} occurred creating the file {output}.")

        return wrapper
    return decorator

@process_image('darkblue', "0,0,0;0,0,0;0,1,0")
def darkblue():
    """Mixes the channels giving a dark blue tone to the image."""

@process_image('green', "0,0,0;0,1,0;0,0,0")
def green():
    """Mixes the channels giving a green tone to the image."""

@process_image('turquoise', "0,0,0;0,0,1;0,0,1")
def turquoise():
    """Mixes the channels giving a turquoise tone to the image."""

@process_image('sea', "0,0,0;0,0,1;0,1,0")
def sea():
    """Mixes the channels giving a sea tone to the image."""

@process_image('greenishandblue', "0,0,0;0,0,1;1,0,0")
def greenishandblue():
    """Mixes the channels giving a greenish and blue tone to the image."""

@process_image('luminousgreen', "0,0,0;1,0,0;0,0,0")
def luminousgreen():
    """Mixes the channels giving a luminous green tone to the image."""

@process_image('greenteal', "0,0,0;1,0,0;0,0,1")
def greenteal():
    """Mixes the channels giving a green and teal tone to the image."""

@process_image('darkred', "0,0,1;0,0,0;0,0,0")
def darkred():
    """Mixes the channels giving a dark red tone to the image."""

@process_image('purple', "0,0,1;0,0,0;0,0,1")
def purple():
    """Mixes the channels giving a purple tone to the image."""

@process_image('lilacblue', "0,0,1;0,0,0;1,0,0")
def lilacblue():
    """Mixes the channels giving a lilac and blue tone to the image."""

@process_image('paleyellow', "0,0,1;0,0,1;0,0,0")
def paleyellow():
    """Mixes the channels giving a pale yellow tone to the image."""

@process_image('palepurplegrey', "0,0,1;0,0,1;0,1,0")
def palepurplegrey():
    """Mixes the channels giving a pale purple and grey tone to the image."""

@process_image('purplegrey', "0,0,1;0,0,1;1,0,0")
def purplegrey():
    """Mixes the channels giving a purple and grey tone to the image."""

@process_image('lemonlime', "0,0,1;0,1,0;0,0,0")
def lemonlime():
    """Mixes the channels giving a lemon-lime tone to the image."""

@process_image('yellowgreen', "0,0,1;1,0,0;0,0,0")
def yellowgreen():
    """Mixes the channels giving a yellow and green tone to the image."""

@process_image('purplegreen', "0,0,1;1,0,0;0,0,0")
def purplegreen():
    """Mixes the channels giving a purple and green tone to the image."""

@process_image('dullgarnetturquoise', "0,0,1;1,0,0;1,0,0")
def dullgarnetturquoise():
    """Mixes the channels giving a dull garnet and turquoise tone to the image."""

@process_image('blackred', "0,1,0;0,0,0;0,0,0")
def blackred():
    """Mixes the channels giving a black and red tone to the image."""

@process_image('blackpurple', "0,1,0;0,0,0;0,0,1")
def blackpurple():
    """Mixes the channels giving a black and purple tone to the image."""

@process_image('lilacpurple', "0,1,0;0,0,0;1,0,0")
def lilacpurple():
    """Mixes the channels giving a lilac and purple tone to the image."""

@process_image('tanning', "0,1,0;0,0,1;0,0,1")
def tanning ():
    """Mixes the channels giving a tanning tone to the image."""

@process_image('palepurplegreen', "0,1,0;0,0,1;0,1,0")
def palepurplegreen():
    """Mixes the channels giving a pale purple and green tone to the image."""

@process_image('paleolive', "0,1,0;0,1,0;0,0,1")
def paleolive():
    """Mixes the channels giving a pale olive tone to the image."""

@process_image('whiteyellow', "0,0,0;0,0,0;0,0,1 negate")
def whiteyellow():
    """Mixes the channels giving a white and yellow tone to the image."""

@process_image('whitepink', "0,0,0;0,0,1;0,0,0 negate")
def whitepink():
    """Mixes the channels giving a white and pink tone to the image."""

@process_image('whitered', "0,0,0;0,0,1;0,0,1 negate")
def whitered():
    """Mixes the channels giving a white and red tone to the image."""

@process_image('redamber', "0,0,0;0,0,1;1,0,0 negate")
def redamber():
    """Mixes the channels giving a amber and red tone to the image."""

@process_image('whitelilac', "0,0,0;0,1,0;0,0,0 negate")
def whitelilac():
    """Mixes the channels giving a white and lilac tone to the image."""

@process_image('whitecyan', "0,0,1;0,0,0;0,0,0 negate")
def whitecyan():
    """Mixes the channels giving a white and cyan tone to the image."""

@process_image('whitegreen', "0,0,1;0,0,0;0,0,1 negate")
def whitegreen():
    """Mixes the channels giving a white and green tone to the image."""

@process_image('whiteblue', "0,0,1;0,0,1;0,0,0 negate")
def whiteblue():
    """Mixes the channels giving a white and blue tone to the image."""

@process_image('whiteblacknegate', "0,0,1;0,0,1;0,0,1 negate")
def whiteblacknegate():
    """Mixes the channels giving a white and black negate tone to the image."""

@process_image('blackberrypistachio', "0,0,1;0,0,1;1,0,0 negate")
def blackberrypistachio():
    """Mixes the channels giving a blackberry and pistachio tone to the image."""


@click.group()
def cli():
    pass


cli.add_command(darkblue)
cli.add_command(green)
cli.add_command(turquoise)
cli.add_command(sea)
cli.add_command(greenishandblue)
cli.add_command(luminousgreen)
cli.add_command(greenteal)
cli.add_command(darkred)
cli.add_command(blackred)
cli.add_command(purple)
cli.add_command(lilacblue)
cli.add_command(paleyellow)
cli.add_command(palepurplegrey)
cli.add_command(purplegrey)
cli.add_command(lemonlime)
cli.add_command(yellowgreen)
cli.add_command(purplegreen)
cli.add_command(blackpurple)
cli.add_command(lilacpurple)
cli.add_command(dullgarnetturquoise)
cli.add_command(palepurplegreen)
cli.add_command(paleolive)
cli.add_command(whiteyellow)
cli.add_command(whitepink)
cli.add_command(whitered)
cli.add_command(redamber)
cli.add_command(whitelilac)
cli.add_command(whitecyan)
cli.add_command(whitegreen)
cli.add_command(whiteblue)
cli.add_command(whiteblacknegate)
cli.add_command(blackberrypistachio)



if __name__ == "__main__":
    cli()
