#!/bin/bash
autopep8 . --recursive --in-place --aggressive --aggressive
pylint hwamsmartctrl
