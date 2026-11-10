# helloWorld
This repo will have some simple output lines; mainly demonstrates repo

10.21 Added a .py file that outputs 'hello'

## Feature Specifications

- **Manual-primary (`manual-feature`):** Expand the default greeting demo with
  additional named hello and goodbye examples.
- **AI-primary (`ai-feature`):** Accept zero or more names as command-line
  arguments, greet each supplied name, and preserve the default demo when no
  names are provided.

## Feature Development Comparison

The `manual-feature` branch updates the greeting demo with additional example
calls, including more names and a goodbye. Its implementation is a direct,
manual edit to the program's existing main block; running the script displays
the expanded sequence.

The `ai-feature` branch adds personalized command-line greetings. It uses
Python's `argparse` to accept one or more names, loops over them to greet each
person, and preserves the original demo when no names are supplied. The AI
implementation worked correctly on its first run: single-name, multiple-name,
and default-demo behavior all produced the expected output. No AI-produced
implementation code needed to be modified or rejected; regression tests and
usage documentation were added to verify and explain the feature.

The AI approach gave me greater confidence in the finished feature because its
automated tests check both the new argument cases and the existing no-argument
behavior, making the behavior repeatable to verify. The manual change was
straightforward and easy to inspect, but its validation was a direct run of the
demo rather than a test suite. Both approaches were simple; the tests provide
stronger evidence that the AI branch behaves as specified and avoids a
regression.
