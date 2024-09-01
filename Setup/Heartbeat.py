import asyncio
from mavsdk import System

async def run():
    # Create a new System instance and connect it via serial port
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyS0:57600")

    # Wait for the drone to be connected
    print("Waiting for the drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    # Subscribe to heartbeat messages and print them
    async for heartbeat in drone.telemetry.health():
        print(f"Heartbeat: {heartbeat}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
