#!/usr/bin/env python

import owlready2
import argparse

from my_logging import logging
from factory import Factory
from file_loader import IndividualsLoader, InvalidOntologyCSVFile
from cli.cli import Cli

import navigator

import show_functions

OWL_FILE_LOCATION = "./ontologies/"
OWL_EVM_FILE = "evm.owl"


def get_cli_arguments():
    parser = argparse.ArgumentParser(
        prog='evm_loader',
        description='''This program loads the Ethical Violation Management Ontology definition on the
        memory and allows the user to initialize a set of individuals and its relations for this
        ontology definition from multiple files(see "-i" and "-p" parameters). If no extra
        parameters are given, the program will load everything, perform the ontology reasoning and
        display all the relationships and entities that were both given by the user or reasoned by
        the program. If the "--cli" parameter is entered, however, the program won\'t display
        those results and will start a command line interface application that allows the user to
        navigate and visualize the ontology entities by themself.''',
        epilog='The evm_loader app was developed by Hugo Constantinopolos.\
        hugo.constantinopolos@inf.ufrgs.br')
    parser.add_argument('-f', '--input-file', action='append', nargs='+', help='''
    CSV files containing ontology individuals to be loaded.
    ''')
    parser.add_argument('--cli', action='store_true',
                        help="start the command line interface app after loading the ontology")
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='display reasoning log messages')
    parser.add_argument('-l', '--load-only', action='store_true', help='''do nothing after loading
        the individuals. Specially useful when combined with -v to debug the ontology loading and
        reasoning.''')
    parser.add_argument('-r', '--rules', action='store_true')
    return parser.parse_args()


def finish():
    logging.info("Exiting")


def main():
    args = get_cli_arguments()

    logging.info("Starting")
    # load the ontology
    logging.info(f"Loading the ontology from the {OWL_FILE_LOCATION}{OWL_EVM_FILE} file")
    ontology = owlready2.get_ontology(f"{OWL_FILE_LOCATION}/{OWL_EVM_FILE}").load()
    logging.info("The EVM ontology has been successfully loaded")
    owlready2.sync_reasoner_hermit(infer_property_values=True, debug=False)

    with ontology:
        # Initialize the instance factory
        factory = Factory(ontology)
        try:
            loader = IndividualsLoader(ontology, factory, args.input_file)
        except InvalidOntologyCSVFile as err:
            logging.error(err)
            return finish()

    nav = navigator.OntologyNavigator(ontology)

    # Run the HermiT reasoner if there is individuals
    try:
        owlready2.sync_reasoner_hermit(infer_property_values=True, debug=args.verbose)
        logging.info("HermiT reasoner has successfully run")
    except Exception as err:
        if args.verbose:
            logging.error(err)
        else:
            logging.warning("HermiT reasoner did not run")

    # clean up the ontology
    for individual in ontology.world.individuals():
        if individual not in loader.needed_individuals:
            owlready2.destroy_entity(individual)

    if args.rules:
        show_functions.show_all_rules(nav)

    if args.load_only:
        return finish()

    if args.cli:
        cli = Cli(controller=nav)
        cli.main_loop()

    elif nav.get_number_of_individuals() > 0:
        print("="*40)
        for individual in nav.all_individuals:
            show_functions.show_individual(individual, nav)
            print("="*40)

    return finish()


if __name__ == "__main__":
    main()
