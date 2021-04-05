from dataclasses import dataclass
# import pandas as pd
from dataclass_csv import DataclassReader
from pathlib import Path
@dataclass
class BBox:
    # fid: int
    Width: float # = 0
    Height: float # = 0
    Bbx: float # = 0
    Bby: float # = 0
    Filename: str # = None
    Occ: int # = 0
    Frameout: int # = 0
    objid: int # = 0
    gtcategory: int # = 0
    angle: float # = 0
    option: int # = 0

    def ltrb(self):
        pass


@dataclass
class Seg:
    pass


@dataclass
class Pose:
    pass


@dataclass
class Gt1frame:
    BBoxes: list
    dirname: str
    # image: str
    # void: str
    # seg: str
    imagepath: str
    # property: Dict eye/face/body/...{


@dataclass
class GT1dir:
    GTframes: Gt1frame
    category: str

@dataclass
class GtAll:
    GT: list

def csv2list(filename):
    csv_list = list()
    with open(filename) as users_csv:
        reader = DataclassReader(users_csv, BBox)
        for row in reader:
            csv_list.append(row)
    return csv_list

def get_gt_1dir(csv_list):
    all_gt_list = list()
    for filename in csv_list:
        dirname = Path(filename).parents[1].name
        gt1dir_list = csv2list(filename)
        gt1dir = GT1dir(gt1dir_list, dirname)
        all_gt_list.append(gt1dir)
    return all_gt_list

def get_gt_1frame(csv_list):
    dir_gt_list = list()
    for filename in csv_list:
        dirname = Path(filename).parents[2].name
        gt1frame_list = csv2list(filename)
        framename = gt1frame_list[0].Filename
        gt1frame = Gt1frame(gt1frame_list, dirname, framename)
        dir_gt_list.append(gt1frame)
    return dir_gt_list

def main():
    # src_path = '/home/tenkawa/PycharmProjects/dataclass/data'
    src_path = '/home/tenkawa/PycharmProjects/dataclass/data2'
    src = Path(src_path)
    csv_list = list(src.glob('**/*.csv'))
    # 1dir1gt想定
    # all_gt_class = GtAll(get_gt_1dir(csv_list))
    all_gt_class = GtAll(get_gt_1frame(csv_list))

    print("a")
    # image: str
    # void: str
    # seg: str
    # imagepath: str



    # 1画像ごとに処理する必要あり
    # testgt = Gt1frame(bbox, 'test', 'test', 'test', 'test')
    # print(testgt)

    # BBoxes のlistをGTに入れる

    # GT1dirに入れる


main()

print("finish")

