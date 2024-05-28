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

            gmic.run(f'{input} {instruction} output {output}')

            output_path = Path(output)
            if output_path.is_file():
                click.echo(f"The image has been created{colorama.Fore.GREEN} successfully{colorama.Style.RESET_ALL}: {output}")
            else:
                click.echo(f"An{colorama.Fore.RED} error{colorama.Style.RESET_ALL} occurred creating the file {output}.")

        return wrapper
    return decorator

@process_image('orange', "balance_gamma 241,147,-121")
def orange():
    """Changes the color of the received image to orange."""

@process_image('pastelorange', "balance_gamma 250,178,124")
def pastelorange():
    """Changes the color of the received image to pastel orange."""

@process_image('luminousgreen', "balance_gamma -12,96,-237")
def luminousgreen():
    """Changes the color of the received image to luminous green."""

@process_image('pastelturquoise', "balance_gamma -17,165,127")
def pastelturquoise():
    """Changes the color of the received image to pastel turquoise."""

@process_image('indigo', "balance_gamma -19,106,128")
def indigo():
    """Changes the color of the received image to indigo."""

@process_image('pastelblue', "balance_gamma -21,202,231")
def pastelblue():
    """Changes the color of the received image to pastel blue."""

@process_image('blue', "balance_gamma -23,69,215")
def blue():
    """Changes the color of the received image to blue."""

@process_image('nightblue', "balance_gamma -31,10,80")
def nightblue():
    """Changes the color of the received image to night blue."""

@process_image('palealien', "balance_gamma -46,40,8")
def palealien():
    """Changes the color of the received image to pale alien."""

@process_image('lime', "balance_gamma -60,205,-155")
def lime():
    """Changes the color of the received image to lime."""

@process_image('luminousblue', "balance_gamma -85,97,205")
def luminousblue():
    """Changes the color of the received image to luminous blue."""

@process_image('turquoise', "balance_gamma -93,124,94")
def turquoise():
    """Changes the color of the received image to turquoise."""

@process_image('pastelgreen', "balance_gamma -119,197,18")
def pastelgreen():
    """Changes the color of the received image to pastel green."""

@process_image('paleindigo', "balance_gamma -147,77,120")
def paleindigo():
    """Changes the color of the received image to pale indigo."""

@process_image('spectralpurple', "balance_gamma 5,-5,47")
def spectralpurple():
    """Changes the color of the received image to spectral purple."""

@process_image('luminousindigo', "balance_gamma 6,109,167")
def luminousindigo():
    """Changes the color of the received image to luminous indigo."""

@process_image('luminouslime', "balance_gamma 6,191,104")
def luminouslime():
    """Changes the color of the received image to luminous lime."""

@process_image('pinkblue', "balance_gamma 7,-54,199")
def pinkblue():
    """Changes the color of the received image to pink and blue."""

@process_image('blackred', "balance_gamma 7,-54,199")
def blackred():
    """Changes the color of the received image to black and red."""

@process_image('bluepurplesubtle', "balance_gamma 8,16,129")
def bluepurplesubtle():
    """Changes the color of the received image to blue and purple subtle."""

@process_image('shininggreen', "balance_gamma 8,254,159")
def shininggreen():
    """Changes the color of the received image to shining green."""


@click.group()
def cli():
    pass

cli.add_command(orange)
cli.add_command(pastelorange)
cli.add_command(pastelgreen)
cli.add_command(luminousgreen)
cli.add_command(luminouslime)
cli.add_command(pastelturquoise)
cli.add_command(turquoise)
cli.add_command(pastelblue)
cli.add_command(blue)
cli.add_command(nightblue)
cli.add_command(luminousblue)
cli.add_command(luminousindigo)
cli.add_command(indigo)
cli.add_command(paleindigo)
cli.add_command(palealien)
cli.add_command(lime)
cli.add_command(spectralpurple)
cli.add_command(pinkblue)
cli.add_command(blackred)
cli.add_command(bluepurplesubtle)
cli.add_command(shininggreen)


if __name__ == "__main__":
    cli()
