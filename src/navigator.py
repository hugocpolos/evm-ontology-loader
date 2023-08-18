class OntologyNavigator:
    def __init__(self, ontology):
        self.__onto__ = ontology

    @property
    def all_individuals(self):
        return self.__onto__.world.individuals()

    @property
    def all_classes(self):
        return self.__onto__.world.classes()

    @property
    def all_properties(self):
        return list(self.__onto__.world.properties())

    def dump_ontology(self):
        print("\nindividuals:")
        for i in self.all_individuals:
            print(f"\n\t{i}")
            if (properties := self.get_all_properties_of_an_individual(i)):
                print("\tproperties:")
            for p in properties:
                for _, target in p.get_relations():
                    print(f"\t\t{p} {target}")

            if (inv_p := self.get_all_inverse_properties_of_an_individual(i)):
                print("\tinverse properties:")
            for source, p in inv_p:
                print(f"\t\t{source} {p}")

    def search_individual_by_name(self, name, strict=False):
        name = name if strict else f'*{name}*'
        search_result = self.__onto__.search(iri=name)
        return search_result

    def get_individual_by_name(self, name):
        for i in self.all_individuals:
            if i.name == name:
                return i
        return None

    def get_class_by_name(self, name, strict=False):
        possible_classes = list()
        for cls in self.all_classes:
            if strict and cls.name == name:
                possible_classes.append(cls)
            if not strict and name in cls.name:
                possible_classes.append(cls)
        return possible_classes

    def get_individuals_of_a_class(self, cls):
        individuals = list(x for x in self.all_individuals if cls in x.is_instance_of)
        return individuals

    def get_individuals_of_a_class_by_class_name(self, classname, strict=False):
        search_result = list()
        for cls in self.get_class_by_name(classname):
            search_result.extend(self.__onto__.search(type=cls))
        return search_result

    def get_all_properties_of_an_individual(self, individual):
        return list(individual.get_properties())

    def get_all_inverse_properties_of_an_individual(self, individual):
        return list(individual.get_inverse_properties())

    def get_target_of_property(self, property_):
        pass

    def select_individual(self):
        print('\n'.join(f"[{i}] {ind}" for i, ind in enumerate(self.all_individuals)))

    def get_all_individuals(self):
        return list(self.all_individuals)

    def get_all_properties_relations_of_an_individual(self, individual):
        _props = self.get_all_properties_of_an_individual(individual)
        _all_relations = {x: list(x.get_relations()) for x in _props}

        _relations = {}

        for p, relation_list in _all_relations.items():
            for relation in relation_list:
                if relation[0] != individual:
                    continue
                if p not in _relations:
                    _relations[p] = list()

                _relations[p].append(relation)

        return _relations

    def get_individual_by_index(self, index):
        return self.get_all_individuals()[index]

    def get_property_of_individual_by_index(self, individual, index):
        return self.get_all_properties_of_an_individual(individual)[index]

    def get_inverse_property_of_individual_by_index(self, individual, index):
        return self.get_all_inverse_properties_of_an_individual(individual)[index]

    def deep_search_class_from_individual(self, individual, target_class, ignore_list):
        original_individual = individual
        previous_visited = list()
        return self._recursive_deep_search_class_from_individual(original_individual, target_class,
                                                                 previous_visited, ignore_list)

    def _recursive_deep_search_class_from_individual(self, individual, target_class, visited_list,
                                                     ignore_list):

        # print(f"search debug: \tindividual: {individual.name}")

        if individual not in ignore_list and target_class in [x.name for x in individual.is_a]:
            return individual

        if individual in visited_list:
            return None

        visited_list.append(individual)

        _tmp = self.get_all_properties_relations_of_an_individual(individual)

        for prop in _tmp:
            for relation in _tmp[prop]:
                next_hop = self._recursive_deep_search_class_from_individual(relation[1],
                                                                             target_class,
                                                                             visited_list,
                                                                             ignore_list)
                if next_hop:
                    return (relation[0], prop, next_hop)

    def deep_inverse_search_class_from_individual(self, individual, target_class, ignore_list):
        original_individual = individual
        previous_visited = list()
        return self._recursive_inverse_deep_search_class_from_individual(original_individual,
                                                                         target_class,
                                                                         previous_visited,
                                                                         ignore_list)

    def _recursive_inverse_deep_search_class_from_individual(self, individual, target_class,
                                                             visited_list, ignore_list):

        # print(f"search debug: \tindividual: {individual.name}")

        if individual not in ignore_list and target_class in [x.name for x in individual.is_a]:
            return individual

        if individual in visited_list:
            return None

        visited_list.append(individual)

        _tmp = self.get_all_inverse_properties_of_an_individual(individual)

        for relation in _tmp:
            next_hop = self._recursive_inverse_deep_search_class_from_individual(
                relation[0],
                target_class,
                visited_list,
                ignore_list)
            if next_hop:
                return (individual, relation[1], next_hop)
