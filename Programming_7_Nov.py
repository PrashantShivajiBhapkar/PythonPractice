

def printfunc(par):
    """ Build a Connection String"""
    return "-".join(["%s %s" % (a, b) for a, b in par.items()])


if __name__ == "__main__":
    param = {"server": "asd", "database": "SQL"}
    print(printfunc(param))
    import odbchelper
    print(odbchelper.buildConnectionString.__doc__)
