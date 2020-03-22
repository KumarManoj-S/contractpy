# contractpy

contractpy is a tiny library for validating our data against a contract.

# Basic usage

You could simply create a contract object and you could validate your data against the contract.
~~~~{.python}
from pycontract import Contract, Types

my_contract = {
    'name': Types.STRING,
    'id': Types:INTEGER
}
contract = Contract(my_contract)

assert contract.verify({'name': 'Captain America': 'id': 12345}) is True
~~~~
Yes it is as simple as this.

It works for complicated data as well. Like a json that contains a list of strings or list of dictionaries. It will recursively iterate over the inner dicts and check it against the contract. Please check out the other examples,

## Other examples

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

You could also do the contract testing for the APIs using this library.
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
