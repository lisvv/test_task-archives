from pathlib import Path
from zipfile import ZipFile

from xml_gen import XMLGenerator


class ZipGenerator:

    @staticmethod
    def get_xml_data(count: int) -> None:
        xml_gen = XMLGenerator()
        for index in range(count):
            yield index, xml_gen.generate_xml()

    def create_zipfile(self) -> None:
        Path("./archives/").mkdir(parents=True, exist_ok=True)
        for index in range(50):
            with ZipFile(f'./archives/{index}.zip', 'w') as zip_file:
                for index, data in self.get_xml_data(count=100):
                    zip_file.writestr(f'{index}.xml', data)


if __name__ == '__main__':
    x = ZipGenerator()
    x.create_zipfile()
