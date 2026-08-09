# Printed parts

One STL per unique component. Six printed parts in total, five unique geometries: the thumb screw
is printed twice.

| File | Print | What it is |
| --- | --- | --- |
| `Arena.stl` | 1 | Box body, 207 x 207 x 220 mm |
| `LidAndSpacer.stl` | 1 | Tapered tower: closes the box and sets camera height, 199 x 199 x 240 mm |
| `CamHolder.stl` | 1 | Clamps the camera between body and lens, 46 x 46 x 80 mm |
| `Wheel.stl` | 1 | Running wheel, 157 mm diameter |
| `ThumbScrew.stl` | 2 | Both screws are the same part, 16 x 16 x 25 mm |

Exported from `Complete_Package` in Fusion. The meshes carry their assembly coordinates rather than
being centred on the origin, so parts land away from the plate when first loaded. Any slicer will
drop them to the bed and place them; nothing about the geometry needs changing.

For print settings and the build order see [../README.md](../README.md).
