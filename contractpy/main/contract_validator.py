from contractpy.main.exceptions.invalid_format import InvalidFormat
from contractpy.main.exceptions.invalid_value import InvalidValue
from contractpy.main.types import Types


class ContractValidator:
    @staticmethod
    def _validate_format(contract):
        valid_formats = (dict, list)
        if not isinstance(contract, valid_formats):
            raise InvalidFormat(
                f"Invalid contract format. Valid formats are {','.join(map(lambda x: x.__name__, valid_formats)) }."
            )

    @staticmethod
    def _validate_contract_recursively(contract):
        if isinstance(contract, list):
            if len(contract) != 1:
                raise InvalidValue("More than one value cannot be passed to list")
            ContractValidator._validate_contract_recursively(contract[0])
        elif isinstance(contract, dict):
            for key, value in contract.items():
                if isinstance(value, (dict, list)):
                    ContractValidator._validate_contract_recursively(value)
                elif value not in [Types.FLOAT, Types.INTEGER, Types.STRING]:
                    raise InvalidValue(
                        f"Invalid value for the field {key}. Valid values are {', '.join(i for i in dir(Types) if not i.startswith('__'))}."
                    )
        elif contract not in [Types.FLOAT, Types.INTEGER, Types.STRING]:
            raise InvalidValue(
                f"Invalid values for the list. Valid values are {', '.join(i for i in dir(Types) if not i.startswith('__'))}"
            )

    @staticmethod
    def validate(contract):
        ContractValidator._validate_format(contract)
        ContractValidator._validate_contract_recursively(contract)
