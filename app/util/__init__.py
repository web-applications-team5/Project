import datetime
import time


def kt2dict(keyed_tuple):
    """ sqlalchemy.util._collections.KeyedTuple to dict """
    return dict(zip(keyed_tuple.keys(), keyed_tuple))

def sqla2dict(model):
    """ Declarative Base model to dict """
    result = {}

    for c in model.__table__.columns:
        val = getattr(model, c.name)
        if isinstance(val, datetime.time):
            result[c.name] = val.strftime('%I:%M:%S %p')
        else:
            result[c.name] = val

    return result
    # return {c.name: getattr(model, c.name) for c in model.__table__.columns}