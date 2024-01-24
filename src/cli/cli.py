from enum import Enum
import itertools
import readline
import json


class commands(Enum):
    help_ = ['help']
    list_ = ['list']
    select_ = ['select']
    unselect_ = ['unselect']
    # properties_ = ['properties']
    # iproperties_ = ['iproperties']
    follow_ = ['follow']
    ifollow_ = ['ifollow']
    # dsearch_ = ['dsearch']
    # isearch_ = ['isearch']
    search_ = ['search']
    show_ = ['show']
    exit_ = ['exit']
    nop_ = []


def get_a_selector_from_a_list(lst: list, index_selector=True) -> str:
    if index_selector:
        return '\n'.join(f"[{i}] {item}" for i, item in enumerate(lst))

    return '\n'.join(f"{item}" for item in lst)


class Cli():
    _select_autocomplete_list = list()

    def __init__(self, controller=None, configuration=None):
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self._autocompleter)
        self._selected_individual = None
        self._selected_history = []
        self._controller = controller
        self._set_ps1()
        self._config = configuration if configuration else self._load_default_configuration()
        self._select_autocomplete_list = self._fill_select_autocomplete_list()

    def _fill_select_autocomplete_list(self):
        if not self._controller:
            return list()
        return_list = self._controller.get_all_individuals()
        return [x.name for x in return_list]

    def _autocompleter(self, text, state):
        options = list(x for x in itertools.chain.from_iterable(x.value for x in commands) if
                       x.startswith(text))

        buffer = readline.get_line_buffer()

        if buffer.startswith('search') or buffer.startswith('isearch') or buffer.startswith('dsearch'):
            options = list(x for x in self._config.get("SEARCH_OPTIONS") if x.startswith(text))
        elif buffer.startswith('select'):
            options = list(x for x in self._select_autocomplete_list if x.startswith(text))

        if state < len(options):
            return options[state]
        else:
            return None

    def _print_message_from_cli_config(self, message, **kwargs):
        _msg_l = self._config.get(message, [])
        print('\n'.join(_msg_l).format(**kwargs))

    def _load_default_configuration(self):
        with open('cli/configuration.json') as fp:
            _cfg = json.load(fp)
        return _cfg

    def _set_ps1(self, value=None):
        if value:
            self._ps1 = f"({value})> "
        else:
            self._ps1 = "> "

    def _help(self, *args):
        if len(args) > 1:
            return self._help()
        if len(args) == 0:
            return self._print_message_from_cli_config('HELP_MESSAGE')

        _cmd = self.get_command_from_raw_text(args[0])
        return {
            commands.help_: self._help,
            commands.list_: self._list_help_message,
            commands.select_: self._select_help_message,
            commands.unselect_: self._unselect_help_message,
            # commands.properties_: self._properties_help_message,
            # commands.iproperties_: self._iproperties_help_message,
            commands.follow_: self._follow_help_message,
            commands.ifollow_: self._ifollow_help_message,
            # commands.dsearch_: self._dsearch_help_message,
            # commands.isearch_: self._isearch_help_message,
            commands.search_: self._search_help_message,
            commands.show_: self._show_help_message,
            commands.exit_: self._exit_help_message,
            commands.nop_: self._unknown_command,
        }.get(_cmd, self._unknown_command)()

    def _list_help_message(self):
        self._print_message_from_cli_config('LIST_HELP_MESSAGE')

    def _select_help_message(self):
        self._print_message_from_cli_config('SELECT_HELP_MESSAGE')

    def _unselect_help_message(self):
        self._print_message_from_cli_config('UNSELECT_HELP_MESSAGE')

    def _properties_help_message(self):
        self._print_message_from_cli_config('PROPERTIES_HELP_MESSAGE')

    def _iproperties_help_message(self):
        self._print_message_from_cli_config('IPROPERTIES_HELP_MESSAGE')

    def _follow_help_message(self):
        self._print_message_from_cli_config('FOLLOW_HELP_MESSAGE')

    def _ifollow_help_message(self):
        self._print_message_from_cli_config('IFOLLOW_HELP_MESSAGE')

    def _dsearch_help_message(self):
        self._print_message_from_cli_config('DSEARCH_HELP_MESSAGE')

    def _isearch_help_message(self):
        self._print_message_from_cli_config('ISEARCH_HELP_MESSAGE')

    def _search_help_message(self):
        self._print_message_from_cli_config('SEARCH_HELP_MESSAGE')

    def _show_help_message(self):
        self._print_message_from_cli_config('SHOW_HELP_MESSAGE')

    def _exit_help_message(self):
        self._print_message_from_cli_config('EXIT_HELP_MESSAGE')

    def _unknown_command(self, *args):
        self._print_message_from_cli_config('UNKNOWN_COMMAND_MESSAGE')

    def _no_selected_individual(self, *args):
        self._print_message_from_cli_config('NO_SELECTED_INDIVIDUAL')

    def _out_of_range(self, field, index):
        self._print_message_from_cli_config('OUT_OF_RANGE', field=field, index=index)

    def _not_found(self, field, *args):
        self._print_message_from_cli_config('NOT_FOUND', field=field, individual=' '.join(str(x) for x
                                                                                          in args))

    def _search_not_found(self, individual, class_name):
        self._print_message_from_cli_config('SEARCH_NOT_FOUND', individual=individual,
                                            class_name=class_name)

    def _update_selected_individual(self, individual):
        self._selected_individual = individual
        if self._selected_individual:
            self._selected_history.append(individual)
        self._set_ps1(self._selected_individual)

    def _list(self, *args):
        res = ""
        list_individual_format = "\t({class_name}) {individual_name}"

        if self._controller:
            res = get_a_selector_from_a_list(list_individual_format.format(class_name=' / '.join(
                z.name for z in x.is_instance_of),
                individual_name=x) for x in self._controller.get_all_individuals())
        print("[#id]\t(Class) individual_name")
        print(res)

    def _select(self, *args):
        if not self._controller:
            return

        if len(args) == 0:
            return self._select_help_message()

        if len(args) == 1 and args[0].isnumeric():
            return self._select_by_index(args[0])

        _s = ' '.join([*args])
        if (ind := self._controller.get_individual_by_name(name=_s)):
            self._update_selected_individual(ind)
            return

        return self._not_found('individual', *args)

    def _select_by_index(self, index_s):
        try:
            index = int(index_s)
            assert index >= 0
        except (ValueError, AssertionError):
            return self._select_help_message()

        try:
            self._update_selected_individual(self._controller.get_individual_by_index(index))
        except IndexError:
            return self._out_of_range('individual', index)
        self._set_ps1(self._selected_individual)

    def _unselect(self, *args):
        if len(self._selected_history) <= 1:
            self._selected_history = []
            return self._update_selected_individual(None)
        self._selected_history.pop()
        _last_individual = self._selected_history.pop()
        self._update_selected_individual(_last_individual)

    def _properties(self, *args):
        if not self._selected_individual:
            return self._no_selected_individual()

        res = []
        if self._controller:
            _tmp = self._controller.get_all_properties_relations_of_an_individual(
                self._selected_individual)
            for prop in _tmp:
                for relation in _tmp[prop]:
                    res.append(f"{relation[0]} -> {prop} -> {relation[1]}")

        print(get_a_selector_from_a_list(res))

    def _iproperties(self, *args):
        if not self._selected_individual:
            return self._no_selected_individual()

        res = []
        if self._controller:
            _tmp = self._controller.get_all_inverse_properties_of_an_individual(
                self._selected_individual)
            for relation in _tmp:
                res.append(f"{relation[0]} -> {relation[1]} -> {self._selected_individual}")

        print(get_a_selector_from_a_list(res))

    def _follow(self, *args):
        if not self._selected_individual:
            return self._no_selected_individual()

        if len(args) != 1:
            return self._follow_help_message()

        try:
            index = int(args[0])
            assert index >= 0
        except (ValueError, AssertionError):
            return self._select_help_message()

        res = []
        if self._controller:
            _tmp = self._controller.get_all_properties_relations_of_an_individual(
                self._selected_individual)
            for prop in _tmp:
                for relation in _tmp[prop]:
                    res.append(relation[1])
        try:
            self._update_selected_individual(res[index])
        except IndexError:
            self._out_of_range('property', index)

    def _ifollow(self, *args):
        if not self._selected_individual:
            return self._no_selected_individual()

        if len(args) != 1:
            return self._ifollow_help_message()

        try:
            index = int(args[0])
            assert index >= 0
        except (ValueError, AssertionError):
            return self._select_help_message()

        res = []
        if self._controller:
            _tmp = self._controller.get_all_inverse_properties_of_an_individual(
                self._selected_individual)
            for relation in _tmp:
                res.append(relation[0])
        try:
            self._update_selected_individual(res[index])
        except IndexError:
            self._out_of_range('inverse property', index)

    def _get_individual_from_dsearch_result(self, result):
        if type(result) == tuple:
            return self._get_individual_from_dsearch_result(result[2])

        return result

    def _get_textual_output_from_dsearch_result(self, result):
        if type(result) == tuple:
            next_hop = self._get_textual_output_from_dsearch_result(result[2])
            return f"{result[0]} -> {result[1]} -> {next_hop}"

        return result

    def _dsearch(self, *args, quiet=False):
        if not self._selected_individual:
            if not quiet:
                return self._no_selected_individual()
            return

        if len(args) != 1:
            if not quiet:
                return self._dsearch_help_message()
            return

        if not self._controller:
            return

        target_class = args[0]
        if target_class not in self._config.get("SEARCH_OPTIONS"):
            if not quiet:
                print(f"{target_class} is not a valid searchable class")
            return

        already_found = list()
        dsearch_result = list()
        while (result :=
                self._controller.deep_search_class_from_individual(self._selected_individual,
                                                                   target_class,
                                                                   already_found)):
            already_found.append(self._get_individual_from_dsearch_result(result))
            dsearch_result.append(self._get_textual_output_from_dsearch_result(result))

        if len(dsearch_result) == 0:
            if not quiet:
                self._search_not_found(self._selected_individual, target_class)
            return dsearch_result

        if not quiet:
            print(get_a_selector_from_a_list(dsearch_result))
        return dsearch_result

    def _get_individual_from_isearch_result(self, result):
        return self._get_individual_from_dsearch_result(result)

    def _get_textual_output_from_isearch_result(self, result):
        if type(result) == tuple:
            next_hop = self._get_textual_output_from_isearch_result(result[2])
            return f"{result[0]} <- {result[1]} <- {next_hop}"

        return result

    def _isearch(self, *args, quiet=False):
        if not self._selected_individual:
            if not quiet:
                return self._no_selected_individual()
            return

        if len(args) != 1:
            if not quiet:
                return self._dsearch_help_message()
            return

        if not self._controller:
            return

        target_class = args[0]
        if target_class not in self._config.get("SEARCH_OPTIONS"):
            if not quiet:
                print(f"{target_class} is not a valid searchable class")
            return

        already_found = list()
        isearch_result = list()
        while (result :=
                self._controller.deep_inverse_search_class_from_individual(
                    self._selected_individual,
                    target_class,
                    already_found)):
            already_found.append(self._get_individual_from_isearch_result(result))
            isearch_result.append(self._get_textual_output_from_isearch_result(result))

        if len(isearch_result) == 0:
            if not quiet:
                self._search_not_found(self._selected_individual, target_class)
            return isearch_result

        if not quiet:
            print(get_a_selector_from_a_list(isearch_result))
        return isearch_result

    def _search(self, *args):
        if not self._selected_individual:
            return self._no_selected_individual()

        if len(args) != 1:
            return self._dsearch_help_message()

        if not self._controller:
            return

        target_class = args[0]
        if target_class not in self._config.get("SEARCH_OPTIONS"):
            print(f"{target_class} is not a valid searchable class")
            return

        dsearch = self._dsearch(*args, quiet=True)
        isearch = self._isearch(*args, quiet=True)
        print(get_a_selector_from_a_list(dsearch + isearch, index_selector=False))

        if len(dsearch) + len(isearch) == 0:
            return self._search_not_found(self._selected_individual, target_class)

    def _show(self, *args):
        if not self._selected_individual:
            return self._no_selected_individual()

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
        if self._controller:
            _tmp = self._controller.get_all_properties_relations_of_an_individual(
                self._selected_individual)
            i = 0
            for prop in _tmp:
                for relation in _tmp[prop]:
                    properties.append(f"[{i}] {relation[0]} -> {prop} -> {relation[1]}")
                    i += 1

        iproperties = []
        if self._controller:
            _tmp = self._controller.get_all_inverse_properties_of_an_individual(
                self._selected_individual)
            for i, relation in enumerate(_tmp):
                iproperties.append(
                    f"[{i}] {relation[0]} -> {relation[1]} -> {self._selected_individual}")

        print(show_template.format(
            individual_name=self._selected_individual.name,
            instance_of=', '.join(z.name for z in self._selected_individual.is_instance_of),
            properties='\n'.join(properties),
            inverse_properties='\n'.join(iproperties)
        ))

    def _exit(self, *args):
        pass

    def get_command_from_raw_text(self, raw_text):
        for c in commands:
            if raw_text in c.value:
                return c
        return commands.nop_

    def execute_command(self, cmd, *args):
        {
            commands.help_: self._help,
            commands.list_: self._list,
            commands.select_: self._select,
            commands.unselect_: self._unselect,
            # commands.properties_: self._properties,
            # commands.iproperties_: self._iproperties,
            commands.follow_: self._follow,
            commands.ifollow_: self._ifollow,
            # commands.dsearch_: self._dsearch,
            # commands.isearch_: self._isearch,
            commands.search_: self._search,
            commands.show_: self._show,
            commands.exit_: self._exit,
            commands.nop_: self._unknown_command,
        }.get(cmd, self._unknown_command)(*args)

    def main_loop(self):
        _command = None
        _args = None
        print()
        self._print_message_from_cli_config('WELCOME_MESSAGE')
        _args = []
        while _command != commands.exit_:
            try:
                raw_input = list(filter(('').__ne__, input(self._ps1).split(' ')))
                line = raw_input[0]
                _args = raw_input[1:]
            except EOFError:
                print('exit')
                line = 'exit'
            except IndexError:
                continue

            _command = self.get_command_from_raw_text(line)
            self.execute_command(_command, *_args)


if __name__ == '__main__':
    Cli().main_loop()
