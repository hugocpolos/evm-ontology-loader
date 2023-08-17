import logging


class EvmInstances:
    instance1 = None
    instance2 = None
    instance3 = None
    cls = None

    def __init__(self, cls):
        logging.info(f"initializing instances of class '{cls.name}'")
        self.cls = cls
        self.instance1 = cls()
        self.instance2 = cls()
        self.instance3 = cls()
