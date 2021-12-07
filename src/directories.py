from typing import Dict, List, Optional, Union


class Directory:

    def __init__(self):
        self.root: Dict = {}

    def _beautify(
            self, folders: Optional[Union[Dict, List]], indent: int=0
    ) -> None:
        if isinstance(folders, dict):
            for key, value in folders.items():
                print('  ' * indent + str(key))
                if isinstance(value, dict) or isinstance(value, list):
                    self._beautify(value, indent + 1)
        elif isinstance(folders, list):
            for folder in folders:
                self._beautify(folder, indent)

    def create(self, folder_name: str) -> None:
        print(f'CREATE {folder_name}')
        folders: List = folder_name.split('/')
        new_directory: Dict = {}
        for key in reversed(folders):
            new_directory = {key: new_directory}

        self.root.update(new_directory)

    def move(self, from_folder: str, to_folder: str) -> None:
        print(f'MOVE {from_folder} {to_folder}')
        folders: List = from_folder.split('/')
        sub_folder: Dict = self.root
        for i in folders[:-1]:
            sub_folder = sub_folder[i]

        self.root[to_folder][folders[-1]] = sub_folder.pop(folders[-1])

    def delete(self, folder_name: str) -> None:
        print(f'DELETE {folder_name}')
        folders: List = folder_name.split('/')
        sub_folder: Dict = self.root
        for folder in folders[:-1]:
            sub_folder = sub_folder.get(folder, None)
            if sub_folder is None:
                print(
                    f'Cannot delete {folder_name} - {folder} does not exist'
                )
                break
        if sub_folder is not None:
            del sub_folder[folders[-1]]

    def list(self) -> None:
        print('LIST')
        self._beautify(self.root)
