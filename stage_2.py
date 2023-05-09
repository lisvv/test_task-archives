import csv
import multiprocessing
import os
import xml.etree.ElementTree as ET
from multiprocessing import Pool, Process
from zipfile import ZipFile


class XMLtoCSVConverter:

    def get_data(self) -> list:
        files = os.listdir('archives')
        with Pool(multiprocessing.cpu_count()) as pool:
            results = pool.map(self.unpack_rows, files)
            return results

    @staticmethod
    def unpack_rows(filename: str) -> tuple[list, list]:
        with ZipFile(f'./archives/{filename}', mode='r') as zfile:
            output_id_and_lvl = []
            output_objects = []
            for xml_file in zfile.infolist():
                with zfile.open(xml_file) as file:
                    obj = ET.fromstring(file.read())
                    output_id_and_lvl.append((obj[0].get('value'), obj[1].get('value')))
                    for item in obj[2]:
                        output_objects.append((obj[0].get('value'), item.get('name')))
            return output_id_and_lvl, output_objects


def write_id_and_lvl(result: list) -> None:
    with open('id_and_lvl.csv', 'w', newline='') as csvfile:
        for res in result:
            fieldnames = ['id', 'level']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for id_and_lvl in res[0]:
                writer.writerow({"id": id_and_lvl[0], "level": id_and_lvl[1]})


def write_objects(result: list) -> None:
    with open('objects.csv', 'w', newline='') as csvfile:
        for res in result:
            fieldnames = ['id', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for object in res[1]:
                writer.writerow({"id": object[0], "name": object[1]})


if __name__ == '__main__':

    converter = XMLtoCSVConverter()
    result = converter.get_data()
    p = Process(target=write_id_and_lvl, args=(result,))
    p.start()
    p2 = Process(target=write_objects, args=(result,))
    p2.start()
