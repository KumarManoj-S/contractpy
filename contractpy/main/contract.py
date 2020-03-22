from contractpy.main.contract_validator import ContractValidator
from contractpy.main.contract_verifier import ContractVerifier


class Contract:
    def __init__(self, contract):
        ContractValidator.validate(contract)
        self.contract = contract

    def verify(self, data):
        """
        This method is to verify the data against the contract.

        :param data: dict or List of dict
        :return: bool
        """
        return ContractVerifier.verify(self.contract, data)


