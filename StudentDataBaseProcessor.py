import json
import Student

class DataBaseProcessor():
    def __init__(self):
        self.listOfStudent = []


    def AppendStudent(self, student):
        self.listOfStudent.append(student)

    def SerializeDataBase(self):
        with open("data_file.json", "a") as write_to_json_file:
            write_to_json_file.write(json.dumps(self.listOfStudent, default=convert_to_dict, indent=4, sort_keys=True))
            #for i in self.listOfStudent:
                #write_to_json_file.write(json.dumps(i, default=convert_to_dict, indent=4, sort_keys=True))


    def DeserializeDataBase(self):
        with open("data_file.json", "r") as read_from_json_file:
            listofstudents=json.loads(read_from_json_file.read(), object_hook=dict_to_obj)
            print(listofstudents)
            print(type(listofstudents))
            return listofstudents

def convert_to_dict(obj):
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)

    return obj_dict


def dict_to_obj(our_dict):
    """
    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")

        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")

        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)

        # Get the class from the module
        class_ = getattr(module, class_name)

        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj
