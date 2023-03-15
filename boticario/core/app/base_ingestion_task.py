from boticario.core.app.task import Task
from boticario.logger import get_logging

logging = get_logging(__name__)


class BaseIngestionTask(Task):
    def run(self):
        logging.info('Base Ingestion')
