#!/bin/bash
# run_low_power.sh

GEM5_BIN=/path/to/gem5/build/X86/gem5.opt
CONFIG=config_low_power.py
WORKLOAD=/path/to/daxpy_low_power.py

$GEM5_BIN $CONFIG --cmd=$WORKLOAD > gem5_low_power_output.txt 2>&1

echo "Simulation completed. Check gem5_low_power_output.txt for results."
