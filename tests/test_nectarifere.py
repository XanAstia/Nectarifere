from nectarifere.nectar import nectar

@nectar
def do(a):
    if a != 5:
        raise ValueError

do(5)
do(4)