from abc import ABC, abstractmethod


class InMemoryDB(ABC):
    """interface representing in-memory relational databse"""

    @abstractmethod
    def create_table(self, table_name: str, schema: dict[str, type]) -> None:
        """Creates a new table with the specified name and schema. Schema is a dictionary where keys are column names and values are datatypes."""
        pass

    @abstractmethod
    def insert(self, table_name: str, row: dict[str, any]) -> None:
        """Inserts new row into specified table.
        Each row is represented as a dictionary with column names as keys and corresponding values.
        """
        pass

    @abstractmethod
    def delete(self, table_name: str, condition: dict[str, any]) -> bool:
        """Deletes row matching full info. Returns true if row deleted, False otherwise"""
        pass

    @abstractmethod
    def query(self, table_name: str, condition: dict[str, any]) -> list[dict[str, any]]:
        # Returns all rows from specified table that match condition
        # Condition is a dictionary where keys are col names and values are required values.
        pass

    @abstractmethod
    def update(
        self, table_name: str, condition: dict[str, any], updates: dict[str, any]
    ) -> bool:
        """Updates rows in speciifed table given condition. If updates return True, else False"""
        pass
