from unittest.mock import patch

from app.main.contract import Contract


@patch('app.main.contract.ContractValidator')
def test_contract_init(mock_contract_validator):
    mock_contract_validator.validate.return_value = None

    contract = Contract("my-contract")

    assert contract.contract == "my-contract"
    mock_contract_validator.validate.assert_called_once_with("my-contract")


@patch('app.main.contract.ContractValidator')
@patch('app.main.contract.ContractVerifier')
def test_contract_verify(mock_contract_verifier, mock_contract_validator):
    mock_contract_validator.validate.return_value = None
    mock_contract_verifier.verify.return_value = True

    contract = Contract("my-contract")
    contract.verify("data")

    assert contract.contract == "my-contract"
    mock_contract_validator.validate.assert_called_once_with("my-contract")
    mock_contract_verifier.verify.assert_called_once_with("my-contract", "data")
