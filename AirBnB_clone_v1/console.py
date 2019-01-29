#!/usr/bin/python3
"""
Entry point to command interpreter
"""
import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    """Console Interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Receives End Of File signal and exits out of program"""
        print()
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, args):
        """Create a new instance of a class"""
        args = "".join(args).split()
        #check that there isn't more than one arg
        if len(args) == 1:
            error = models.error_check(args, 1)
            if error != 0:
                model = eval("models.{}".format(args[0]))()
                model.save()
                print(model.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Print the instance's class name and ID"""
        args = "".join(args).split()
        key = models.error_check(args)
        if key == 0:
            return
        try:
            obj_dict = models.storage.all()
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an existing instance"""
        args = "".join(args).split()
        key = models.error_check(args)
        if key == 0:
            return
        try:
            obj_dict = models.storage.all()
            del obj_dict[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Print instances: can print class-specific"""
        args = "".join(args).split()
        obj_dict = models.storage.all()
        #all w/o class name
        if len(args) == 0:
            for obj_id in obj_dict.keys():
                obj = obj_dict[obj_id]
                print(obj)
        #all w/class name
        else:
            if models.error_check(args, 1) == 0:
                    return
            else:
                for k, v in obj_dict.items():
                    if v.to_dict()['__class__'] == args[0]:
                        obj = obj_dict[k]
                        print(obj)

    def do_update(self, args):
        """
        update exisiting instances
        Ex: update BaseModel 123 email "aibnb@holbertonschool.com"
        """
        args = "".join(args).split()
        key = models.error_check(args)
        if key == 0:
            return
        try:
        #check ID is valid
            obj_dict = models.storage.all()
            value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
        #check attribute is inputed
            print("** attribute name missing **")
            return
        if len(args) == 3:
        #check attribute value is inputed
            print("** value missing **")
            return
        #check attribute is valid
        new_args3 = args[3].replace('"', '')
        if hasattr(value, args[2]):
            item = getattr(value, args[2])
            convert = type(item)
            new_args3 = convert(new_args3)
        setattr(value, args[2], new_args3)
        value.save()

    def do_count(self, arg):
        """Prints number of instance"""
        arg = arg.split()
        obj = models.storage.all()
        counter = 0
        for key, value in obj.items():
            compare = key.split(".")
            if arg[0] == compare[0]:
                counter += 1
        print(counter)

    def parse(self, classname, arg):
        new_arg = arg.split('{')
        baseid = new_arg[0][0:-2]
        new_dict = "{"
        delim = ["'"]
        for c in new_arg[1]:
            new_dict += c
        obj_dict = json.loads(new_dict)
        for k, v in obj_dict.items():
            string = "{} {} {} {}".format(classname, baseid, k, v)
            self.do_update(string)

    def default(self, line):
        """
        Execute command using:
        classname.cmd()
        Ex:
        User.all()
        User.destroy(<id>)
        """
        function = {'all': self.do_all,
                    'create': self.do_create,
                    'update': self.do_update,
                    'destroy': self.do_destroy,
                    'show': self.do_show,
                    'count': self.do_count}
        delim = ['(', ')']
        delim2 = [',', '"']
        text = ""
        for c in line:
            if c in delim:
                text += '.'
            else:
                text += c
        arg = text.split('.')
        if arg[1] == 'update':
            if '{' in arg[2]:
                self.parse(arg[0], arg[2])
                return
        delim3 = ['(', ')', '.']
        b = ""
        for c in line:
            if c in delim3:
                b += '.'
            elif c in delim2:
                b += ""
            else:
                b += c
        arg = b.split('.')
        string = "{}".format(arg[0])
        if arg[2] != "":
            string = "{} {}".format(arg[0], arg[2])
        func = function[arg[1]]
        func(string)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
