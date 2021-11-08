from nectarifere.falzar import falzar

@falzar
def do(a):
    if a != 5:
        raise ValueError

do(5)
do(4)