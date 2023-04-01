```mermaid
sequenceDiagram
    participant code
    participant machine
    participant tank
    participant engine
    code->>machine: Machine()
    machine->>tank: FuelTank()
    machine->>tank: fill(40)
    machine->>engine: Engine(tankki)
    code->>machine: drive()
    machine->>engine: start()
    engine->>tank: consume(5)
    machine->>engine: is_running()
    engine->>machine: True
    machine->>engine: use_energy()
    engine->>tank: consume(10)

