from src.directories import Directory


def test_create_directory(directory_empty: Directory) -> None:
    folder_name: str = 'flowers/rose'
    directory_empty.create(folder_name=folder_name)
    assert directory_empty.root == {'flowers': {'rose': {}}}

    new_folder_name: str = 'flowers/rose/lincoln'
    directory_empty.create(folder_name=new_folder_name)

    assert directory_empty.root == {'flowers': {'rose': {'lincoln': {}}}}


def test_move_directory(directory_full: Directory) -> None:
    folder_path: str = 'fruits/apples/fuji fruits'
    directory_full.move(folder_path=folder_path)

    assert directory_full.root == {'fruits': {'apples': {}, 'fuji': {}}}


def test_delete_directory(directory_full: Directory) -> None:
    folder_name: str = 'fruits/apples/fuji'
    directory_full.delete(folder_name=folder_name)

    assert directory_full.root == {'fruits': {'apples': {}}}


def test_delete_directory_fail(directory_full: Directory, capsys) -> None:
    folder_name: str = 'fuji'
    directory_full.delete(folder_name=folder_name)

    captured = capsys.readouterr()
    assert captured.out == 'Cannot delete fuji - fuji does not exist\n'
    assert directory_full.root == {'fruits': {'apples': {'fuji': {}}}}

    folder_name: str = 'apples/fuji'
    directory_full.delete(folder_name=folder_name)
    captured = capsys.readouterr()
    assert captured.out == 'Cannot delete apples/fuji - apples does not exist\n'
    assert directory_full.root == {'fruits': {'apples': {'fuji': {}}}}


def test_get_list_of_directories(directory_full: Directory, capsys) -> None:
    directory_full.list()
    captured = capsys.readouterr()

    assert captured.out == f'fruits\n  apples\n    fuji\n'
