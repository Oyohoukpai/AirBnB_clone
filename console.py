#!/usr/bin/python3
''' console module '''
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry points '''

    prompt = '(hbnb) '
    myclasses = ["BaseModel", "User", "Place", "State", "Amenity", "Review",
                 "City"]

    def do_EOF(self, line):
        ''' exit the program '''
        return True

    def help_EOF(self):
        ''' help EOF'''
        print("EOF command to exit the program\n")

    def help_quit(self):
        ''' help quit '''
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        ''' quit interpreter '''
        return True

    def emptyline(self):
        ''' do nothing with empty lines '''
        pass

    def do_create(self, classname):
        ''' create a new instance of '''
        if len(classname) == 0:
            print('** class name missing **')
        elif classname not in self.myclasses:
                print('** class doesn\'t exist **')
                return False
        else:
            new = eval("{}()".format(classname))
            new.save()
            print(new.id)

    def help_create(self):
        ''' help create '''
        print("Create command to create a class\n")

    def do_show(self, line):
        '''represents an instance'''
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False

        if len(args) < 2:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        for i in all_objs.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(all_objs[i])
                return False
        print('** no instance found **')

    def help_show(self):
        ''' help show '''
        print("Show command to display the string representation of class\n")

    def do_destroy(self, line):
        ''' deletes an instance based on the class id'''
        args = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        elif len(args) < 2:
            print('** instance id missing **')
            return False
        else:
            all_objs = storage.all()
            for i in all_objs:
                if i == "{}.{}".format(args[0], args[1]):
                    all_objs.pop(i)
                    storage.save()
                    return False
            print('** no instance found **')

    def help_destroy(self):
        ''' help destroy '''
        print("Destroy command to destroy an object\n")

    def do_all(self, line):
        ''' prints all string representations of instances'''
        args = line.split()
        all_objs = storage.all()

        if len(args) == 0:
            for i in all_objs:
                strarg = str(all_objs[i])
                print(strarg)
        elif line not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        else:
            for i in all_objs:
                if i.startswith(args[0]):
                    strarg = str(all_objs[i])
                    print(strarg)
        return False

    def help_all(self):
        ''' help all'''
        print("All command to show all instances\n")

    def do_update(self, line):
        ''' updates an instance based on class name and id'''
        args = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            clsname = line.split()[0]
            eval("{}()".format(clsname))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            instanceid = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except IndexError:
            print('** no instance found **')
            return False

        try:
            attributename = line.split()[2]
        except IndexError:
            print('** attribute name missing **')
            return False

        try:
            updatevalue = line.split()[3]
        except IndexError:
            print('** value missing **')
            return False

        if updatevalue.isdecimal() is True:
            setattr(clschange, attributename, int(updatevalue))
            storage.save()
        else:
            try:
                setattr(clschange, attributename, float(updatevalue))
                storage.save()
            except:
                setattr(clschange, attributename, str(updatevalue))
                storage.save()

    def help_update(self):
        '''help update'''
        print("update command to update attributes\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()



    #!/usr/bin/python3
import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)


class TestHBNBCommandPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestHBNBCommand(unittest.TestCase):
    """ tests for class HBNBCommand """
    pass





#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
import re
import json


class HBNBCommand(cmd.Cmd):
    """Command line program"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles Exiting the program by pressing Ctrl-D.
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id"""
        if line == '' or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class name missing **")
        else:
            dict = storage.classes()
            inst = dict[line]()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        if line == '' or line is None:
            print('** class name missing **')
            return
        cmd = line.split(' ')
        if cmd[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print('** instance id missing **')
        else:
            key = f'{cmd[0]}.{cmd[1]}'
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line == "":
            obj_list = [str(obj) for obj in storage.all().values()]
            print(obj_list)
        else:
            cmd = line.split(' ')
            if cmd[0] not in storage.classes():
                print('** class doesn\'t exist **')
                return
            obj_list = [str(obj) for obj in storage.all().values()
                        if type(obj).__name__ == cmd[0]]
            print(obj_list)

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        print(words)
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
