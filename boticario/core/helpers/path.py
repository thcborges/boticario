from datetime import date
from pathlib import Path


def get_root_path() -> Path:
    """Returns the root path to the package

    Returns:
        Path: root path to the package
    """
    return Path(__file__).parent.parent.parent


def get_config_file(config: str) -> Path:
    root = get_root_path()

    config_file = {'logger': Path('conf/logging_custom.yaml')}.get(config)
    if not config_file:
        raise NotImplementedError(f'There is no config file for {config}')
    config_path = root / config_file
    return config_path


def get_logging_path() -> Path:
    root = get_root_path()
    today = date.today().strftime('%Y-%m-%d')
    logging_path = root / 'log' / today

    logging_path.mkdir(parents=True, exist_ok=True)
    return logging_path


def get_data_path() -> Path:
    root = get_root_path()
    data_path = root / 'data'
    return data_path
