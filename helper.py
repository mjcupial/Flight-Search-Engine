def save_data_to_file(data, file_name):
    """To format json in PyCharm: Ctrl+Alt+L"""
    with open(f"{file_name}", "w") as file:
        file.write(str(data))
        file.close()