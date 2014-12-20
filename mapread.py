def mapread(game, filename):
    map = open(filename, "r")

    tmpstr = map.read()
    tmparray = tmpstr.splitlines()

    return tmparray