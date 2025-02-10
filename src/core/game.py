from types import SimpleNamespace

# just a global namespace accessible to anything inside the game
# unfortunately this means no typehinting
# as everything is initialized in main

# i won't bother with this further as to avoid the troublesome error of circular import

gameSpace = SimpleNamespace()
