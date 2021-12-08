from typing import Dict, List, Optional, Union


class Directory:
    def __init__(self):
        self.root: Dict = {}

    def _beautify(self, folders: Optional[Union[Dict, List]], indent: int = 0) -> None:
        if isinstance(folders, dict):
            for key, value in folders.items():
                print("  " * indent + str(key))
                if isinstance(value, dict) or isinstance(value, list):
                    self._beautify(value, indent + 1)

    def create(self, folder_name: str) -> None:
        folders: List = folder_name.split("/")
        new_directory: Dict = {}
        for key in reversed(folders):
            new_directory = {key: new_directory}

        self.root.update(new_directory)

    def move(self, folder_path: str) -> None:
        from_folder, to_folder = folder_path.split(" ")
        folders: List = from_folder.split("/")
        sub_folder: Dict = self.root
        for i in folders[:-1]:
            sub_folder = sub_folder[i]

        self.root[to_folder][folders[-1]] = sub_folder.pop(folders[-1])

    def delete(self, folder_name: str) -> None:
        folders: List = folder_name.split("/")
        sub_folder: Dict = self.root
        prev_folder: Dict = {}
        for folder in folders:
            prev_folder = sub_folder
            sub_folder = sub_folder.get(folder, None)
            if sub_folder is None:
                print(f"Cannot delete {folder_name} - {folder} does not exist")
                break
        if sub_folder is not None:
            del prev_folder[folders[-1]]

    def list(self) -> None:
        self._beautify(self.root)
