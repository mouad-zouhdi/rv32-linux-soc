#!/usr/bin/env bash
# Lint de tout le RTL avec Verible
cd "$(dirname "$0")/.." && verible-verilog-lint --rules_config_search rtl/*.sv
