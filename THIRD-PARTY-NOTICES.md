# Third-party notices

Everything in this repository is covered by the [MIT License](LICENSE) except the components listed
below, which are redistributed under their own terms.

## UclOpen packages

`Software/Behaviour_Box/local_packages/` contains five NuGet packages, redistributed as
binaries because they are not published on nuget.org and the workflow will not restore without them:

- `UclOpen.Core.0.0.0-sandbox`
- `UclOpen.Devices.0.0.0-sandbox`
- `UclOpen.Logging.0.0.0-sandbox`
- `UclOpen.Video.0.0.0-sandbox`
- `UclOpen.Vision.0.0.0-sandbox`

They come from [ucl-open/ucl-open](https://github.com/ucl-open/ucl-open) at commit
`27892d3ee53b8297eeede92571668fed8c425248`, and each carries the licence text below in its own
`LICENSE` file.

```
BSD 3-Clause License

Copyright 2026 (c) University College London and Contributors

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## Not redistributed here

`Software/Setup.cmd` downloads Bonsai and restores the packages listed in `Bonsai.config` from
nuget.org at install time. None of those are stored in this repository, and each remains under its
own licence. Bonsai itself is MIT, copyright the Bonsai Foundation CIC and Contributors.

The Spinnaker SDK is installed by hand from Teledyne and is not redistributed in any form.
