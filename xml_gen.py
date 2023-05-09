import random
import string
import uuid
from xml.etree.ElementTree import Element, tostring


class XMLGenerator:

    def generate_xml(self) -> Element:
        root = Element("root")
        root.insert(0, self.get_uuid_elem())
        root.insert(1, self.get_int_elem())
        root.insert(2, self.get_objects())
        return tostring(root)

    @staticmethod
    def get_uuid_elem() -> Element:
        elem = Element('var')
        elem.set('name', 'id')
        elem.set('value', str(uuid.uuid4()))
        return elem

    @staticmethod
    def get_int_elem() -> Element:
        elem = Element('var')
        elem.set('name', 'level')
        elem.set('value', str(random.choice(range(101))))
        return elem

    @staticmethod
    def get_objects() -> Element:
        elem = Element('objects')

        for index in range(1, random.randint(2, 11)):
            obj = Element('object')
            obj.set('name', ''.join(random.choice(string.ascii_letters) for _ in range(6)))
            elem.insert(index, obj)
        return elem
