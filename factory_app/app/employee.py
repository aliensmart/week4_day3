from .orm import ORM

class Worker(ORM):
    #attribute:
    #   name
    #   job
    #   years
    #   department is None
    tablename = "employees"
    fields = ["name", "job", "years", "department","factory_pk"]
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.name = kwargs.get("name")
        self.job = kwargs.get("job")
        self.years = kwargs.get("years")
        self.factory_pk = kwargs.get("factory_pk")
        self.department = None
    
    #Create methods set_department and increase_tenure
    
    def set_department(self,depart):

        """
            will take in a string, 
            and re-assign the worker's 
            department for the day

        """
        self.department = depart

    def increase_tenure(self):
        """

            will add one year to the number 
            of years this worker has been 
            at the factory.

        """
        self.years +=1
    