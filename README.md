# Behaviour Box Mini
A simplified, open-source behavioural recording platform focusing on robust mouse locomotion tracking as the first step towards scalable behavioural phenotyping.
<img width="1001" height="1001" alt="behaviour box model" src="https://github.com/user-attachments/assets/24f0d75a-5f1c-4b53-864f-57188c86a247" />


## Overview

The Mini Behaviour Box is an open-source, standardised behavioural recording platform for automated mouse locomotion tracking. The system combines video acquisition with rotary encoder-based locomotion measurement and is built around the Harp ecosystem using Bonsai for hardware control, data synchronisation, and data acquisition.
The long-term objective of this project is to establish a scalable behavioural phenotyping pipeline that can be used to pre-screen experimental animals before downstream experiments. By identifying behavioural differences at an early stage, the platform aims to improve experimental efficiency, reduce unnecessary resource use, and support the principles of animal welfare by helping minimise the number of animals required for subsequent studies.

Example frames from a recording session:

![Example frames captured inside the box](assembly/Pictures/Example%20frames.jpg)

## Features

Standardised behavioural acquisition
Reproducible recording of spontaneous mouse behaviour across experiments.

Video-based tracking
Continuous camera capture for behavioural observation and offline analysis.

Rotary encoder locomotion measurement
High-temporal-resolution quantification of voluntary wheel movement.

Harp ecosystem integration
Reliable hardware communication and synchronised timestamping.

Bonsai-based acquisition workflows
Open, modular, and easily customisable data acquisition pipelines.

Designed for behavioural pre-screening
Supports early identification of behavioural phenotypes before downstream experimental procedures.

Open-source and extensible
Built to facilitate community development and future integration of additional behavioural measurements.

## Bill of Materials

| # | Part | Qty | Supplier | Cost | Notes |
|---|------|-----|----------|------|-------|
| 1 |[3D Print Filament](https://uk.store.bambulab.com/products/pla-basic-filament)|2|Bambu Lab|18*2|PLA|
| 2 |[FLIR cameras](https://www.digikey.co.uk/en/products/detail/flir-integrated-imaging-solutions-inc/BFS-U3-16S2M-CS/16528335)|1|Digikey|277|BFS-U3-16S2M-CS|
| 3 |Rotary Encoder|1|Ali-Express|18||
| 4 |HARP Behaviour Board|1|HARP|415||
| 5 |[locking USB 3.0 Micro-B cable](https://www.amazon.co.uk/dp/B0BYDYKB75)|1|Amazon|18|5 m, black straight connector|
| 6 |[GPIO cable](https://www.digikey.co.uk/en/products/detail/flir-integrated-imaging-solutions-inc/ACC-01-3010/16528421)|1|Digikey|33|For Camera Trigger. FLIR ACC-01-3010, Hirose HR10 6-pin|
| 7 |[Varifocal lens, 2.8-12 mm, CS mount](https://www.aliexpress.com/item/1005006136279769.html)|1|Ali-Express|12.49|Manual zoom and focus, no IR filter|
| 8 |[IR LED strip, 850 nm, 12 V](https://www.aliexpress.com/item/1005009046927133.html)|0.5 m|Ali-Express|8.29|Also stocked in 2 m|
| 9 |[Mini PC, e.g. GEEKOM Air12](https://www.amazon.co.uk/dp/B0CPLNDHZ5)|1|Amazon|240|Meets the minimum specification below|
| 10 |[M3 hex screw set, 6-14 mm](https://www.aliexpress.com/item/1005008068815080.html)|1|Ali-Express|9|50 each of 6, 8, 10, 12 and 14 mm|

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

A mini PC has no PCIe slot, so the camera has to run from a built-in port rather than an expansion
card. On storage, compressed video at 1440 x 1080 runs at roughly 1-4 GB per hour, so a 512 GB drive
holds weeks of recording. Writing uncompressed would fill it in under three hours at 30 fps.

## Build Guide

1. **Print and Assemble** — STL files in (assembly/). Print settings: 15% infill, enable support when needed.

<p align="center">
<img src="assembly/Pictures/Exploded%20render.png" width="360" alt="Exploded render of the printed parts">
</p>

2. Follow the [assembly guide](assembly/assembly-guide.md).
3. **Wire** — See [wiring](assembly/wiring.md) .
4. **Software** — See [Software](assembly/software.md)

Brief instructions to go from assembled box to running a first session:
## How to Run the Workflow

The **Software** section explains how to configure the camera and experiment settings. Once the hardware has been assembled and configured, follow the steps below to perform a behavioural recording.

1. Clean the behaviour box using **dehydrated ethanol** (or another suitable disinfectant), then wipe all surfaces thoroughly to ensure the box is completely dry.

2. Place the mouse into the behaviour box.

3. Install the lid with the camera attached.

   > **Note:** If area measurements (e.g. mouse area per frame) are required, ensure that the camera orientation matches the predefined crop region. See the **Software** section for further details.

4. Connect all required hardware:
   - 12 V power supply to the Harp Behaviour Board
   - Rotary encoder to the Harp Behaviour Board (default **Port P0**)
   - IR LED strip power supply
   - Camera USB cable to the computer
   - Camera GPIO trigger cable to the Harp Behaviour Board

5. Minimise external lighting by either:
   - Turning off the room lights, or
   - Covering the behaviour box with black fabric (**recommended**).

6. Open the Bonsai workflow and verify that the **live camera preview** is updating correctly.

7. Configure the experiment settings (e.g. save directory, subject ID, session ID and trial length), then click **Start**.

8. Recording will stop automatically once the specified trial length has been reached. Both a video recording and a CSV file containing the behavioural data will be saved automatically.

9. Remove the mouse from the behaviour box and return it to its home cage.

10. Clean the behaviour box before the next recording. Carefully inspect all corners of the box, as mouse faeces can be difficult to spot.

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
