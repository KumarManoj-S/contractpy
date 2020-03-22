from contractpy.main.contract_verifier import ContractVerifier
from contractpy.main.types import Types


def test_contract_verifier_for_single_value():
    assert ContractVerifier.verify(str, "manoj") is True
    assert ContractVerifier.verify(int, 10) is True
    assert ContractVerifier.verify(float, 2.0) is True
    assert ContractVerifier.verify(int, 10.3) is False
    assert ContractVerifier.verify(str, 10) is False


def test_contract_verifier_for_list_of_values():
    assert ContractVerifier.verify([Types.STRING], ["str1", "str2"]) is True
    assert ContractVerifier.verify([Types.INTEGER], [123, 45]) is True
    assert ContractVerifier.verify([Types.FLOAT], [4.0, 5.2]) is True
    assert ContractVerifier.verify([Types.STRING], ["str1", 1]) is False
    assert ContractVerifier.verify([Types.INTEGER], [1, 2.0]) is False


def test_contract_verifier_for_flat_dict():
    assert ContractVerifier.verify({
        'a': Types.INTEGER,
        'b': Types.FLOAT,
        'c': Types.STRING
    }, {
        'a': 5,
        'b': 3.4,
        'c': 'manoj'
    }) is True

    assert ContractVerifier.verify({
        'a': Types.INTEGER,
        'b': Types.FLOAT,
        'c': Types.STRING
    }, {
        'a': '5',
        'b': 3.4,
        'c': 'manoj'
    }) is False

    assert ContractVerifier.verify({
        'a': Types.INTEGER,
        'b': Types.FLOAT,
        'c': Types.STRING
    }, {
        'a': 5,
        'b': 3,
        'c': 'manoj'
    }) is False


def test_contract_verifier_for_flat_dict_contains_value_as_list_of_primitive_types():
    assert ContractVerifier.verify({
        'a': Types.INTEGER,
        'b': Types.FLOAT,
        'c': [Types.STRING]
    }, {
        'a': 5,
        'b': 3.0,
        'c': ['manoj', 'kumar']
    }) is True

    assert ContractVerifier.verify({
        'a': [Types.INTEGER],
        'b': Types.FLOAT,
        'c': Types.STRING
    }, {
        'a': [5],
        'b': 3.0,
        'c': 'abc'
    }) is True

    assert ContractVerifier.verify({
        'a': [Types.INTEGER],
        'b': Types.FLOAT,
        'c': Types.STRING
    }, {
        'a': [5],
        'b': [3.0],
        'c': 'abc'
    }) is False


def test_contract_verifier_for_nested_dict():
    assert ContractVerifier.verify({
        'a': [Types.INTEGER],
        'b': Types.FLOAT,
        'c': {
            'd': [Types.STRING],
            'e': Types.INTEGER,
            'a': {'f': [Types.FLOAT]}
        }
    }, {
        'a': [5],
        'b': 3.0,
        'c': {
            'd': ["def"],
            'e': 45,
            'a': {'f': [4.0]}
        }
    }) is True

    assert ContractVerifier.verify({
        'a': [Types.INTEGER],
        'b': Types.FLOAT,
        'c': {
            'd': [Types.STRING],
            'e': Types.INTEGER,
            'a': {'f': [Types.FLOAT]}
        }
    }, {
        'a': [5],
        'b': 3.0,
        'c': {
            'd': ["def"],
            'e': 45,
            'a': {'f': 4.0}
        }
    }) is False


def test_contract_verifier_for_dict_contains_list_dict():
    assert ContractVerifier.verify({
        'a': [{'b': Types.INTEGER, 'c': [Types.STRING]}]
    }, {
        'a': [
            {'b': 45, 'c': ['manoj']},
            {'b': 34, 'c': ['abc', 'cde'], 'e': 'er'}
        ]
    }) is True

    assert ContractVerifier.verify({
        'a': [{'b': Types.INTEGER, 'c': [Types.STRING]}]
    }, {
        'a': [
            {'b': 45, 'c': ['manoj']},
            {'b': 34, 'c': ['abc', 'cde'], 'e': 'er'},
            {'b': "manoj", 'c': ['a']}
        ]
    }) is False

    assert ContractVerifier.verify({
        'a': [{'b': Types.INTEGER, 'c': [Types.STRING]}]
    }, {
        'a': [
            {'b': 45, 'c': ['manoj']},
            {'b': 34, 'c': ['abc', 'cde'], 'e': 'er'},
            {'b': 34, 'c': ['a', 5]}
        ]
    }) is False


def test_contract_verifier_should_return_true_if_data_matches_the_contract():
    contract = {
        'abc': {
            'bcd': {
                'efg': [Types.STRING]
            },
            'erf': Types.INTEGER
        },
        'xyz': [{
            'qwerty': [Types.INTEGER]
        }]
    }

    data = {
        'abc': {
            'bcd': {
                'efg': ['I', 'Love', 'my', 'country']
            },
            'erf': 12345
        },
        'xyz': [
            {'qwerty': [1, 2, 3, 4, 5]}, {'qwerty': [10, 20, 30, 40, 50]}
        ]
    }

    assert ContractVerifier.verify(contract, data) is True


def test_contract_verifier_should_return_false_if_data_does_not_matches_the_contract():
    contract = {
        'abc': {
            'bcd': {
                'efg': [Types.STRING]
            },
            'erf': Types.INTEGER
        },
        'xyz': [{
            'qwerty': [Types.INTEGER]
        }]
    }

    data = {
        'abc': {
            'bcd': {
                'efg': ['I', 'Love', 'my', 'country']
            },
            'erf': 12345
        },
        'xyz': [
            {'qwerty': [1, 2, 3, 4, 5]}, {'qwerty': [10, 20, 30, 40, "string"]}
        ]
    }

    assert ContractVerifier.verify(contract, data) is False


def test_contract_verifier_should_return_false_if_data_does_not_contain_any_mandatory_field():
    contract = {
        'abc': {
            'bcd': {
                'efg': [Types.STRING]
            },
            'erf': Types.INTEGER
        },
        'xyz': [{
            'qwerty': [Types.INTEGER]
        }]
    }

    data = {
        'abc': {
            'bcd': {
                'efg': ['I', 'Love', 'my', 'country']
            }
        },
        'xyz': [
            {'qwerty': [1, 2, 3, 4, 5]}, {'qwerty': [10, 20, 30, 40, 50]}
        ]
    }

    assert ContractVerifier.verify(contract, data) is False