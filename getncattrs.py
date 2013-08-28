#
# acrosby 2013
#

def __init__():
    pass

def __call__(nc):
    s = {}
    for attr in nc.ncattrs():
        s[attr] = nc.getncattr(attr)
    return s
