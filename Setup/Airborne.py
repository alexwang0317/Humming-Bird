# Serial Port connection was used. Specifically /dev/ttyS0 with a baud rate of 57600

import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

async def run():
    # Initialize the drone and connect via serial port
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyS0:57600")  

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break

    # Arm the drone -> This basically means that the drone's rotos/motors actually are on. 
    print("Arming the drone...")
    await drone.action.arm()

    # Take off and reach 1 meter altitude
    print("Taking off...")
    await drone.action.takeoff()
    await asyncio.sleep(5)  # Wait for the drone to take off

    # Fly to 1 meter altitude
    print("Flying to 1 meter altitude...")
    async for position in drone.telemetry.position():
        if position.relative_altitude_m >= 1.0:
            print(f"Reached 1 meter altitude: {position.relative_altitude_m} meters")
            break

    # Hover at the current position for 10 seconds
    print("Hovering...")
    await asyncio.sleep(10)

    # Land the drone
    print("Landing...")
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())

