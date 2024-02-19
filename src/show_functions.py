def show_individual(individual, controller):
    show_template = \
        """
Name: {individual_name}
Instance of: {instance_of}

Properties:
{properties}

Inverse properties:
{inverse_properties}

"""

    properties = []
    if controller:
        _tmp = controller.get_all_properties_relations_of_an_individual(individual)
        for prop in _tmp:
            for relation in _tmp[prop]:
                properties.append(f"{relation[0]} -> {prop} -> {relation[1]}")

    iproperties = []
    if controller:
        _tmp = controller.get_all_inverse_properties_of_an_individual(individual)
        for relation in _tmp:
            iproperties.append(f"{relation[0]} -> {relation[1]} -> {individual}")

    print(show_template.format(
        individual_name=individual.name,
        instance_of=', '.join(z.name for z in individual.is_instance_of),
        properties='\n'.join(properties),
        inverse_properties='\n'.join(iproperties)
    ))


def show_all_rules(controller):
    for r in controller.all_rules:
        # print(r.head)
        # print()
        try:
            print(r)
        except:
            for i in r.body:
                try:
                    print(i)
                except:
                    print(i.generate_default_name())
            print(r.head)

        print()
