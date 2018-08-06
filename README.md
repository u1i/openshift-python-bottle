# openshift-python-bottle

Sample App for running Python/Bottle on OpenShift

## How to deploy

`oc new-app https://github.com/u1i/openshift-python-bottle.git`

`oc expose svc/openshift-python-bottle`

## Access the App

Navigate to the overview in the OpenShift GUI - the URL should appear right next to the app. In Minishift you can also do this on the command line:

`minishift openshift service openshift-python-bottle --in-browser`

## Trigger a Build

Get the 'Generic Webhook URL' from Builds >> openshift-python-bottle >> Configuration

`curl -k -X POST <WEBHOOK_URL>`

## Auto-Scale App

Minimum 3 instances, maximum 10:

`oc autoscale dc/openshift-python-bottle --min 3 --max 10`

`oc get dc/openshift-python-bottle`

`oc describe dc/openshift-python-bottle`


## Delete App

`oc delete all -l app=old-app1`