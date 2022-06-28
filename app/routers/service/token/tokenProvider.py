path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
def get_token():
    with open(path) as f:
        return "Bearer " + f.read()
