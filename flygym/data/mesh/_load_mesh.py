import trimesh

mesh_name = "RWing.stl"
mesh = trimesh.load(f'/home/xw/fly_unnamed_torch/fly_unnamed/env/neuromechfly/data/mesh/{mesh_name}')
bbox = mesh.bounding_box.extents  # [x, y, z]
half_sizes = bbox / 2
print("MuJoCo size:", half_sizes)
