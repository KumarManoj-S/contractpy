from app.main.contract_validator import ContractValidator
import pytest
from unittest.mock import patch
from app.main.contract_validator import Types

from app.main.exceptions.invalid_format import InvalidFormat
from app.main.exceptions.invalid_value import InvalidValue


def test_validate_contract_returns_none_for_valid_formats():
    assert ContractValidator._validate_format({"a": "b"}) is None
    assert ContractValidator._validate_format([{"a": "b"}]) is None


def test_validate_contract_raise_exception_for_unexpected_format():
    with pytest.raises(InvalidFormat) as e:
        ContractValidator._validate_format(('a', 'b'))

    assert str(e.value) == "Invalid contract format. Valid formats are dict,list."


def test_validate_contract_returns_none_for_valid_contract():
    valid_contracts = [
        {
            "first": Types.STRING,
            "second": Types.INTEGER,
            "third": Types.FLOAT
        },
        [{
            "first": Types.STRING,
            "second": Types.INTEGER,
            "third": Types.FLOAT
        }],
        {
            "first": Types.STRING,
            "second": Types.INTEGER,
            "third": Types.FLOAT,
            "fourth": [{"fifth": Types.INTEGER}]
        },
        {
            "first": Types.STRING,
            "second": Types.INTEGER,
            "third": Types.FLOAT,
            "fourth": {
                "fifth": [{
                    "sixth": Types.INTEGER
                }]
            }
        },
        [Types.STRING],
        {
            "first": Types.STRING,
            "second": [{
                "third": Types.INTEGER
            }],
            "third": [Types.FLOAT]
        }
    ]

    for contract in valid_contracts:
        assert ContractValidator.validate(contract) is None


def test_validate_contract_raise_exception_for_unecpected_value():
    with pytest.raises(InvalidValue) as e:
        ContractValidator.validate({"first": 'Double'})

    assert str(e.value) == 'Invalid value for the field first. Valid values are FLOAT, INTEGER, STRING.'

    with pytest.raises(InvalidValue) as e:
        ContractValidator.validate({"first": 'Double'})

    assert str(e.value) == 'Invalid value for the field first. Valid values are FLOAT, INTEGER, STRING.'


@patch.object(ContractValidator, 'validate')
def test_contract_class(mock__validate_contract):
    mock__validate_contract.return_value = None

    contract = ContractValidator({'test': 'contract'})

    assert contract.contract == {'test': 'contract'}
    mock__validate_contract.assert_called_once_with({'test': 'contract'})

