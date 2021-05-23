import os
import yaml
import re


def load_configuration(config_path=None, tag="!ENV"):
    pattern = re.compile(".*?\\${(\\w+)}.*?")
    loader = yaml.SafeLoader
    loader.add_implicit_resolver(tag, pattern, None)

    def constructor_env_variables(loader, node):
        value = loader.construct_scalar(node)
        match = pattern.findall(value)
        if match:
            full_value = value
            for g in match:
                full_value = full_value.replace(f"${{{g}}}", os.environ.get(g, ""))
            return full_value
        return value

    loader.add_constructor(tag, constructor_env_variables)

    if config_path:
        with open(config_path) as config_data:
            return yaml.load(config_data, Loader=loader)
    else:
        raise ValueError("Either a path or data should be defined as input")