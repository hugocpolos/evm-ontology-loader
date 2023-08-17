from abc import ABC, abstractmethod
import csv


class _FileLoader(ABC):
    def __init__(self, files):
        self._files = files[0] if files is not None else list()
        self._read_csv_files()

    def _read_csv_files(self):
        for file in self._files:
            self._read_single_csv_file(file)

    def _read_single_csv_file(self, file, ignore_header=True):
        with open(file, 'r') as fp:
            reader = csv.reader(fp)

            if ignore_header:
                next(reader)

            for line in reader:
                self.load_csv_line(line)

    @abstractmethod
    def load_csv_line(self, line):
        pass


class IndividualsLoader(_FileLoader):
    def __init__(self, factory, files):
        self._factory = factory
        super().__init__(files)

    def load_csv_line(self, line):
        class_name, individual_name = line
        f = self._factory.get_factory_by_name(class_name)
        f(individual_name)


class PropertiesLoader(_FileLoader):
    def __init__(self, ontology, files):
        self._ontology = ontology
        super().__init__(files)

    def load_csv_line(self, line):
        property_name, source, target = line
        source_individual = self.get_ontology_individual_by_name(source)
        target_individual = self.get_ontology_individual_by_name(target)

        source_property = getattr(source_individual, property_name)
        source_property.append(target_individual)

    def get_ontology_individual_by_name(self, individual_name):
        for i in self._ontology.individuals():
            if i.name == individual_name:
                return i
