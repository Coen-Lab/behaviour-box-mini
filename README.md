# Behaviour Box Mini
A deliberately simple, open-source box for recording mouse locomotion, built as a first step
towards scalable behavioural phenotyping.

<p align="center">
<img src="assembly/Pictures/Box%20render.png" width="440" alt="Exploded render of the printed parts">
</p>

## Overview

Every part is either printed or bought off the shelf, the whole build is six printed pieces and
two screws, and a session needs one cable to the computer. Simplicity is the point: a box that is
quick to replicate, cheap enough to run in parallel, and hard to set up wrongly.

The box pairs video capture with rotary-encoder wheel tracking, using Harp for synchronised
timestamping and Bonsai for control and acquisition. The aim is to pre-screen animals before
downstream experiments, so behavioural differences show up early — improving experimental
efficiency and reducing the number of animals needed later.

![Example frames captured inside the box](assembly/Pictures/Example%20frames.jpg)

## Features

- **Simple to build** — printed parts, off-the-shelf components, no machining
- **Standardised acquisition** — reproducible recording of spontaneous behaviour across experiments
- **Video tracking** — continuous capture for observation and offline analysis
- **Wheel locomotion** — high-temporal-resolution measurement of voluntary movement
- **Harp integration** — reliable hardware communication and synchronised timestamping
- **Bonsai workflows** — open, modular, easily customisable pipelines
- **Extensible** — built for community development and further behavioural measures

## Bill of Materials

| # | Part | Qty | Supplier | Cost | Notes |
|---|------|-----|----------|------|-------|
| 1 |[3D Print Filament](https://uk.store.bambulab.com/products/pla-basic-filament)|2|Bambu Lab|18*2|PLA|
| 2 |[FLIR cameras](https://www.digikey.co.uk/en/products/detail/flir-integrated-imaging-solutions-inc/BFS-U3-16S2M-CS/16528335)|1|Digikey|277|BFS-U3-16S2M-CS|
| 3 |[Rotary Encoder](https://www.aliexpress.com/item/1005005665235932.html)|1|Ali-Express|18|1024 PR version|
| 4 |[HARP Behaviour Board](https://open-ephys.org/harp/oeps-1216)|1|Open Ephys|415|Listed at €510|
| 5 |[locking USB 3.0 Micro-B cable](https://www.amazon.co.uk/dp/B0BYDYKB75)|1|Amazon|18|5 m, black straight connector|
| 6 |[GPIO cable](https://www.digikey.co.uk/en/products/detail/flir-integrated-imaging-solutions-inc/ACC-01-3010/16528421)|1|Digikey|33|For Camera Trigger. FLIR ACC-01-3010, Hirose HR10 6-pin|
| 7 |[Varifocal lens, 2.8-12 mm, CS mount](https://www.aliexpress.com/item/1005006136279769.html)|1|Ali-Express|12.49|Manual zoom and focus, no IR filter|
| 8 |[IR LED strip, 850 nm, 12 V](https://www.aliexpress.com/item/1005009046927133.html)|0.5 m|Ali-Express|8.29|Also stocked in 2 m|
| 9 |[Mini PC, e.g. GEEKOM Air12](https://www.amazon.co.uk/dp/B0CPLNDHZ5)|1|Amazon|240|Meets the minimum specification below|
| 10 |[M3 hex screw set, 6-14 mm](https://www.aliexpress.com/item/1005008068815080.html)|1|Ali-Express|9|Mounts the rotary encoder (3 × M3 × 8 mm). Set covers 6-14 mm|

Approximate total: £1070

### Computer minimum specification

One machine per box runs Bonsai and writes the video. The GEEKOM Air12 in row 9 is the cheapest
unit we have found that clears the bar, so its specification is the floor:

| | Minimum |
|---|---|
| CPU | 4-core x86, Intel N-series or PT7505 class |
| RAM | 16 GB |
| Storage | 512 GB NVMe SSD |
| USB | One USB 3.2 Gen 1 Type-A port dedicated to the camera |
| OS | Windows 11, for Bonsai and the Spinnaker SDK |

Two things to watch:

- **No PCIe slot** on a mini PC, so the camera runs from a built-in port rather than an expansion card.
- **Storage** — compressed video runs at roughly 1-4 GB per hour, so 512 GB holds weeks. Uncompressed
  would fill it in under three hours at 30 fps.

## Build Guide

1. **Print** — STL files in [assembly/](assembly/). 15% infill, supports where needed.
2. **Assemble** — [assembly guide](assembly/assembly-guide.md).
3. **Wire** — [wiring](assembly/wiring.md).
4. **Software** — [software](Softwares/software.md).

## How to Run the Workflow

Configure the camera and experiment settings first — see [software](Softwares/software.md). Then:

1. Clean the box with **dehydrated ethanol** or another disinfectant, and wipe it completely dry.

2. Place the mouse in the box.

3. Fit the lid with the camera attached.

   > **Note:** For area measurements (e.g. mouse area per frame), the camera orientation must match the predefined crop region. See [software](Softwares/software.md).

4. Connect the hardware:
   - 12 V power supply to the Harp Behaviour Board
   - Rotary encoder to the Harp Behaviour Board (default **Port P0**)
   - IR LED strip power supply
   - Camera USB cable to the computer
   - Camera GPIO trigger cable to the Harp Behaviour Board

5. Minimise external light — turn the room lights off, or cover the box with black fabric (**recommended**).

6. Open the Bonsai workflow and check the **live camera preview** is updating.

7. Set the save directory, subject ID, session ID and trial length, then click **Start**.

8. Recording stops automatically at the trial length, saving a video and a CSV of the behavioural data.

9. Return the mouse to its home cage.

10. Clean the box before the next recording, checking the corners carefully — faeces are easy to miss.

## Troubleshooting

- **No live camera preview**
  - Check that the camera is connected via the Locking USB 3.0 cable.
  - Verify that the correct version of the Spinnaker SDK is installed.
  - Ensure the camera serial number matches the connected device.

- **Rotary encoder not responding**
  - Check the RJ45 connection to the Harp Behaviour Board.
  - Verify that the encoder is connected to the correct input pins.

### I cannot see the camera preview or CSV output

If the camera preview and CSV output windows do not appear after starting the workflow, they can be reopened manually.

#### Camera Preview

1. Right-click the **Logging** node and select **Show Default Editor...**
2. In the editor window, right-click the **LogVideo** node and select **Show Default Editor...**
3. Right-click the **VideoWriter** node and select:
   - **Show Visualizer**
   - **Bonsai.*ImageVisualizer**

#### CSV Output

1. Right-click the **CSVWriter** node.
2. Select:
   - **Show Visualizer**
   - **Bonsai.*TextVisualizer**

> **Tip**
>
> Avoid closing these visualizer windows manually. When the workflow is stopped, Bonsai will close them automatically. If they remain open during normal operation, they will automatically reappear the next time the workflow is started.
## License

[LICENSE](LICENSE)
