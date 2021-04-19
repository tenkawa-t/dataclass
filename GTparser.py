from dataclasses import dataclass
from pathlib import Path
import re
import csv
import pandas as pd

def main():
    src_path = '/home/tenkawa/PycharmProjects/dataclass'
    a = GTParser(src_path)
    a.analysis_gt()

    # gtdir = a.gt_dir_list()
    # # gtdir.is_semseg()
    # # b = a.img_list()
    # # print(b)
    # c = a.gt_list()
    # print(c)
    # void = a.void_list()
    # print(void)
    # for i in c:
    #     t = a.read_and_analysis_csv_header(i)
    #     print(t)

@dataclass
class GTParser:
    '''
    by dir
    '''
    root: str=""

    def analysis_gt(self):
        gt_dir = self.gt_dir_list()
        for gt in gt_dir:
            # semseg OK
            semseg = self.is_semseg(gt)
            print(f'semseg:{semseg}')
            pose = self.is_pose(gt)
            print(f'pose:{pose}')
            if not semseg and not pose:
                # icb1/2/3/4 OK?
                # xtrack OK
                print('xtrack/icb')
                csv_list = self.gt_list()
                for csv in csv_list:
                   print(self.read_and_analysis_csv_header(csv))

        # detect
        # track
        # pose
        # 1 from csv header filename
        # from png filename

    def csv_filename(self, list):
        for csv in list:
            self.read_and_analysis_csv_header(csv)
            # print(csv)

    def csv_filename(self, csv):
        return csv.name
        # if '/gt/' in str(csv):
        #     print(csv)

    def is_semseg(self, dir):
        return True if '/seg/' in str(dir) else False

    def is_pose(self, dir):
        return True if '/Anno/' in str(dir) else False

    def read_and_analysis_csv_header(self, csv):
        df = pd.read_csv(csv, engine='python')
        columns = df.columns.tolist()
        xtrack = ['fid', 'Width', 'Height', 'Bbx', 'Bby', 'Filename', 'Occ', 'Frameout',
       'objid', 'gtcategory', 'angle', 'option']
        icb1 = []
        icb2 = []
        icb3 = []
        head = []
        if columns==xtrack:
            return 'xtrack'
        else:
            return 'none'


    def img_list(self):
        ip = Path(self.root)
        images = sorted([p for p in ip.glob('**/*') if re.search('/*\.(jpg|jpeg|png|gif|bmp)', str(p))])
        return images

    def gt_list(self):
        cp = Path(self.root)
        csvs = sorted([p for p in cp.glob('**/*') if re.search('/*\.(csv)', str(p))])
        return csvs

    def gt_dir_list(self):
        cp = Path(self.root)
        gt_dirs = [p for p in cp.glob('**/gt/*')]
        return gt_dirs

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



