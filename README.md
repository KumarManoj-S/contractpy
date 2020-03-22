# contractpy

contractpy is a tiny library for validating the data against a contract.

# Basic usage

You could simply create a contract object and validate your data if it conforms to the contract.
~~~~{.python}
from pycontract import Contract, Types

my_contract = {
    'name': Types.STRING,
    'id': Types:INTEGER
}
contract = Contract(my_contract)

assert contract.verify({'name': 'Captain America': 'id': 12345}) is True
~~~~
Yes, it is as simple as this.

Also, it works for the complicated data like nested dict object (Values in a dict object can be another dict object or list of dict objects). In such case, it will recursively iterate over the inner dicts and validate them against the contract. Please check out the below example,

~~~~{.python}
my_contract = {
    'name': Types.STRING,
    'id': Types:INTEGER,
    'orders': [
        {
            'orderId': Types:INTEGER,
            'price': Types:FLOAT,
        }
    ],
    comments: [Types.String]
}

data = {
    'name': 'Hazel Grace',
    'id: 57331,
    'orders': [
        {
            'orderId': 1,
            'price': 420.45
        },
        {
            'orderId': 2,
            'price': 750.38
        }
    ],
    comments: ["I really liked the product!", "I am completely satisfied."]
}

assert Contract(my_contract).verify(data) is True
~~~~

In case, if you want to specify a list for any field, simple use the [ ] bracket as specified in the field `data`. In such case, it will validate all the values against the contract that are present in the list.

You could also do the contract testing for the REST APIs using this library.
For Example,

~~~~{.python}
def test_users_api_conforms_the_contract():
    user_api_contract = {
        'page': Types.INTEGER,
        'per_page': Types.INTEGER,
        'total': Types.INTEGER,
        'total_pages': Types.INTEGER,
        'data': [
            {
                'id': Types.INTEGER,
                'name': Types.STRING,
                'year': Types.INTEGER,
                'color': Types.STRING,
                'pantone_value': Types.STRING
            }
        ],
        'ad': {
            'company': Types.STRING,
            'url': Types.STRING,
            'text': Types.STRING
        }
    }

    response = requests.get('https://reqres.in/api/user?page=1')

    assert response.status_code == 200
    assert Contract(user_api_contract).verify(response.json()) is True
~~~~

Note: Here, the test api is powered by [reqres.in](https://reqres.in/)
