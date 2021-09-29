from nectarifere.nectar import Nectar

@Nectar
def do(a):
    if a != 5:
        raise ValueError

do(4)
do(5)