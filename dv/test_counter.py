import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def compte_et_remise_a_zero(dut):
    cocotb.start_soon(Clock(dut.clk_i, 10, unit="ns").start())
    dut.en_i.value = 0
    dut.rst_ni.value = 0
    for _ in range(3):
        await RisingEdge(dut.clk_i)
    dut.rst_ni.value = 1
    dut.en_i.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk_i)
    await RisingEdge(dut.clk_i)
    await Timer(1, unit="ns")
    assert int(dut.count_o.value) == 6, f"attendu 6, obtenu {int(dut.count_o.value)}"
