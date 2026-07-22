## About

`PortAudio.NET` provides low-level C# bindings for [PortAudio](https://www.portaudio.com/). Currently only Windows x64 is well-tested, although Linux x64 is expected to work if bindings are regenerated.

Most of PortAudio's host API-specific functionality is not yet exposed with the exception of WASAPI.

## How to Use

This package includes only the managed bindings, and should be combined with the appropriate native runtime `PortAudio.NET.Native.*` package when deployed in self-contained applications.

## Additional Documentation

For additional documentation and examples, refer to the [API documentation](https://bonsai-rx.org/portaudio.net) and the [official PortAudio documentation](https://files.portaudio.com/docs/v19-doxydocs/).

## Feedback & Contributing

`PortAudio.NET` is released as open source under the [MIT license](https://licenses.nuget.org/MIT). Bug reports and contributions are welcome at [the GitHub repository](https://github.com/bonsai-rx/portaudio.net).