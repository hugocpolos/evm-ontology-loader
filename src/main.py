import owlready2 as owl
import argparse

from my_logging import logging
from factory import Factory
from file_loader import IndividualsLoader, PropertiesLoader
from cli.cli import Cli

import world
import navigator

OWL_FILE_LOCATION = "/home/hugo.marredo/Documents/personal/tg2/python3/ontologies/"
OWL_EVM_FILE = "evm.owl"

ontology = None
sync_reasoner = None
w = None
nav = None


def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--load-individuals-from-file', action='append', nargs='+')
    parser.add_argument('-p', '--load-properties-from-file', action='append', nargs='+')
    parser.add_argument('--cli', action='store_true')
    return parser.parse_args()


def main():
    logging.info("Starting")

    args = get_cli_arguments()
    global ontology
    global sync_reasoner
    global w
    global nav

    print(args.load_individuals_from_file)
    print(args.load_properties_from_file)

    # load ontology
    ontology = owl.get_ontology(f"{OWL_FILE_LOCATION}/{OWL_EVM_FILE}").load()

    with ontology:
        # Initialize the instance factory
        factory = Factory(ontology)

        # w = world.World(factory, property_factory, world.WorldScenario.scenario_one)

        IndividualsLoader(factory, args.load_individuals_from_file)
        PropertiesLoader(ontology, args.load_properties_from_file)

    # Run the HermiT reasoner
    owl.sync_reasoner_hermit()

    nav = navigator.OntologyNavigator(ontology)

    if args.cli:
        cli = Cli(controller=nav)
        cli.main_loop()

    logging.info("Exiting")


if __name__ == "__main__":
    main()
    pass
