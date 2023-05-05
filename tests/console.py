#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        return True
        
    def emptyline(self):
        pass

    def base_error_handler(self, line, cb):
        line_args = shlex.split(line)
        if not line:
            print("** class name missing **")
        elif line_args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            cb(line_args)
    
    def do_create(self, line):
        def cb(line_args):
            bm = BaseModel()
            bm.save()
            print(bm.id)
        self.base_error_handler(line, cb)
    
    def do_show(self, line):
        def cb(line_args):
            args_len = len(line_args)

            if args_len == 1:
                print("** instance id missing **")
            else:
                model_name, id = line_args
                class_id =  f"{model_name}.{id}"
                print(storage.all().get(class_id, "** no instance found **"))   
            
        self.base_error_handler(line, cb)

    def do_destroy(self, line):
        def cb(line_args):
            args_len = len(line_args)

            if args_len == 1:
                print("** instance id missing **")
            else:
                model_name, id = line_args
                class_id =  f"{model_name}.{id}"
                try:
                    storage.all().pop(class_id)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
        self.base_error_handler(line, cb)
    
    def do_all(self, line):
        objects = storage.all()
        if not line:
            print({key: str(ins) for key, ins in objects.items()})
        else:
           all_class_ins = {key: str(ins) for key, ins in objects.items()\
                             if line in self.classes}
           print(all_class_ins if len(all_class_ins)\
                 else "** class doesn't exist **")
    def computed_complete_list(self, text):
        if not text:
            classes = self.classes[:]
        else:
            classes = [x for x in self.classes if x.startswith(text)]
        return classes

    def complete_create(self, text, line, begidx, endidx):
        return self.computed_complete_list(text)
    
    def complete_show(self, text, line, begidx, endidx):
        return self.computed_complete_list(text)

    def complete_destroy(self, text, line, begidx, endidx):
        return self.computed_complete_list(text)
    
    def complete_all(self, text, line, begidx, endidx):
        return self.computed_complete_list(text)

if __name__  == "__main__":
    HBNBCommand().cmdloop()

