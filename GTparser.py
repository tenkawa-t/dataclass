from dataclasses import dataclass
from pathlib import Path
import re
import csv

def main():
    # src_path = '/home/tenkawa/PycharmProjects/dataclass/data'
    src_path = '/home/tenkawa/PycharmProjects/dataclass'
    # src = Path(src_path)
    a = GTParser(src_path)
    b = a.img_list()
    print(b)
    c = a.gt_list()
    print(c)
    void = a.void_list()
    print(void)
    for i in c:
        t = a.read_and_analysis_csv_header(i)
        print(t)

@dataclass
class GTParser:
    root: str=""

    def analysis_gt(self):
        # icb
        # xtrack
        # detect
        # track
        # semseg
        # pose
        # 1 from csv header filename
        # from png filename
        #
        pass
    def csv_filename(self, list):
        for csv in list:
            self.ana_filename(csv)
            # print(csv)

    def filename(self, csv):
        name = csv.name
        if '/gt/' in str(csv):
            # 親ディレクトリ取得
            # csv
            # while csv.parents[2]
            print(csv)

    def read_and_analysis_csv_header(self, csv):
        with open(csv, 'r') as f:
            for row in f:
                print(row)


    def img_list(self):
        ip = Path(self.root)
        images = sorted([p for p in ip.glob('**/*') if re.search('/*\.(jpg|jpeg|png|gif|bmp)', str(p))])
        return images

    def gt_list(self):
        cp = Path(self.root)
        csvs = sorted([p for p in cp.glob('**/*') if re.search('/*\.(csv)', str(p))])
        return csvs

    def void_list(self):
        ip = Path(self.root)
        voids = sorted([p for p in ip.glob('**/Void/*') if re.search('/*\.(png)', str(p))])
        return voids

    def out1dircsv(self):
        pass
    def out1imgcsv(self):
        pass

    def df_all(self):
        pass


main()



