# Fortnite Replay Parser

Minimal Python library intended to parse events in Fortnite replay files from Chapter 4 Season 1 with backwards compatibility for earlier versions.

## Example Usage

Here is an example function that will output match events regarding player eliminations and other statistics to a JSON file in the root directory.

This should help you get started with using the library and collecting data from game replays:
```python
import json
import os
from reader import FortniteReplayReader

from pydantic.json import pydantic_encoder

filename = os.path.join(os.path.dirname(__file__), "your_replay_file.replay")
with FortniteReplayReader(filename) as replay:
    header = replay.header.dict()
    metadata = replay.metadata.dict(exclude={"encryption_key"})

    output = {"header": header, "metadata": metadata, "events": replay.events}
    with open("replay_dump.json", "w") as f:
        json.dump(output, f, indent=4, default=pydantic_encoder)
```

## Credits

Credits to [Shiqan](https://github.com/Shiqan) for various protocol documentation and developing the original Python implementation. This library is a fork of [that project](https://github.com/Shiqan/fortnite-replay-reader).

Credits to [xNocken](https://github.com/xNocken) whose Node library proved to be a great reference in getting started with updating this project.
