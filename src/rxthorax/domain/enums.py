from enum import Enum


class PathologyLabel(str, Enum):
    NORMAL = "normal"
    PNEUMONIA = "pneumonia"
    NODULE = "nodule"
    OPACITY = "opacity"
    OTHER = "other"


class StudySplit(str, Enum):
    TRAIN = "train"
    VALIDATION = "validation"
    TEST = "test"
