class ContractVerifier:
    @staticmethod
    def verify(contract, data):
        if isinstance(contract, type):
            if isinstance(data, contract):
                return True

        if not isinstance(data, type(contract)):
            return False

        if isinstance(contract, list):
            contract_type = contract[0]

            if not all([ContractVerifier.verify(contract_type, value) for value in data]):
                return False

        elif isinstance(contract, dict):
            for key in contract.keys():
                if not ContractVerifier.verify(contract[key], data.get(key)):
                    return False

        return True