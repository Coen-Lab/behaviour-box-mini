# Software

Two components:

- **Spinnaker SDK (SpinView)** — camera driver and configuration
- **Bonsai** — acquisition, encoder recording, trigger control and data saving

Install them in that order: Bonsai cannot see the camera without the Spinnaker driver.

---

## Spinnaker SDK (SpinView)

Spinnaker is Teledyne FLIR's official package. It provides the camera driver and lets you configure
image size, exposure time, gain, frame rate and trigger mode.

Download it from
[Teledyne Vision Solutions](https://www.teledynevisionsolutions.com/support/support-center/software-firmware-downloads/iis/spinnaker-sdk-download/spinnaker-sdk--download-files/?pn=Spinnaker+SDK&vn=Spinnaker+SDK).
An account is needed, so this step cannot be scripted and must be done by hand.

> **Important**
>
> Bonsai works only with Spinnaker SDK **4.2.0.83**. Pick the version deliberately: the download page
> defaults to the latest.
>
> This is upstream's requirement, not a local quirk. `Bonsai.Spinnaker 0.9.1` states it in its package
> description and ships a matching `SpinnakerNET_v140.dll` at exactly 4.2.0.83. The package provides
> the managed wrapper while the SDK provides the native runtime, and the two are version-locked, so a
> mismatch fails at interop and shows up as the camera simply not appearing.

---

## Bonsai

Run [`Setup.cmd`](Setup.cmd) once. It downloads Bonsai and restores
the packages listed in `Bonsai.config` from nuget.org and `local_packages/`, so nothing else needs
installing by hand.

Then, because of compatibility patches in this project, open the workflow manually rather than
launching it directly:

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

### Data output

Each recording gets its own folder, built from the settings above:

```
<save directory>\sub-<SubjectId>\ses-<SessionId>_date-<yyyy-MM-ddTHH-mm-ss>
```

The date is the UTC time at which the workflow started, so a late-evening session in British
Summer Time files under the following day. The folder holds `LogData.csv` and
`VideoData_Camera.avi`.

The CSV has one row per camera frame, with a header:

| Column | Meaning |
|---|---|
| `Seconds` | Harp clock time of the frame trigger, in seconds |
| `Timestamp` | Camera chunk timestamp |
| `FrameID` | Camera frame counter |
| `ExposureTime` | Exposure of that frame, from the camera chunk |
| `MouseLocation.X` | Mouse centroid, pixels from the left edge of the image |
| `MouseLocation.Y` | Mouse centroid, pixels from the top edge of the image |
| `WheelDistance` | Cumulative distance run since the recording started, in cm |

The centroid is a `Point2f`, which Bonsai's CsvWriter splits into the two dotted columns above
rather than one combined field, so the file has seven columns. The origin is the top-left pixel and
Y increases downwards, following OpenCV.

Acquisition constants, all set in the workflow:

| | Value |
|---|---|
| Frame rate | 50 Hz, camera hardware-triggered by the Harp board |
| Encoder counts per revolution | 4096 (1024 ppr, quadrature decoded x4) |
| Wheel diameter | 150 mm, so a circumference of 47.12 cm |
| Distance per encoder count | 0.0115 cm |

`WheelDistance` accumulates the per-sample encoder difference, with 16-bit counter wraparound
corrected, so it increases monotonically while the animal runs forwards and is not reset within a
session. Change `CountsPerRev` or `WheelDiameterMm` in the workflow if you use a different encoder
or wheel, or the distances will be silently wrong.

---

## Camera settings

The workflow ships with recommended settings and should not need changing. If it does:

### Exposure time, gain and binning

1. Double-click the **Metadata** node.
2. Click on an empty area within the editor.
3. Modify the desired parameters in the **Properties** panel.

### Frame rate

1. Double-click the **Logging** node.
2. Click on an empty area.
3. Adjust the frame rate in the **Properties** panel.

> **Note**
>
> Changing **Binning** also changes the output resolution. If you need a specific image size, set the
> camera dimensions manually in **SpinView** afterwards.

## Mouse centroid tracking

Position is estimated by **centroid tracking**. Compared with pose estimation or segmentation it is
computationally light, robust, and accurate enough for locomotion, which suits a standardised
screening platform.

Each frame's centroid is written to the CSV as `MouseLocation`, in pixels. Nothing is classified
online: if you need to know whether the animal was on the wheel or in the arena, test the logged
coordinates against a wheel region offline. Doing it after the fact means one region definition
applied identically to every session, rather than one drawn by hand per rig.

> **Note**
>
> The hardware and default parameters are optimised for **black mice**. For **white or light-coloured
> mice**, either:
>
> - Print the box in a darker colour to increase contrast, or
> - Adjust the tracking threshold for reliable centroid detection.
