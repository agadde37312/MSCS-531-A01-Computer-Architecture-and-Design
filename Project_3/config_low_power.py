# config_low_power.py
from m5.objects import *
import m5

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]
system.membus = SystemXBar()

system.cpu = DerivO3CPU()
system.cpu.numThreads = 4

system.cpu.icache = L1ICache(size='32kB')
system.cpu.dcache = L1DCache(size='32kB')
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

system.l2bus = L2XBar()
system.l2cache = L2Cache(size='256kB')
system.l2cache.connectCPUSideBus(system.l2bus)
system.cpu.connectAllPorts(system.l2bus)
system.l2cache.connectMemSideBus(system.membus)

system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

system.workload = SEWorkload.init_compatible('tests/test-progs/hello/bin/x86/linux/hello')

root = Root(full_system=False, system=system)
m5.instantiate()

print("Starting Low-Power Simulation...")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")
