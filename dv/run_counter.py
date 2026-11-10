"""Lance le test cocotb du compteur avec Verilator."""
from pathlib import Path
try:
    from cocotb_tools.runner import get_runner   # cocotb 2.x
except ImportError:
    from cocotb.runner import get_runner         # cocotb 1.9

root = Path(__file__).resolve().parent.parent
runner = get_runner("verilator")
runner.build(sources=[root / "rtl" / "counter.sv"], hdl_toplevel="counter",
             build_dir=root / "dv" / "build", always=True, waves=True)
runner.test(hdl_toplevel="counter", test_module="test_counter",
            test_dir=root / "dv", build_dir=root / "dv" / "build")
