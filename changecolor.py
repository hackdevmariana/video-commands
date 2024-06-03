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

@process_image('bluepurple', "balance_gamma 9,-39,94")
def bluepurple():
    """Changes the color of the received image to blue and purple."""


@process_image('luminouslemonlime', "balance_gamma 9,224,-34")
def luminouslemonlime():
    """Changes the color of the received image to luminous lemon lime."""

@process_image('bluelime', "balance_gamma 18,174,52")
def bluelime():
    """Changes the color of the received image to blue lime."""

@process_image('darklemonlime', "balance_gamma 10,86,-246")
def darklemonlime():
    """Changes the color of the received image to dark lemon lime."""

@process_image('blacklemon', "balance_gamma 31,45,-177")
def blacklemon():
    """Changes the color of the received image to black and lemon."""

@process_image('blacklime', "balance_gamma 40,90,-204")
def blacklime():
    """Changes the color of the received image to black and lime."""

@process_image('luminousintenseblue', "balance_gamma 40,47,224")
def luminousintenseblue():
    """Changes the color of the received image to luminous intense blue."""

@process_image('greenishhue', "balance_gamma 46,102,79")
def greenishhue():
    """Changes the color of the received image to greenish hue."""

@process_image('palegreenhue', "balance_gamma 74,118,56")
def palegreenhue():
    """Changes the color of the received image to pale green hue."""

@process_image('palebluehue', "balance_gamma 72,67,155")
def palebluehue():
    """Changes the color of the received image to pale blue hue."""

@process_image('purplehue', "balance_gamma 64,36,91")
def purplehue():
    """Changes the color of the received image to purple hue."""

@process_image('green', "balance_gamma 52,187,30")
def green():
    """Changes the color of the received image to green."""

@process_image('intensegreen', "balance_gamma 62,168,-238")
def intensegreen():
    """Changes the color of the received image to intense green."""

@process_image('burngreen', "balance_gamma 54,245,101")
def burngreen():
    """Changes the color of the received image to burn green."""

@process_image('blackyellow', "balance_gamma 62,18,-55")
def blackyellow():
    """Changes the color of the received image to black and yellow."""

@process_image('limelemon', "balance_gamma 67,118,-131")
def limelemon():
    """Changes the color of the received image to lime and lemon."""

@process_image('redsubtle', "balance_gamma 78,7,47")
def redsubtle():
    """Changes the color of the received image to subtle red."""

@process_image('bluepink', "balance_gamma 91,-107,190")
def bluepink():
    """Changes the color of the received image to blue and pink."""

@process_image('luminouspurple', "balance_gamma 92,-190,127")
def luminouspurple():
    """Changes the luminous colors of the received image to purple."""

@process_image('yellowgreen', "balance_gamma 95,237,-38")
def yellowgreen():
    """Changes the colors of the received image to yellow and green."""

@process_image('amber', "balance_gamma 96,41,-233")
def amber():
    """Changes the colors of the received image to amber."""

@process_image('subtleyellowandgreen', "balance_gamma 108,188,-195")
def subtleyellowandgreen():
    """Changes the colors of the received image to subtle yellow and green."""

@process_image('dullbrown', "balance_gamma 121,50,23")
def dullbrown():
    """Changes the colors of the received image to dull brown."""

@process_image('dullgreen', "balance_gamma 123,181,70")
def dullgreen():
    """Changes the colors of the received image to dull green."""

@process_image('amberbrown', "balance_gamma 127,20,-69")
def amberbrown():
    """Changes the colors of the received image to amber and brown."""

@process_image('yellowbrown', "balance_gamma 151,70,-89")
def yellowbrown():
    """Changes the colors of the received image to yellow and brown."""

@process_image('purplesubtle', "balance_gamma 176,76,251")
def purplesubtle():
    """Changes the colors of the received image to purple subtle."""

@process_image('whitish', "balance_gamma 189,205,177")
def whitish():
    """Changes the colors of the received image to whitish."""

@process_image('warm', "balance_gamma 190,75,-69")
def warm():
    """Changes the colors of the received image to warm tones."""

@click.group()
def cli():
    pass

cli.add_command(orange)
cli.add_command(pastelorange)
cli.add_command(green)
cli.add_command(intensegreen)
cli.add_command(burngreen)
cli.add_command(pastelgreen)
cli.add_command(luminousgreen)
cli.add_command(greenishhue)
cli.add_command(purplehue)
cli.add_command(palebluehue)
cli.add_command(palegreenhue)
cli.add_command(luminouslime)
cli.add_command(pastelturquoise)
cli.add_command(turquoise)
cli.add_command(pastelblue)
cli.add_command(blue)
cli.add_command(nightblue)
cli.add_command(luminousblue)
cli.add_command(luminousintenseblue)
cli.add_command(luminousindigo)
cli.add_command(indigo)
cli.add_command(paleindigo)
cli.add_command(palealien)
cli.add_command(lime)
cli.add_command(bluelime)
cli.add_command(blacklemon)
cli.add_command(blacklime)
cli.add_command(blackyellow)
cli.add_command(spectralpurple)
cli.add_command(pinkblue)
cli.add_command(blackred)
cli.add_command(bluepurplesubtle)
cli.add_command(purplesubtle)
cli.add_command(redsubtle)
cli.add_command(shininggreen)
cli.add_command(bluepurple)
cli.add_command(luminouslemonlime)
cli.add_command(darklemonlime)
cli.add_command(limelemon)
cli.add_command(bluepink)
cli.add_command(luminouspurple)
cli.add_command(yellowgreen)
cli.add_command(amber)
cli.add_command(subtleyellowandgreen)
cli.add_command(dullbrown)
cli.add_command(dullgreen)
cli.add_command(amberbrown)
cli.add_command(yellowbrown)
cli.add_command(whitish)
cli.add_command(warm)



if __name__ == "__main__":
    cli()
