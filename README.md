# altwalker-graph-data-demo

A simple example of an AltWalker project that updates the graph data from the test code.

## Overview

This example showcases how you can update you graph data (model data) in order to influence the path generation.

Basically we have a node from witch we want to go.


> **Note**:
>
> This method doesn't works with the `offline` command because it generates all steps before the execution of the test code.
>
> This method only works with the `online` command, where only one step from the path is generated at a time and then executed.


Fist we will initialize a variable `number` inside the `action` section of the model with a default value:

```json
"actions": [
    "number = 0;"
]
```

Fist we will add a guard.

```json
"guard": "number > 0.5"
```

In order to update the graph data from your tests, you need to define the method with a parameter, and AltWalker will pass the graph data to your method. This method is a way of executing actions from you test code.

Then in the method corresponding with our branching vertex will add:

```python
def v_start(self, data):
    data['number'] = random.random()
```

## Setup

You can find the AltWalker setup guide [here](https://altom.gitlab.io/altwalker/altwalker/installation.html).

## Running the tests

```
$ altwalker online tests -m models/default.json "random(vertex_coverage(100))"
```

## License

This project is licensed under the [MIT License](LICENSE).
