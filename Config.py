import json


class Config:
    def _fill_config(self, config_file):
        j, _ = Config.load_json(config_file)
        Config.__update_members_from_dict(self, j)
        sections_dict = self._get_sub_sections()
        for section_class, labels in sections_dict.items():
            json_section = j
            for label in labels:
                if label in json_section:
                    json_section = json_section[label]
                else:
                    json_section = None
                    break
            if json_section:
                Config.__update_members_from_dict(section_class, json_section)

    def _get_sub_sections(self):
        # return: subsections dictionary with subsection name and class
        return {}

    @staticmethod
    def __update_members_from_dict(clazz, json_dict):
        clazz.__dict__.update(
            (k, json_dict.get(k)) for k in
            clazz.__dict__.keys() & json_dict.keys())

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
