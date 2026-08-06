# Software

Two components:

- **Spinnaker SDK (SpinView)** — camera driver and configuration
- **Bonsai** — acquisition, encoder recording, trigger control and data saving

---

## Spinnaker SDK (SpinView)

Spinnaker is Teledyne FLIR's official package. It provides the camera driver and lets you configure
image size, exposure time, gain, frame rate and trigger mode.

> **Important**
>
> Bonsai works only with Spinnaker SDK **4.2.0.83**. Another version may stop Bonsai detecting the
> camera, or make it behave unexpectedly or crash.

---

## Bonsai

The installers, packages and workflow are in
[`Behaviour_box_ucl_open`](Behaviour_box_ucl_open/). Because of compatibility patches in this
project, open the workflow manually rather than launching it directly:

1. Open **Bonsai**.
2. Select **File → Open**.
3. Open **`ucl_open_behaviour_box.bonsai`**.

With the workflow loaded, click the blank workspace to bring up the experiment settings in the
**Properties** panel on the right. Set before each recording:

- Save directory
- 8-digit camera serial number
- Session ID
- Subject ID
- Trial length (minutes)

Recording stops automatically at the trial length, saving a **CSV** of behavioural data and a
**video**.

---

## Camera Settings

The workflow ships with recommended settings and should not need changing. If it does:

### Exposure Time, Gain and Binning

1. Double-click the **Metadata** node.
2. Click on an empty area within the editor.
3. Modify the desired parameters in the **Properties** panel.

### Frame Rate

1. Double-click the **Logging** node.
2. Click on an empty area.
3. Adjust the frame rate in the **Properties** panel.

> **Note**
>
> Changing **Binning** also changes the output resolution. If you need a specific image size, set the
> camera dimensions manually in **SpinView** afterwards.

## Mouse Centroid Tracking

Position is estimated by **centroid tracking**. Compared with pose estimation or segmentation it is
computationally light, robust, and accurate enough for locomotion and area classification, which
suits a standardised screening platform.

Each frame's centroid **X** and **Y** go to the output CSV. To tell whether the mouse is on the
**running wheel** or in the **arena**, the workflow tests whether the centroid falls inside a
user-defined polygon covering the wheel: inside is **Wheel**, outside is **Arena**.

## Wheel Region Calibration

The wheel region is a **CropPolygon** node, set up for the reference hardware used during
development. Any of the following will throw the polygon out of alignment:

- Camera height
- Lens focal length
- Camera orientation (rotation)
- Behaviour box geometry

**Recalibrate the polygon after assembling the system**, or area classification will be wrong.

### Updating the polygon

1. Open the Bonsai workflow.
2. Navigate to the **CropPolygon** node.
3. Replace the existing polygon so that it accurately covers the running wheel.

Keep the following settings unchanged:

- **Fill Value:** `255,255,255,255`
- **Mask Type:** `ToZero`

If editing the existing polygon is difficult, it is often easier to create a new one:

1. Delete the existing **CropPolygon** node.
2. Add a new **CropPolygon** node (keep the settings above unchanged).
3. Start the workflow.
4. Select the **CropPolygon** node.
5. Click the **(...)** button next to the **Regions** property.
6. Draw a new polygon around the running wheel directly on the live camera image.

Once updated, the workflow will automatically classify each frame as either **Wheel** or **Arena** based on the mouse centroid location.

> **Note**
>
> The hardware and default parameters are optimised for **black mice**. For **white or light-coloured
> mice**, either:
>
> - Print the box in a darker colour to increase contrast, or
> - Adjust the tracking threshold for reliable centroid detection.
