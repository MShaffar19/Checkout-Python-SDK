from authorize_order import *
from capture_order import *
from create_order import *

response = CreateOrder().create_order()
order_id = ''
print 'Creating Order...'
if response.status_code == 201:
    order_id = response.result.id
    for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(str(link.rel).capitalize(), link.href, link.method))
    print 'Created Successfully\n'
    print 'Copy approve link and paste it in browser. Login with buyer account and follow the instructions.\nOnce approved hit enter...'
else:
    print 'Link is unreachable'
    exit(1)

raw_input()
print 'Authorizing Order...'
response = AuthorizeOrder().authorize_order(order_id)
authorization_id = ''
if response.status_code == 201:
    authorization_id = response.result.purchase_units[0].payments.authorizations[0].id
else:
    print("Link is unreachable")
    exit(1)
print 'Authorized Successfully\n'

print 'Capturing Order...'
response = CaptureOrder().capture_order(authorization_id)
if response.status_code == 201:
    print 'Captured Successfully\n'
    print 'Status Code: ', response.status_code
    print 'Status: ', response.result.status
    print 'Order ID: ', response.result.id
    print 'Links: '
    for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))




