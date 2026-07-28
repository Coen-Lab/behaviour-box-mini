# Software


The Mini Behaviour Box uses two software components:

1. **Spinnaker SDK (SpinView)** – Camera driver and configuration software
2. **Bonsai** – Behaviour acquisition and recording workflow
---


       Spinnaker SDK -> Camera Driver

       Bonsai -> Camera Acquisition
              -> Encoder Recording
              -> Trigger Control
              -> Data Saving

## Spinnaker SDK (SpinView)

Spinnaker SDK is the official software package for FLIR/Teledyne cameras. It provides the camera driver required for communication with the computer and allows users to configure camera parameters such as image size, exposure time, gain, frame rate and trigger mode.

> **Important**
>
> Bonsai is only compatible with specific versions of the Spinnaker SDK(ver 4.2.0.83)
>
> Installing a different version of the Spinnaker SDK may cause Bonsai to fail to detect the camera, behave unexpectedly, or crash.

---

## Bonsai

All required Bonsai installers, packages and workflows can be found in the **`mouse_box_ucl_open`** folder.

Due to compatibility patches included in this project, the workflow should be opened manually from File → Open rather than launched directly.

Instead:

1. Open **Bonsai**.
2. Select **File → Open**.
3. Open **`ucl_open_behaviour_box.bonsai`**.

After the workflow loads, click anywhere on the blank workspace to access the experiment settings in the **Properties** panel on the right-hand side.

The following parameters can be configured before each recording:

- Save directory
- 8-digit camera serial number
- Session ID
- Subject ID
- Trial length (minutes)

Once recording starts, the workflow will automatically stop when the specified trial length is reached. Both a **CSV file** containing behavioural data and a **video recording** will be saved automatically.

---

## Camera Settings

The default workflow has been configured with recommended camera settings and should not require modification for most users.

If camera parameters need to be adjusted:

### Exposure Time, Gain and Binning

1. Double-click the **Metadata** node.
2. Click on an empty area within the editor.
3. Modify the desired parameters in the **Properties** panel.

Available settings include:

- Exposure Time
- Gain
- Binning

### Frame Rate

To modify the frame rate:

1. Double-click the **Logging** node.
2. Click on an empty area.
3. Adjust the frame rate in the **Properties** panel.

> **Note**
>
> Changing the **Binning** value also changes the output image resolution. If a specific image size is required, we recommend opening **SpinView** and manually reconfiguring the camera image dimensions after changing the binning setting.
>
> ## Mouse Centroid Tracking

The Mini Behaviour Box uses a **centroid-based tracking** approach to estimate the animal's position throughout each recording. Compared with full-body pose estimation or segmentation methods, centroid tracking is computationally lightweight, robust, and sufficiently accurate for locomotion tracking and behavioural area classification, making it well suited for a standardised behavioural screening platform.

For each frame, the workflow calculates the mouse centroid and records its **X** and **Y** coordinates in the output CSV file.

To determine whether the mouse is on the **running wheel** or in the **arena**, the workflow checks whether the centroid lies inside a user-defined polygon representing the wheel region. If the centroid falls within the polygon, the frame is classified as **Wheel**; otherwise, it is classified as **Arena**.

### Wheel Region Calibration

The wheel region is defined using a **CropPolygon** node.

The default polygon is configured for the reference hardware setup used during development. However, changes to any of the following may cause the polygon to no longer align with the running wheel:

- Camera height
- Lens focal length
- Camera orientation (rotation)
- Behaviour box geometry

To ensure accurate area classification, **the wheel polygon should be recalibrated after assembling the system.**

### Updating the Wheel Polygon

1. Open the Bonsai workflow.
2. Navigate to the **CropPolygon** node.
3. Replace the existing polygon so that it accurately covers the running wheel.

Keep the following settings unchanged:

- **Fill Value:** `255,255,255,255`
- **Mask Type:** `ToZero`

If editing the existing polygon is difficult, it is often easier to create a new one:

1. Delete the existing **CropPolygon** node.
2. Add a new **CropPolygon** node.
3. Start the workflow.
4. Select the **CropPolygon** node.
5. Click the **(...)** button next to the **Regions** property.
6. Draw a new polygon around the running wheel directly on the live camera image.

Once updated, the workflow will automatically classify each frame as either **Wheel** or **Arena** based on the mouse centroid location.
