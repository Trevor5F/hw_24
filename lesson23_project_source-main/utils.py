def build_query(cmd, val, file_list):
    if cmd == 'filter':
        return filter(lambda x: val in x, file_list)

    if cmd == 'map':
        val = int(val)
        return [x.split()[val] for x in file_list]

    if cmd == 'unique':
        return list(set(file_list))

    if cmd == 'sort':
        reverse = val == 'disc'
        return sorted(file_list, reverse=reverse)

    if cmd == 'limit':
        val = int(val)
        return list(file_list)[:val]

