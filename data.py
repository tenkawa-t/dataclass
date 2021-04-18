from dataclasses import dataclass
import pickle
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
    """Gt1dirを格納、category別"""
    GTframes: Gt1frame
    category: str

    def printbbox(self):
        print(self.GTframes)
        for i in range(len(self.GTframes)):
            print(self.GTframes[i])


@dataclass
class GtAll:
    """Gtすべてを格納、binary出力機能"""
    GT: list

    def printbbox(self):
        print(self.GT)
        for i in range(len(self.GT)):
            print(self.GT[i])
        return self.GT

    def binary(self, filename):
        pickle.dump(self.GT, filename)