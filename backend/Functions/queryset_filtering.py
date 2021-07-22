from django.db.models import Q
from icecream import ic


def queryset_filtering(model, queries):
    from django.db.models import F

    ordering = queries.get("ordering")
    #TODO
    # AllDataStr.objects.annotate(search=SearchVector('name', 'codename')).filter(search='add event')
    filters = Q()
    all_fields = [x.name for x in model._meta.get_fields()]
    model = model.objects.all()

    queries_fields = []
    for field in queries.keys():
        if "F('" in queries[field]:
            queries[field] = eval(queries[field])
        #TODO
        # if regex in field and  "r('" in queries[field]:
        #     queries[field] = eval(queries[field])

        for x in all_fields:
            if x in field:
                queries_fields.append(field)

    for key in queries_fields:
        q = Q(**{"%s" % key: queries.get(key)})
        filters &= q
    Model = model.filter(Q(filters))
    latest = queries.get('latest')
    earliest = queries.get('earliest')
    if latest:
        Model = [Model.latest()]
    if earliest:
        Model = [Model.earliest()]

    if ordering:
        Model = Model.order_by(ordering)
    return Model
