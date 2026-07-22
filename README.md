# Behaviour Box Mini
A simplified, open-source behavioural recording platform focusing on robust mouse locomotion tracking as the first step towards scalable behavioural phenotyping.
<img width="1076" height="862" alt="Mousebox_Mini" src="https://github.com/user-attachments/assets/58b505bc-96c5-453c-a68e-cf2c58eb5d2b" />

## Overview

The Mini Behaviour Box is an open-source, standardised behavioural recording platform for automated mouse locomotion tracking. The system combines video acquisition with rotary encoder-based locomotion measurement and is built around the Harp ecosystem using Bonsai for hardware control, data synchronisation, and data acquisition.
The long-term objective of this project is to establish a scalable behavioural phenotyping pipeline that can be used to pre-screen experimental animals before downstream experiments. By identifying behavioural differences at an early stage, the platform aims to improve experimental efficiency, reduce unnecessary resource use, and support the principles of animal welfare by helping minimise the number of animals required for subsequent studies.

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
| 1 |Box Bodies|2|Bambu Lab|18| |

Approximate total: £TBD

## Build Guide

1. **Print** — STL files in [hardware/stl/](hardware/stl/). Print settings: TBD.
2. **Assemble** — Follow the [assembly guide](assembly/assembly-guide.md).
3. **Wire** — See [wiring diagram](electronics/wiring-diagram.svg) and [pinout](electronics/pinout.md).
4. **Software** — Install [Bonsai](https://bonsai-rx.org/) and the packages listed in [bonsai/extensions.md](bonsai/extensions.md).

## Quick Start

TBD — brief instructions to go from assembled box to running a first session.

## License

[LICENSE](LICENSE)

## Citation

TBD
