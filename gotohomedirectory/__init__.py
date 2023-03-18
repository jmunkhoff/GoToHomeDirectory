# Copyright (C) 2023 John Munkhoff
# SPDX-License-Identifier: MIT

from fman import ApplicationCommand, DirectoryPaneCommand
from fman.url import as_url
import os

__all__ = [ 'GoToHomeDirectory', 'GoToHomeDirectoryInAllPanes' ]


# This command navigates to the user's home directory in the current
# pane (or more precisely, the pane in which the command is run).
class GoToHomeDirectory(DirectoryPaneCommand):
    def __call__(self):
        home_dir = _get_home_dir()
        _goto_dir(self.pane, home_dir)


# This command navigates to the user's home directory in all panes.  In
# fman's current implementation, that should be only the left and right
# panes.  But theoretically, this code should support any number of panes,
# hence the name "all panes".
class GoToHomeDirectoryInAllPanes(ApplicationCommand):
    def __call__(self):
        home_dir = _get_home_dir()
        for pane in self.window.get_panes():
            _goto_dir(pane, home_dir)


# Navigate to the specified directory (URL) in the given pane.
# For this plugin, the URL is the user's home directory.
# Run the open_directory command because it handles errors gracefully.
def _goto_dir(pane, url):
    pane.run_command('open_directory', {'url': url})


# Returns, as a URL, the path of the user's home directory.
def _get_home_dir():
    home_path = os.path.expanduser('~')
    home_url = as_url(home_path)
    return home_url


