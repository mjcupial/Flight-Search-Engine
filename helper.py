import json
def save_data_to_file(data, file_name):
    """To format json in PyCharm: Ctrl+Alt+L"""
    with open(f"{file_name}", "w") as file:
        file.write(str(data))
        file.close()

def read_data_from_file(file_name):
    """Read data from *.json to avoid limitation request"""
    with open(file_name, "r") as file:
        data = json.load(file)
        file.close()
        return data