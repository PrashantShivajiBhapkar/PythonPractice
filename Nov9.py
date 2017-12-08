def getFuncInfo(object, spacing=20, collapse=1):
    methodlist = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" % (method.ljust(spacing), processFunc(
        str(getattr(object, method).__doc__))) for method in methodlist]))


if __name__ == "__main__":
    l = []
    print(getFuncInfo(l))
