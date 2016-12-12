# Signavio Workflow CRM connector example

This is an example of a [custom data connector](http://docs.workflow.signavio.com/en/latest/integration/connectors.html) for Signavio Workflow.
This connector serves a small fixed list of customers.

The Python program uses [Flask](http://flask.pocoo.org) to serve the connector endpoints.
This uses the type descriptor and customer data in the files `descriptor.json` and `data.json`, respectively.
