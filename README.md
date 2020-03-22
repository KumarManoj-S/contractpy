# contractpy

contractpy is a tiny library for validating our data if it conforms to the contract that's specified.

# Basic usage

You could simply create a contract object and you could validate your data against the contract.
```
from pycontract import contract, Types

my_contract = {
    'name': Types.STRING,
    'id': Types:INTEGER
}
contract = Contract(my_contract)

assert contract.verify({'name': 'Captain America': 'id': 12345}) is True
```
Yes it is as simple as this.

It works for complicated data as well. Like a json that contains a list of strings or list of dictionaries. Please check out the other examples,

## Other examples

```
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
```