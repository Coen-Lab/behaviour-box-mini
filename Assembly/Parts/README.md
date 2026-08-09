# Printed parts

One STL per unique component. Six printed parts in total, five unique
geometries: the thumb screw is printed twice.

| File | Print | Notes |
| --- | --- | --- |
| `Arena.stl` | 1 | |
| `Wheel.stl` | 1 | |
| `CamHolder.stl` | 1 | |
| `CamSpacer.stl` | 1 | |
| `ThumbScrew.stl` | 2 | Both screws are the same part |

Exported from `Complete_Package` in Fusion. The meshes carry their assembly
coordinates rather than being centred on the origin, so parts will land away
from the plate when first loaded. Any slicer will drop them to the bed and
place them; nothing about the geometry needs changing.

`../Behaviour_Box_Complete.stl` is the whole box as one body, for reference
only. It cannot be printed. `../Behaviour_Box_Complete.step` is the editable
solid model.
