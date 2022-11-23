A CoAP server is generally a service running on a constrained device hosting/managing one or more resources (e.g. light switches, alarms, sensors). Each resource will be provided with a unique CoAP address endpoint and a defined API so that CoAP clients could interact with that resource.

In this particular example our server has a single resource which an Alarm State.
Here our client_put.py program is trying to update the state of alarm on the server randomly.

To create COAP server and client, we are using Python 3 and Aiocoap Library