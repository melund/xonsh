"""Tests the xonsh lexer."""
from __future__ import unicode_literals, print_function
import os
from contextlib import ContextDecorator, contextmanager
import tempfile



from nose.tools import assert_equal, assert_true, assert_false
from xonsh.completer import Completer
from xonsh import built_ins

built_ins.load_builtins()

from xonsh.tools import ON_WINDOWS



@contextmanager
def setup_test_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()        
        os.chdir(tmpdir)
        os.makedirs('Folder WITH Spaces/subfolder1')
        os.makedirs('Folder WITH Spaces/subfolder2')
        yield tmpdir
        os.chdir(cwd)


if ON_WINDOWS:
    
    def test_complete1():
        with setup_test_dir():
            cmpl = Completer()
            args = ('folder', "cd folder",3,8)
            cmpl_list = cmpl.complete(*args)
            assert_equal(cmpl_list[0], "'Folder WITH Spaces\\'")
    
    def test_complete2():
        with setup_test_dir():
            cmpl = Completer()
            args = ("wit", "cd 'folder wit",11,13)
            cmpl_list = cmpl.complete(*args)
            assert_equal(cmpl_list[0], "'Folder WITH Spaces\\'")
            
            args = ('"fold', 'cd "fold',3,7)
            cmpl_list = cmpl.complete(*args)
            assert_equal(cmpl_list[0], "'Folder WITH Spaces\\'")
            
            args = ('s', 'cd "folder with s',16,17)
            cmpl_list = cmpl.complete(*args)
            assert_equal(cmpl_list[0], "'Folder WITH Spaces\\'")

            args = ('s', 'cd "./folder with s',16,17)
            cmpl_list = cmpl.complete(*args)
            assert_equal(cmpl_list[0], "'Folder WITH Spaces\\'")

        # make something that completes part of a filename/cmd/etc. if the suggested
        # autocompletions have a some prefix in common. 




if __name__ == '__main__':
    
    
    
    test_complete1()
    test_complete2()
