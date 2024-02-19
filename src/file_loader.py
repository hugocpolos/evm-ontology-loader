import csv
import os.path


class InvalidOntologyCSVFile(Exception):
    pass


class IndividualsLoader:
    def __init__(self, ontology, factory, files):
        self._files = files[0] if files is not None else list()
        self._ontology = ontology
        self._factory = factory
        self.needed_individuals = []
        self._read_csv_files()

    def _read_csv_files(self):
        for file in self._files:
            self._read_single_csv_file(file)

    def _read_single_csv_file(self, file):
        if not os.path.isfile(file):
            raise InvalidOntologyCSVFile(f"{file} not found.")

        with open(file, 'r') as fp:
            reader = csv.reader(fp)

            for i, line in enumerate(reader):
                if self._empty_line(line):
                    continue

                if self._is_commentary(line):
                    continue

                if self._is_individual(line):
                    try:
                        self._load_individual_csv_line(line)
                    except AssertionError as err:
                        raise InvalidOntologyCSVFile(
                            f"{file}:{i+1}. Error loading individual {err}")

                elif self._is_property(line):
                    try:
                        self._load_property_csv_line(line)
                    except AssertionError as err:
                        raise InvalidOntologyCSVFile(
                            f"{file}:{i+1}. Error loading property {err}")
                else:
                    raise InvalidOntologyCSVFile(
                        f"{file}: {i+1}. Invalid line(number of columns: {len(line)})")

    def _empty_line(self, csv_line: list):
        return len(csv_line) == 0

    def _is_commentary(self, csv_line: list):
        return csv_line[0].startswith('/*') and csv_line[-1].endswith('*/')

    def _is_individual(self, csv_line):
        return len(csv_line) == 2

    def _is_property(self, csv_line):
        return len(csv_line) == 3

    def _load_individual_csv_line(self, line):
        class_name, individual_name = line
        f = self._factory.get_factory_by_name(class_name)
        assert f is not None, f"Invalid class '{class_name}'"
        f(individual_name)

    def _load_property_csv_line(self, line):
        property_name, source, target = line

        source_individual = self._get_ontology_individual_by_name(source)
        assert source_individual is not None, f"individual '{source}' does not exist"
        self.needed_individuals.append(source_individual)

        target_individual = self._get_ontology_individual_by_name(target)
        assert target_individual is not None, f"individual '{target}' does not exist"
        self.needed_individuals.append(target_individual)

        assert hasattr(source_individual, property_name)
        f"property '{property_name}' does not exist in the class '{source_individual.is_a[0]}'"

        source_property = getattr(source_individual, property_name)
        if property_name in ['nepcategory', 'nepteam_type']:
            setattr(source_individual, property_name, target_individual)
        else:
            source_property.append(target_individual)

    def _get_ontology_individual_by_name(self, individual_name):
        for i in self._ontology.world.individuals():
            if i.name == individual_name:
                return i
