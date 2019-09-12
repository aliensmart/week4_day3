#!/usr/bin/env python3
from .orm import ORM
from .employee import Worker
from .item import Item

class Factory(ORM):
    #attribut:
    #   workers is the list of worker obj
    #   products is the list of items
    #   days_since_last_incident

    tablename = "factories_compo"
    fields = ["name", "days_since_last_incident"]
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.name = kwargs.get("name")
        self.days_since_last_incident = 0

    #method need:
    #   add_worker
    #   create_product
    #   ship
    #   add_day
    #   incident



    def ship(self):
        """
            should remove everything from our current 

        """
        self.products = []
    
    def get_workers(self):
        workers =  Worker.all_from_where_clause("WHERE factory_pk=?", (self.pk,))
        print("{}: ".format(self.name))
        for worker in workers:
            print("name => {}, Job => {}".format(worker.name, worker.job))

    def get_products(self):
        products = Item.all_from_where_clause("WHERE factory_pk=?", (self.pk,))
        print("{}: ".format(self.name))
        for product in products:
            print("name => {}, price => ${}".format(product.name, product.cost))


    
    def add_day(self):
        """
        should add 1 to our 
        self.days_without_incident attribute

        """
        self.days_since_last_incident +=1

    def incident(self):
        """
        re-assign self.days_without_incident to 0
        """
        self.days_since_last_incident = 0













    
