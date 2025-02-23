# Crie o __init__ para interpretar como pacote a pasta atual
# Criando testes unitários
# Biblioteca padrão unittest para testes
from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest
from pytest_mock import mocker

from src.utils import requires_role, square_number


# Teste para casos de sucesso da função
# Testes parametrizados para atribuir mais valores em tempo de execução
@pytest.mark.parametrize('test_input,expected', [(2, 4), (10, 100), (3, 9)])
def test_square_number_success(test_input, expected):
    result = square_number(test_input)
    # Assert retorna um erro se um boolean false de uma comparação
    assert result == expected
    # Sem o AssertionError frameworks como PyTest não vão detectar a falha do teste


# Teste para casos de falha da função
@pytest.mark.parametrize(
    'test_input,exc_class,msg',
    [
        (
            'a',
            TypeError,
            "unsupported operand type(s) for ** or pow(): 'str' and 'int'",
        ),
        (
            None,
            TypeError,
            "unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'",
        ),
    ],
)
def test_square_number_fail(test_input, exc_class, msg):
    # Verifica se o teste retorna um erro determinado
    with pytest.raises(exc_class) as exc:
        square_number(test_input)
    assert str(exc.value) == msg


# Teste de métodos com dependências externas usando unittest
def test_requires_role_success():
    user_mock = Mock()
    # Um valor simulado para uma função
    user_mock.role.name = 'admin'

    # Criando mocks para simular objetos ou métodos
    mock_get_jwt_identity = patch('src.utils.get_jwt_identity')
    # Argumento return_value define o tipo de retorno de determinado mock
    mock_get_or_404 = patch('src.utils.db.get_or_404', return_value=user_mock)

    # Iniciando simulação
    mock_get_jwt_identity.start()
    mock_get_or_404.start()

    # Qualquer função passada para o decorator, apenas para verificar se é executado corretamente
    decorated_function = requires_role('admin')(lambda: 'success')

    result = decorated_function()
    assert result == 'success'

    # Terminando
    mock_get_jwt_identity.stop()
    mock_get_or_404.stop()


# Verificando casos de falha com unittest
def test_requires_role_fail_unit():
    user_mock = Mock()
    user_mock.role.name = 'user'

    # Usando bloco de contexto para omitir start e stop dos mocks
    with (
        patch('src.utils.get_jwt_identity'),
        patch('src.utils.db.get_or_404', return_value=user_mock),
    ):
        decorated_function = requires_role('admin')(lambda: 'success')
        result = decorated_function()
    assert result == ({'message': 'Access Unauthorized'}, HTTPStatus.FORBIDDEN)


# Verificando casos de falha com pytest-mock
def test_requires_role_fail(mocker):
    # Given
    user_mock = mocker.Mock()
    user_mock.role.name = 'user'

    mocker.patch('src.utils.get_jwt_identity')
    mocker.patch('src.utils.db.get_or_404', return_value=user_mock)
    decorated_function = requires_role('admin')(lambda: 'success')

    # When
    result = decorated_function()

    # Then
    assert result == ({'message': 'Access Unauthorized'}, HTTPStatus.FORBIDDEN)


# Execute os testes com pytest, pytest tests/units, pytest tests/units::test_requires_role_success
