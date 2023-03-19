from boticario.core.app.task import Task
from boticario.core.dpo.base_dpo import BaseDpo
from boticario.logger import get_logging

logging = get_logging(__name__)


class BaseTable2Task(Task):
    def create_table(self):
        BaseDpo.create_table_aggregating_sales_by_brand_and_type()

    def run(self):
        self.create_table()
