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
> Bonsai is only compatible with specific versions of the Spinnaker SDK. The compatible installation package is included in this repository.
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
