from dataclasses import dataclass
# import pandas as pd
from dataclass_csv import DataclassReader
from pathlib import Path
from data import BBox, Seg, Pose, Gt1frame, GT1dir, GtAll

"""設計図
- [x] BBoxデータ格納クラス
- [] semsegデータ格納クラス
- [] poseデータ格納クラス
- [] 追尾用にディレクトリ単位で保管できること
- [] カテゴリ単位で保管できること
- [] バイナリとして出力できること

"""
def dataclass_csv2list(filename, gtclass):
    csv_list = list()
    with open(filename) as users_csv:
        reader = DataclassReader(users_csv, gtclass)
        for row in reader:
            csv_list.append(row)
    return csv_list

def get_gt_1dir(csv_list, gtclass):
    all_gt_list = list()
    for filename in csv_list:
        dirname = Path(filename).parents[1].name
        gt1dir_list = dataclass_csv2list(filename, gtclass)
        gt1dir = GT1dir(gt1dir_list, dirname)
        all_gt_list.append(gt1dir)
    return all_gt_list

def get_gt_1frame(csv_list, gtclass):
    dir_gt_list = list()
    for filename in csv_list:
        dirname = Path(filename).parents[2].name
        gt1frame_list = dataclass_csv2list(filename, gtclass)
        framename = gt1frame_list[0].Filename
        gt1frame = Gt1frame(gt1frame_list, dirname, framename)
        dir_gt_list.append(gt1frame)
    return dir_gt_list

def main():
    # src_path = '/home/tenkawa/PycharmProjects/dataclass/data'
    src_path = '/home/tenkawa/PycharmProjects/dataclass/data2'
    src = Path(src_path)


    # 1dir1gt想定
    # csv_list = list(src.glob('**/*.csv'))
    # all_gt_class = GtAll(get_gt_1dir(csv_list))

    # 1frame1gt想定
    csv_list = list(src.glob('**/*.csv'))
    # 複数ディレクトリにまたがるものをどう分離するか。単純
    # framegt = get_gt_1fr/ame(csv_list)
    all_gt_class = GtAll(get_gt_1frame(csv_list, BBox))
    all_gt_class.printbbox()
    all_gt_class.binary('test.pickle')
    print("a")

    # 1画像ごとに処理する必要あり
    # testgt = Gt1frame(bbox, 'test', 'test', 'test', 'test')
    # print(testgt)


if __name__ == '__main__':
    main()

print("finish")

