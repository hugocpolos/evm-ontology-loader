from abc import ABC, abstractmethod
import csv
import os.path


class InvalidOntologyCSVFile(Exception):
    pass


class _FileLoader(ABC):
    def __init__(self, files):
        self._files = files[0] if files is not None else list()
        self._read_csv_files()

    def _read_csv_files(self):
        for file in self._files:
            self._read_single_csv_file(file)

    def _read_single_csv_file(self, file, ignore_header=True):
        if not os.path.isfile(file):
            raise InvalidOntologyCSVFile(f"{file} not found.")

        with open(file, 'r') as fp:
            reader = csv.reader(fp)

            if ignore_header:
                next(reader)

            for i, line in enumerate(reader):
                if self._is_commentary(line):
                    continue
                try:
                    self.load_csv_line(line)
                except AssertionError as err:
                    raise InvalidOntologyCSVFile(f"{file}:{i+1}. {err}")

    def _is_commentary(self, csv_line: list):
        return csv_line[0].startswith('/*') and csv_line[-1].endswith('*/')

    @abstractmethod
    def load_csv_line(self, line):
        pass


class IndividualsLoader(_FileLoader):
    def __init__(self, factory, files):
        self._factory = factory
        super().__init__(files)

    def load_csv_line(self, line):
        assert len(line) == 2, "Wrong number of columns"
        class_name, individual_name = line
        f = self._factory.get_factory_by_name(class_name)
        assert f is not None, f"Invalid class '{class_name}'"
        f(individual_name)


class PropertiesLoader(_FileLoader):
    def __init__(self, ontology, files):
        self._ontology = ontology
        super().__init__(files)

    def load_csv_line(self, line):
        assert len(line) == 3, "Wrong number of columns"
        property_name, source, target = line

        source_individual = self.get_ontology_individual_by_name(source)
        assert source_individual is not None, f"individual '{source}' does not exist"

        target_individual = self.get_ontology_individual_by_name(target)
        assert target_individual is not None, f"individual '{target}' does not exist"

        assert hasattr(source_individual, property_name), \
            f"property '{property_name}' does not exist in the class '{source_individual.is_a[0]}'"

        source_property = getattr(source_individual, property_name)
        source_property.append(target_individual)

    def get_ontology_individual_by_name(self, individual_name):
        for i in self._ontology.individuals():
            if i.name == individual_name:
                return i
