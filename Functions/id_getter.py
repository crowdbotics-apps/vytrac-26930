from icecream import ic

from Functions.typost_check import typos_check


def id_getter(Model,value,query):
    from django.db.models import Q
    try:
        obj = Model.objects.get(Q(**{query: value}))
        return {"success":True,"data": obj.id}
    except:
        machtes = typos_check(Model, value,  query)
        return {"success":False,"data":f'"{value}" is not found, did you mean {machtes}'}


def ids_getter(Model,values,query):
    from django.db.models import Q

    values_ids = []
    for value in values:
        try:
            obj = Model.objects.get(Q(**{query: value}))
            values_ids.append(obj.id)
        except:
            machtes = typos_check(Model, value,  query)
            return {"success":False,"data":f'"{value}" is not found, did you mean {machtes}'}

    return {"success":True,"data": values_ids}
