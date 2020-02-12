from app.main.exceptions.invalid_format import InvalidFormat
from app.main.exceptions.invalid_value import InvalidValue


class Types:
    STRING = 'STRING'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'


class Contract(object):
    def __init__(self, contract):
        self.__contract = contract



class Contract:
    @staticmethod
    def _validate_format(contract):
        valid_formats = [dict, list]
        if type(contract) not in valid_formats:
            raise InvalidFormat(
                f"""Invalid contract format. Valid formats are 
                    { ",".join(map(lambda x: x.__name__, valid_formats)) }.
                """
            )

    @staticmethod
    def _validate_contract(contract):
        Contract._validate_format(contract)
        if type(contract) == list:
            for obj in contract:
                Contract._validate_contract(obj)
        if type(contract) == dict:
            for key, value in contract.items():
                if type(value) in [dict, list]:
                    Contract._validate_contract(value)
                else:
                    if value not in [Types.FLOAT, Types.INTEGER, Types.STRING]:
                        raise InvalidValue(
                            f"""Invalid value for the field {key}. Valid values are 
                                {', '.join(i for i in dir(Types) if not i.startswith('__'))}
                            """
                        )

    def init(self, contract):
        pass