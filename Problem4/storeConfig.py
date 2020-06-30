#Recursive helper to update nested dictionary
def update_helper(modify_data, data):
    for key, value in modify_data.items():
        if isinstance(value, dict):  # Value is a dict
            tmp = update_helper(value, data.get(key, {}))
            data[key] = tmp
        elif isinstance(value, list):  # Value is a list, each element in the list is a dict
            ori_list_in_dict = data.get(key, [])
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    update_helper(item, ori_list_in_dict[index])
        else:
            data[key] = value
    return data


class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    def update(self, modify_data):
        update_helper(modify_data, self.data)
