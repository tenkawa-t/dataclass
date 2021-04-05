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
    image: str
    void: str
    seg: str
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


def main():
    src_path = '/home/tenkawa/PycharmProjects/dataclass/data'
    src = Path(src_path)
    csv_list = list(src.glob('**/*.csv'))
    all_gt_list = list()
    # 1dir1gt想定
    for filename in csv_list:
        dirname = Path(filename).parents[1].name
        # gt1frame = Gt1frame(get_bbox(filename), 'test', 'test', 'test', 'test')
        gt1dir_list = csv2list(filename)
        gt1dir = GT1dir(gt1dir_list, dirname)
        all_gt_list.append(gt1dir)

    all_gt_class = GtAll(all_gt_list)
    print("a")
    # image: str
    # void: str
    # seg: str
    # imagepath: str



    # 1画像ごとに処理する必要あり
    testgt = Gt1frame(bbox, 'test', 'test', 'test', 'test')
    print(testgt)

    # BBoxes のlistをGTに入れる

    # GT1dirに入れる


main()

print("finish")

