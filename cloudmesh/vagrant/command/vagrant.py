from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class VagrantCommand(PluginCommand):

    @command
    def do_vagrant(self, args, arguments):
        """
        ::

          Usage:
                vagrant -f FILE
                vagrant FILE
                vagrant list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



