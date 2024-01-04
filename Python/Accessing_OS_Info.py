"""
Purpose: Accessing Operating Sysytem information using Python
Date: 03/01/2024
Author: Lyra "Archivist" Hawkins
"""

import sys
import platform

print(sys.modules)
print(sys.version_info)
print(sys.platform) #can be used to set code specific to different OS's if sys.platform == "..." then proceed

print(platform.system())
print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.processor())
print(platform.python_compiler())
print(platform.platform())
