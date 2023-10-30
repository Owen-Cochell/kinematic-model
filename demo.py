"""
This file showcases the functionality of the pmodel library.    
"""

import json

from pmodel.containers import Coordinates
from pmodel.pipeline import Pipeline
from pmodel.processors import *
from pmodel.globals import *

# Create a pipeline:

pipeline = Pipeline()

# Add some processors to the pipeline:

pipeline.append(print_process)
pipeline.append(TimeZeroProcessor())
pipeline.append(time_to_seconds)
pipeline.append(standardize_coords)
pipeline.append(to_mps)
pipeline.append(invert_zvel)
pipeline.append(SetOriginProcessor())
pipeline.append(to_enu)

# Load JSON data:

data = None
with open("data/data_20092023-15:33:03(more_movement).json", "r") as f:
    data = json.load(f)

# Iterate over JSON data:

for container in data:

    # For now, filter our attitude data:

    if container["mavpackettype"] == "ATTITUDE":

        continue

    # Create a container from JSON data:

    container = Coordinates.from_json(container)

    # Process container:

    done = pipeline(container)

    # Print container:

    print(done)
