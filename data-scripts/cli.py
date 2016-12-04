import click
import petl as etl

from registry import process_registry
from turnout import process_turnout
from committee import process_committee

@click.group()
def cli():
    pass

@cli.command()
@click.option('--registry', '-r', 'registry_file', type=click.Path(),
              required=True, help='Qualified voter registry file')
@click.option('--turnout', '-t', 'turnout_file', type=click.Path(),
              required=True, help='Voter turnout file')
def voters(registry_file, turnout_file):
    """Cleans and combines registry and turnout files"""
    registry = process_registry(registry_file)
    turnout = process_turnout(turnout_file)

    registry.leftjoin(turnout, key=['ward', 'party']) \
        .tocsv()

@cli.command()
@click.argument('committee_file', type=click.Path())
def committee(committee_file):
    """Cleans committee person file"""
    process_committee(committee_file).tocsv()

if __name__ == '__main__':
    cli()