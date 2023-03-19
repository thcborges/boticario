from datetime import date
from pathlib import Path

PROCESSED_FOLDER = '.processed'


def get_root_path() -> Path:
    """Returns the root path to the package

    Returns:
        Path: root path to the package
    """
    return Path(__file__).parents[2]


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


def set_processed_folder(path: Path | str) -> Path:
    return Path(path) / PROCESSED_FOLDER


def is_processed_path(path: Path | str) -> bool:
    return PROCESSED_FOLDER in Path(path).parts


ROOT_PATH = get_root_path()
DATA_PATH = ROOT_PATH / 'data'
QUERY_PATH = ROOT_PATH / 'core' / 'sql'
