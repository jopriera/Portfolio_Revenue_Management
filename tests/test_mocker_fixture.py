def test_mocker_fixture(mocker):
    mock = mocker.patch('builtins.print')
    print('hola')
    mock.assert_called_once_with('hola')
