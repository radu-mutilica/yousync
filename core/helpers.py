import yaml


def get_last_run(path):
    try:
        with open(path, 'r') as f:
            return yaml.load(f)
    except (yaml.YAMLError, FileNotFoundError):
        return {}
