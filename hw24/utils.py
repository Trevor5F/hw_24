import re
from typing import Iterator, List, Any


def build_query(cmd: str, val: str, file_list: Iterator) -> List[Any]:
    if cmd == 'filter':
        return list(filter(lambda x: val in x, file_list))

    if cmd == 'map':
        return list([x.split()[int(val)] for x in file_list])

    if cmd == 'unique':
        return list(set(file_list))

    if cmd == 'sort':
        reverse = val == 'disc'
        return list(sorted(file_list, reverse=reverse))

    if cmd == 'limit':
        return list(file_list)[:int(val)]

    if cmd == 'regex':
        regex = re.compile(val)
        return list(filter(lambda x: regex.search(x), file_list))
    return []

