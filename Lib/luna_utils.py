# luna_utils.py

import os
import platform

class LunaUtils:
    def init(self):
        pass

    def get_device_info(self):
        # Get device information (OS, architecture, etc.)
        return {
            "os": platform.system(),
            "architecture": platform.architecture
