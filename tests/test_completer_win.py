"""Tests the xonsh lexer."""
from __future__ import unicode_literals, print_function
import os
from contextlib 
import tempfile



import nose
from nose.tools import assert_equal, assert_true, assert_false
from xonsh.completer import Completer
from xonsh import built_ins

built_ins.load_builtins()

from xonsh.tools import ON_WINDOWS

@contextlib.contextmanager
def setup_folder():
   with  tempfile.TemporaryDirectory() as tmpdir:
       os.chdir(tmpdir)
       os.makedirs('folder with space/subfolder1')
       os.makedirs('folder with space/subfolder2')
       os.makedirs('folder with space2/subfolder')
       yield tmpdir


if ON_WINDOWS:
    
    @setup_folder
    def test_complete1():
        cmpl = Completer()
        args = ('folder', "cd folder",3,8)
        cmpl_list = cmpl.complete(*args)
        assert_equal(cmpl_list[0], "'folder with space\\'")
    
    def test_complete2():
        cmpl = Completer()
        args = ("'wit", "cd 'folder wit",11,13)
        cmpl_list = cmpl.complete(*cmplwrap(*args))
        assert_equal(cmpl_list[0], "'folder with space\\'")
        
        args = ('"fold', 'cd "fold',3,7)
        cmpl_list = cmpl.complete(*cmplwrap(*args))
        assert_equal(cmpl_list[0], "'folder with space\\'")
        
        args = ('s', 'cd "folder with s',16,17)
        cmpl_list = cmpl.complete(*cmplwrap(*args))
        assert_equal(cmpl_list[0], "'folder with space\\'")

        # make something that completes part of a filename/cmd/etc. if the suggested
        # autocompletions have a some prefix in common. 


def cmplwrap( prefix, line, begidx, endidx):
    quote_idxs = map(line[0:begidx].rfind, ('"',"'"))
    if quote_idxs:
        begidx = max(quote_idxs)
    prefix = line[begidx:endidx+1]
    return (prefix, line, begidx, endidx)
    

if __name__ == '__main__':
    
    nose.runmodule()
