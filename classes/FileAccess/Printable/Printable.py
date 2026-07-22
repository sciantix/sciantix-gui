
"""
----------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __      ___     .__   __..___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |    /   \    |  \ |  ||           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |   /  ^  \   |   \|  |`---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |  /  /_\  \  |  . `  |    |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  )  |
.----)   |   |  `----.|  | /  _____  \ |  |\   |    |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__|/__/     \__\|__| \__|    |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

----------------------------------------------------------------------------------------------------------------------------------

    Originally developed by G. Léandre

    Version : 1.5.0
    Year :    2026
    Authors : G. Léandre
"""


from .. import FileAccess


class Printable(FileAccess.FileAccess):
    def __init__(self, template):
        FileAccess.FileAccess.__init__(self)

        # Here template is a module, not the function
        self.__print_template = template
    
    
    def print(self):
        with open(f"{self.getPath()}{self.getName()}.txt", 'w') as file:
            # Here template is a module, not the function, so we have to call the .template function
            file.write(self.__print_template.template(self))
