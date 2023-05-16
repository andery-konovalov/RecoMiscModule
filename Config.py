import json
import os.path


class Config:
    __YOLO_KEY = "yolo"
    __RABBIT_KEY = "rabbit_recognizer"
    __RABBIT_DRAWER_KEY = "rabbit_drawer"

    class EmptyConfig:
        pass

    def __init_yolo_section(self):
        self.yolo = Config.EmptyConfig()
        self.yolo.SourcePath = None
        self.yolo.VirtualEnvFolderName = None
        self.yolo.version = None
        self.yolo.logFile = "yolo.log"
        self.yolo.weights = None

    def __init_rabbit_section(self):
        self.rabbit = Config.EmptyConfig()
        self.rabbit.host = None
        self.rabbit.port = 5672

        self.rabbit.reco_request_queue = None
        self.rabbit.reco_error_queue = None

        self.rabbit.drawer_request_queue = None
        self.rabbit.drawer_error_queue = None

        self.rabbit.reco_result_queue = None

        self.rabbit.user_name = None
        self.rabbit.password = None
        self.rabbit.images_cache_queue = None

    def __init_rabbit_drawer_section(self):
        self.rabbit_drawer = Config.EmptyConfig()
        self.rabbit_drawer.host = None
        self.rabbit_drawer.port = 5672

        self.rabbit_drawer.drawer_request_queue = None
        self.rabbit_drawer.drawer_error_queue = None

        self.rabbit_drawer.reco_result_queue = None

        self.rabbit_drawer.user_name = None
        self.rabbit_drawer.password = None

    @staticmethod
    def __update_members_from_dict(clazz, json_dict):
        clazz.__dict__.update(
            (k, json_dict.get(k)) for k in
            clazz.__dict__.keys() & json_dict.keys())

    def __init__(self, config_file):
        self.MarkedImagesFolder = ""
        self.HostURL = ""
        self.LogsFolder = ""
        json, _ = Config.load_json(config_file)
        Config.__update_members_from_dict(self, json)

        self.__init_yolo_section()
        Config.__update_members_from_dict(self.yolo, json[Config.__YOLO_KEY])
        if Config.__RABBIT_KEY in json:
            self.__init_rabbit_section()
            Config.__update_members_from_dict(self.rabbit, json[Config.__RABBIT_KEY])
        if Config.__RABBIT_DRAWER_KEY in json:
            self.__init_rabbit_drawer_section()
            Config.__update_members_from_dict(self.rabbit, json[Config.__RABBIT_DRAWER_KEY])

    @staticmethod
    def load_json(file_name):
        j = None
        result = True
        try:
            with open(file_name, 'r') as j:
                j = json.load(j)
        except OSError:
            result = False
        return j, result
