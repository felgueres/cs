from memdb import InMemoryDB

class MemDBImpl(InMemoryDB):
    '''In memory db implementation'''
    def __init__(self):
        self.tables = {}
    
    def create_table(self, table_name: str, schema: dict[str, type]) -> None:
        self.tables[table_name] = {
            'schema': schema,
            'rows': []
        }
        return True

    def _check_table_exists_and_schema(self, table_name, row, all_cols=False):
        if table_name not in self.tables: raise ValueError('no table with that name')
        cnt_cols = 0
        for col,v in row.items():
            if not (col in self.tables[table_name]['schema'] and type(v) == self.tables[table_name]['schema'][col]):
                raise ValueError("incorrect data or schema")
            cnt_cols+=1
        if all_cols: assert cnt_cols == len(self.tables[table_name]['schema']), 'missing cols'
        return True
    
    def insert(self, table_name: str, row: dict[str, any]) -> bool:
        self._check_table_exists_and_schema(table_name, row, all_cols=True)
        self.tables[table_name]['rows'].append(row)
        return True

    def delete(self, table_name: str, condition: dict[str, any]) -> bool:
        self._check_table_exists_and_schema(table_name, condition)
        
        row_matches = []
        for i,row in enumerate(self.tables[table_name]['rows']):
            matches = 0
            for col, val in row.items():
                if col in condition and condition[col] == val:
                    matches += 1
                else:
                    break
            if matches == len(condition):
                row_matches.append(i)
            
        for i in row_matches:
            self.tables[table_name]['rows'].pop(i)

        return True if row_matches else False
    
    def query(self, table_name: str, condition: dict[str, any]) -> list[dict[str, any]]:
        self._check_table_exists_and_schema(table_name, condition)
        row_matches = []
        for i,row in enumerate(self.tables[table_name]['rows']):
            matches = 0
            for col, val in row.items():
                if col in condition and condition[col] == val:
                    matches += 1
                else:
                    break
            if matches == len(condition):
                row_matches.append(i)
        matched_rows = [self.tables[table_name]['rows'][i] for i in row_matches]
        return matched_rows

    def update(self, table_name: str, condition: dict[str, any], updates: dict[str, any]) -> bool:
        self._check_table_exists_and_schema(table_name, condition)
        self._check_table_exists_and_schema(table_name, updates)
        row_matches = []
        for i,row in enumerate(self.tables[table_name]['rows']):
            matches = 0
            for col, val in row.items():
                if col in condition and condition[col] == val:
                    matches += 1
                else:
                    break
            if matches == len(condition):
                row_matches.append(i)
        for i in row_matches:
            self.tables[table_name]['rows'][i].update(updates)

        return True if row_matches else False
