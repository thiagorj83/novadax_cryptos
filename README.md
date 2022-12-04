# Getting all supported trading symbols from Novadax API

There are three files:
get_symbols.py, check_connection.py and main.py

In file get_symbols.py, the url "https://api.novadax.com/v1/common/symbols" receives a get request and
return all supported trading symbols from Novadax exchange API.

The second file called check_connection.py checks if the internet connection is available in order to make the get request.
If so, request is commited. If not, the function waits five seconds to check the internet availability again and so on until
connection is restored.

Finally, in main.py, there is a function with the same name called main(), where the two previous classes are instantiated.
There is a while loop that verifies if there is internet connection available. If so, it displays on screen the supported
symbols. If not, it veryfies if the connection is restored after each five seconds in order to make the api request.
