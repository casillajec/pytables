from typing import Self

class PyTable:
    titles: list[str]
    _headers: list[str]
    rows: list[list[str]]
    row_length: int
    _borders: bool

    def __init__(self):
        self.titles = list()
        self._headers = list()
        self.rows = list()
        self._borders = False
        self.row_length = None
    
    @staticmethod
    def builder() -> Self:
        return PyTable()
    
    def title(self, title: str) -> Self:
        self.titles.append(title)
        return self

    def validate_row_length(self, against: list):
        if self.row_length and len(against) != self.row_length:
            raise ValueError(f'Fuck you row length is {self.row_length}')


    def headers(self, headers: list[str]) -> Self:
        self.validate_row_length(headers)

        self._headers = headers
        self.row_length = len(headers)
        
        print(self)
        return self

    def row(self, row: list[str]) -> Self:
        self.validate_row_length(row)

        self.rows.append(row)
        self.row_length = len(row)

        return self

    def rows(self, rows: list[list[str]]) -> Self:
        if len(rows) < 1:
            raise ValueError('Cannot set empty rows, got rows={rows}')
        row_length = len(rows[0])

        if any(len(row) != row_length for row in rows):
            raise ValueError('Received something other than a square matrix, fix your shit')

        self.validate_row_length(rows[0])

        self.rows = rows
        self.row_length = len(rows[0])

        return self

    def borders(self, borders: bool = True) -> Self:
        self._borders = borders
        return self

    def print(self):
        PADDING = 2
        BORDER_WIDTH = 1
        
        if self._borders:
            total_extra_space = ((PADDING + BORDER_WIDTH) * self.row_length) + 1
            title_extra = PADDING + (BORDER_WIDTH * 2)
        else:
            total_extra_space = (PADDING * self.row_length)
            title_extra = PADDING


        effective_rows = [self._headers, *self.rows]

        column_lengths = [
                max(len(row[i]) for row in effective_rows)
                for i in range(self.row_length)
        ]
        total_length = sum(column_lengths) + total_extra_space
        
        table_str = ''
        for title in self.titles:
            title_str = f'{title:<{total_length - title_extra}}'
            if self._borders:
                title_str = f'| {title_str} |'
            else:
                title_str = f' {title_str} '
            table_str += f'{title_str}\n'
            table_str += ('-' * total_length) + '\n'

        for row in effective_rows:
            row_str = '|' if self._borders else ''
            for column_length, value in zip(column_lengths, row):
                value_str = f'{value:>{column_length}}'
                if self._borders:
                    value_str = f' {value_str} |'
                row_str += value_str

            table_str += f'{row_str}\n'

        print(table_str)

if __name__ == '__main__':
    (PyTable.builder()
        .title('Er Diavro')
        .title('ksksksksksksks')
        .headers(['a', 'b', 'c', 'diewhenallisnone'])
        .row(['1', '2', '3', 'a'])
        .row(['4', '5', '6', 'b'])
        .row(['7', '8', '9ss', 'c'])
        .row(['wakawakawaka', '', 'erdiablo', 'x'])
        .borders()
        .print())
        
