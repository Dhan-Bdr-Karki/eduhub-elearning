from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# field to define an order for the objects
class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)


    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                print(f'Model-instance: {model_instance} Attribute-name: {self.attname}')
                # retreiving all objects of field's model
                qs = self.model.objects.all()
                print(f'  queryset -> {qs}')
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    print(query)
                    # filter by objects with the same field values
                    qs = qs.filter(**query)
                    print(qs)
                # get the order of the last item
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
                print(f'Value -> {value}' )
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
