#!/bin/bash

set -e

CONFIG_KEY="$1"
THREADS="$2"
N="$3"
REPEAT="$4"

if [ -z "$CONFIG_KEY" ] || [ -z "$THREADS" ] || [ -z "$N" ] || [ -z "$REPEAT" ]; then
  echo "Usage: $0 <config_key> <threads> <N> <repeat>"
  echo "config_key options: op1_iss6 op2_iss5 op3_iss4 op4_iss3 op5_iss2 op6_iss1"
  exit 1
fi

export GEM5_FLOATSIMD_CONFIG="$CONFIG_KEY"

RUN_DIR="run_${CONFIG_KEY}_threads${THREADS}_N${N}_r${REPEAT}_$(date +%Y%m%dT%H%M%S)"
mkdir -p "$RUN_DIR"
echo "Running gem5 with config=$CONFIG_KEY threads=$THREADS N=$N repeat=$REPEAT => output in $RUN_DIR"

# Path to gem5 binary & compiled daxpy - adjust these paths before running
GEM5_BIN="/path/to/gem5/build/X86/gem5.opt"
SE_SCRIPT="/path/to/gem5/configs/example/se.py"
DA_XPY_BIN="/path/to/daxpy_multithreaded"  # compile and place binary here

"$GEM5_BIN" "$SE_SCRIPT" -c "$DA_XPY_BIN" --argv="$N $THREADS $REPEAT" --cpu-type=MinorCPU --num-cpus="$THREADS" --mem-size=4GB > "$RUN_DIR/gem5_stdout.txt" 2>&1

echo "Run finished. Stats (if any) are in $RUN_DIR/m5out/stats.txt or $RUN_DIR/m5out"
