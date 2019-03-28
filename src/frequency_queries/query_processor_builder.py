from src.frequency_queries.query_processors import *
from src.frequency_queries.storage_keeper import StorageKeeper


class QueryProcessorBuilder:
    storage_keeper = StorageKeeper()

    def create_processor(self, query_type, element):
        if query_type == 1:
            processor = AppendingProcessor(element, self.storage_keeper)
        elif query_type == 2:
            processor = RemovingProcessor(element, self.storage_keeper)
        elif query_type == 3:
            processor = CountingProcessor(element, self.storage_keeper)

        return processor
