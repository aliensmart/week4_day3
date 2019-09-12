from .orm import ORM

class Item(ORM):
    #Attributes:
        #name
        #explosive
        #weight
        #cost
    tablename = "items"
    fields = ["name", "explosive", "weight", "cost","factory_pk"]
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.name = kwargs.get("name")
        self.explosive = kwargs.get("explosive")
        self.weight = kwargs.get("weight")
        self.cost = kwargs.get("cost")
        self.factory_pk = kwargs.get("factory_pk")

    #create method explod
    def explode(self):
        """
            If explosive == True, our method
            will print Boom!
        """
        if self.explosive == True:
            return "Boom"
