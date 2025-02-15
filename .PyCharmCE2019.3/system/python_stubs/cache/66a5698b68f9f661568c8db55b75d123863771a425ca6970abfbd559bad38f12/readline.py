# encoding: utf-8
# module readline
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/readline.so
# by generator 1.147
""" Importing this module enables command line editing using GNU readline. """
# no imports

# Variables with simple values

_READLINE_RUNTIME_VERSION = 1538

_READLINE_VERSION = 1538

# functions

def add_history(string): # real signature unknown; restored from __doc__
    """
    add_history(string) -> None
    add a line to the history buffer
    """
    pass

def clear_history(): # real signature unknown; restored from __doc__
    """
    clear_history() -> None
    Clear the current readline history.
    """
    pass

def get_begidx(): # real signature unknown; restored from __doc__
    """
    get_begidx() -> int
    get the beginning index of the readline tab-completion scope
    """
    return 0

def get_completer(): # real signature unknown; restored from __doc__
    """
    get_completer() -> function
    
    Returns current completer function.
    """
    pass

def get_completer_delims(): # real signature unknown; restored from __doc__
    """
    get_completer_delims() -> string
    get the readline word delimiters for tab-completion
    """
    return ""

def get_completion_type(): # real signature unknown; restored from __doc__
    """
    get_completion_type() -> int
    Get the type of completion being attempted.
    """
    return 0

def get_current_history_length(): # real signature unknown; restored from __doc__
    """
    get_current_history_length() -> integer
    return the current (not the maximum) length of history.
    """
    return 0

def get_endidx(): # real signature unknown; restored from __doc__
    """
    get_endidx() -> int
    get the ending index of the readline tab-completion scope
    """
    return 0

def get_history_item(): # real signature unknown; restored from __doc__
    """
    get_history_item() -> string
    return the current contents of history item at index.
    """
    return ""

def get_history_length(): # real signature unknown; restored from __doc__
    """
    get_history_length() -> int
    return the maximum number of items that will be written to
    the history file.
    """
    return 0

def get_line_buffer(): # real signature unknown; restored from __doc__
    """
    get_line_buffer() -> string
    return the current contents of the line buffer.
    """
    return ""

def insert_text(string): # real signature unknown; restored from __doc__
    """
    insert_text(string) -> None
    Insert text into the command line.
    """
    pass

def parse_and_bind(string): # real signature unknown; restored from __doc__
    """
    parse_and_bind(string) -> None
    Parse and execute single line of a readline init file.
    """
    pass

def read_history_file(filename=None): # real signature unknown; restored from __doc__
    """
    read_history_file([filename]) -> None
    Load a readline history file.
    The default filename is ~/.history.
    """
    pass

def read_init_file(filename=None): # real signature unknown; restored from __doc__
    """
    read_init_file([filename]) -> None
    Parse a readline initialization file.
    The default filename is the last filename used.
    """
    pass

def redisplay(): # real signature unknown; restored from __doc__
    """
    redisplay() -> None
    Change what's displayed on the screen to reflect the current
    contents of the line buffer.
    """
    pass

def remove_history_item(pos): # real signature unknown; restored from __doc__
    """
    remove_history_item(pos) -> None
    remove history item given by its position
    """
    pass

def replace_history_item(pos, line): # real signature unknown; restored from __doc__
    """
    replace_history_item(pos, line) -> None
    replaces history item given by its position with contents of line
    """
    pass

def set_completer(function=None): # real signature unknown; restored from __doc__
    """
    set_completer([function]) -> None
    Set or remove the completer function.
    The function is called as function(text, state),
    for state in 0, 1, 2, ..., until it returns a non-string.
    It should return the next possible completion starting with 'text'.
    """
    pass

def set_completer_delims(string): # real signature unknown; restored from __doc__
    """
    set_completer_delims(string) -> None
    set the readline word delimiters for tab-completion
    """
    pass

def set_completion_display_matches_hook(function=None): # real signature unknown; restored from __doc__
    """
    set_completion_display_matches_hook([function]) -> None
    Set or remove the completion display function.
    The function is called as
      function(substitution, [matches], longest_match_length)
    once each time matches need to be displayed.
    """
    pass

def set_history_length(length): # real signature unknown; restored from __doc__
    """
    set_history_length(length) -> None
    set the maximal number of items which will be written to
    the history file. A negative length is used to inhibit
    history truncation.
    """
    pass

def set_pre_input_hook(function=None): # real signature unknown; restored from __doc__
    """
    set_pre_input_hook([function]) -> None
    Set or remove the pre_input_hook function.
    The function is called with no arguments after the first prompt
    has been printed and just before readline starts reading input
    characters.
    """
    pass

def set_startup_hook(function=None): # real signature unknown; restored from __doc__
    """
    set_startup_hook([function]) -> None
    Set or remove the startup_hook function.
    The function is called with no arguments just
    before readline prints the first prompt.
    """
    pass

def write_history_file(filename=None): # real signature unknown; restored from __doc__
    """
    write_history_file([filename]) -> None
    Save a readline history file.
    The default filename is ~/.history.
    """
    pass

# no classes
