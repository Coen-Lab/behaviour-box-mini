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
3. Open **`Behaviour_Box_Mini.bonsai`**.

With the workflow loaded, click the blank workspace to bring up the experiment settings in the
**Properties** panel on the right. Set before each recording:

- Save directory
- 8-digit camera serial number
- Session ID
- Subject ID
- Trial length (minutes)

Recording stops automatically at the trial length, saving a **CSV** of behavioural data and a
**video**.

### Serial port

One thing is set once per machine rather than per recording. The Harp Behaviour Board appears as a
COM port, and the workflow ships pointing at **COM3**, which will be wrong on most computers. Find
the board in Device Manager under **Ports (COM & LPT)**, then set **PortName** in the same
**Properties** panel.

Get this wrong and the workflow fails on startup without saying why.

### Data output

Each recording gets its own folder, built from the settings above:

```
<save directory>\sub-<SubjectId>\ses-<SessionId>_date-<yyyy-MM-ddTHH-mm-ss>
```

The date is the UTC time at which the workflow started, so a late-evening session in British
Summer Time files under the following day. The folder holds `LogData.csv` and
`VideoData_Camera.avi`, the video written as MPEG-4 Part 2 in an AVI container.

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

`Seconds` is the Harp board's own record of when it fired the trigger, matched to the frame by
arrival order rather than by any shared identifier. That holds as long as every trigger produces a
frame. If one ever does not, each frame after it takes the timestamp of the frame before, and
nothing in the file announces it. To check a session, compare the camera's own `Timestamp` against
`Seconds`: the offset between the two clocks should be flat, and a step of one frame period means
the pairing has slipped.

Acquisition constants, all set in the workflow:

| | Value |
|---|---|
| Frame rate | 50 Hz, camera hardware-triggered by the Harp board |
| Exposure | 19 ms |
| Gain | 5 dB |
| Binning | 2, so the 1440 x 1080 sensor gives 720 x 540 images |
| Encoder counts per revolution | 4096 (1024 ppr, quadrature decoded x4) |
| Wheel diameter | 150 mm, so a circumference of 47.12 cm |
| Distance per encoder count | 0.0115 cm |

`WheelDistance` accumulates the per-sample encoder difference, with 16-bit counter wraparound
corrected, so it increases monotonically while the animal runs forwards and is not reset within a
session. Change `CountsPerRev` or `WheelDiameterMm` in the workflow if you use a different encoder
or wheel, or the distances will be silently wrong.

The board is put in **Position** mode, so the encoder register reports an absolute count that the
workflow differences, unwraps and re-accumulates. UclOpen's own `RunningWheel` uses **Displacement**
mode instead, and that is deliberately not copied here: it reports differences already, so the same
chain would difference them twice and the distances would be meaningless.

---

## Camera settings

The workflow ships with recommended settings and should not need changing. If it does:

### Exposure time, gain and binning

1. Double-click the **metadata** node.
2. Click on an empty area within the editor.
3. Modify the desired parameters in the **Properties** panel.

The order to tune them in is exposure first, then gain, then binning:

- **Exposure** buys image quality for free, so make it as long as the frame period allows. At 50 Hz
  a frame lasts 20 ms, and the shipped 19 ms leaves a millisecond of margin. Going over the frame
  period does not slow the camera down gracefully: it drops triggers, and because frames are paired
  with trigger events in order, a dropped one shifts every timestamp after it.
- **Gain** amplifies noise along with signal, so keep it as low as the image allows. Reach for it
  only once exposure is maxed out and the picture is still too dark, and prefer adding IR
  illumination instead.
- **Binning** is the file-size control. It sums neighbouring pixels, so it also brightens the image
  and cuts noise, at the cost of resolution: binning 2 turns the 1440 x 1080 sensor into 720 x 540
  and quarters the data rate.

### Frame rate

The camera is hardware-triggered, so its frame rate is set by the Harp board rather than by the
camera. Changing it means changing three things together, or the recordings go wrong quietly:

1. **Trigger0Frequency** on the `CameraTriggerController` node, inside **metadata** then
   **BehaviorBoards**. This is the one that actually sets the rate.
2. The **frames-per-second multiplier** in the **logging** group, which turns the trial length in
   minutes into a frame count. If it disagrees with the trigger, recordings stop at the wrong
   length.
3. **FrameRate** on the `VideoWriter` node, inside **logging** then **LogVideo**. This only labels
   the AVI, but if it is wrong the video plays back at the wrong speed.

Check the exposure still fits inside the new frame period.

## Mouse centroid tracking

Position is estimated by **centroid tracking**. Compared with pose estimation or segmentation it is
computationally light, robust, and accurate enough for locomotion, which suits a standardised
screening platform.

The centroid is in pixels, and nothing in the recording converts it to distance. The arena floor is
a 200 mm square, which gets you an approximate scale, but for anything quantitative calibrate your
own box: put a ruler or a printed grid on the floor, record a frame, and measure the millimetres per
pixel. The lens is a varifocal focused by hand, so the scale belongs to your box and changes the
moment anyone touches the zoom ring.

Nothing is classified online: if you need to know whether the animal was on the wheel or in the
arena, test the logged coordinates against a wheel region offline. Doing it after the fact means one
region definition applied identically to every session, rather than one drawn by hand per rig.

> **Note**
>
> The hardware and default parameters are optimised for **black mice**. For **white or light-coloured
> mice**, either:
>
> - Print the box in a darker colour to increase contrast, or
> - Adjust the tracking threshold for reliable centroid detection.
