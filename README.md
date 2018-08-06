# openshift-python-bottle

Sample App for running Python/Bottle on OpenShift

## How to deploy

`oc new-app https://github.com/u1i/openshift-python-bottle.git`

`oc expose svc/openshift-python-bottle`

## Access in minishift

`minishift openshift service openshift-python-bottle --in-browser`

