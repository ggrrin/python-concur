
<h1 align="center">
  Python Concur
</h1>

<p align="center">
   <img src="https://raw.githubusercontent.com/ajnsit/purescript-concur/master/docs/logo.png" height="100">
</p>

[**Documentation**](https://potocpav.github.io/python-concur/)

[**Examples**](https://github.com/potocpav/python-concur/tree/master/examples)

<!-- Start docs -->

Concur is a Python UI framework based on synchronous generators.

It is a port of [Concur for Haskell](https://github.com/ajnsit/concur) and [Concur for Purescript](https://github.com/ajnsit/purescript-concur).

Concur can be thought of as a layer on top of [PyImGui](https://github.com/swistakm/pyimgui), which is a set of bindings to the [Dear ImGui](https://github.com/ocornut/imgui) UI library. It helps you to get rid of unprincipled code with mutable state, and lets you build structured and composable abstractions.

A discussion of Concur concepts can also be found in the [Documentation for the Haskell/Purescript versions](https://github.com/ajnsit/concur-documentation/blob/master/README.md). This obviously uses Haskell/Purescript syntax and semantics, but many of the concepts will apply to the Python version.

Being an abstraction over ImGui, Concur is best used for debugging, prototyping and data analysis, rather than user-facing applications.

<p align="center">
<img src="https://raw.githubusercontent.com/potocpav/python-concur/master/screenshot.png">
</p>

<!-- End docs -->

## Installation

Clone the Concur repo including submodules:

```sh
git clone git@github.com:potocpav/python-concur.git --recurse-submodules
cd python-concur
```

Install a forked version of PyImGui from a submodule, then install Concur itself:

```sh
pip install -e pyimgui[glfw]
pip install -e .
```

Run the examples to verify the installation:

```sh
examples/all.py
```
