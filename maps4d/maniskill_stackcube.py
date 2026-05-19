import torch
from geometry_primitive import Cuboid
from base_template import Map_4d


class RedCube:
    def __init__(self, sizes, positions, rotations):
        semantic1 = "red cube"
        self.Object_Prompt = "red cube"
        Nodes = []
        Edges = []
        size1 = sizes[:, 0:3]
        position1 = positions[:, 0:3]
        rotation1 = rotations[:, 0 : 6 * 1]
        Nodes.append(
            Cuboid(
                size1[:, 0],
                size1[:, 1],
                size1[:, 2],
                position=position1,
                rotation=rotation1,
                Semantic=semantic1,
            )
        )
        self.Nodes = Nodes
        self.Edges = Edges


class GreenCube:
    def __init__(self, sizes, positions, rotations):
        semantic1 = "green cube"
        self.Object_Prompt = "green cube"
        Nodes = []
        Edges = []
        size1 = sizes[:, 0:3]
        position1 = positions[:, 0:3]
        rotation1 = rotations[:, 0 : 6 * 1]
        Nodes.append(
            Cuboid(
                size1[:, 0],
                size1[:, 1],
                size1[:, 2],
                position=position1,
                rotation=rotation1,
                Semantic=semantic1,
            )
        )
        self.Nodes = Nodes
        self.Edges = Edges


class Desk:
    def __init__(self, sizes, positions, rotations):
        semantic1 = "desk"
        self.Object_Prompt = "desk"
        Nodes = []
        Edges = []
        size1 = sizes[:, 0:3]
        position1 = positions[:, 0:3]
        rotation1 = rotations[:, 0 : 6 * 1]
        Nodes.append(
            Cuboid(
                size1[:, 0],
                size1[:, 1],
                size1[:, 2],
                position=position1,
                rotation=rotation1,
                Semantic=semantic1,
            )
        )
        self.Nodes = Nodes
        self.Edges = Edges

class Map4d_StackCube(Map_4d):
    def __init__(self, sizes, positions, rotations, clip_model, preprocess=False):
        if preprocess:
            sizes = self._preprocess_parameters(sizes)

        Objects = []
        Objects.append(RedCube(sizes[:, 0:3], positions[:, 0:3], rotations[:, 0 : 6 * 1]))
        Objects.append(GreenCube(sizes[:, 3:6], positions[:, 3:6], rotations[:, 6 * 1 : 6 * 2]))
        Objects.append(Desk(sizes[:, 6:9], positions[:, 6:9], rotations[:, 6*2:6*3]))

        super().__init__(Objects)

    def _preprocess_parameters(self, sizes):
        size_range = (0.02, 5)
        min_s, max_s = size_range
        sizes = torch.sigmoid(sizes) * (max_s - min_s) + min_s
        return sizes


if __name__ == "__main__":
    StackCube_4d = Map4d_StackCube