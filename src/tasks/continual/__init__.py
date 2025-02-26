from box import Box
import pprint

def execute(config: Box):
    strategy = config.parallelization_strategy
    if strategy == "fsdp":
        # Import the Fabric class and its dependencies
        from src.tasks.continual.fabric.fsdp.fsdp import setup
        devices = config.devices
        resume = config.resume
        setup(devices, config, resume)
    elif strategy == "ddp":
        # TODO: Implement DDP
        raise NotImplementedError("Distributed Data Parallel (DDP) is not yet implemented.")
    else:
        raise ValueError(f"Invalid parallelization strategy: {strategy}")
    pass