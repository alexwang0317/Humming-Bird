# This script will continuously print out a drone's altitude, yaw, and other telemetry values. Important first step in order
# to test the initial components of the working drone and connection between Pixhawk 6C and Raspberry Pi. 


import asyncio
from mavsdk import System

async def run():
    drone = System()

    # These were just the serial ports and baud rate that I specifically used. 
    await drone.connect(system_address="serial:///dev/ttyS0:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    print("Fetching telemetry data...")

    async for position in drone.telemetry.position():
        altitude = position.relative_altitude_m  # Altitude above the takeoff point
        latitude = position.latitude_deg
        longitude = position.longitude_deg
        print(f"Altitude: {altitude:.2f} meters, Latitude: {latitude:.6f}, Longitude: {longitude:.6f}")

    async for attitude in drone.telemetry.attitude():
        yaw = attitude.yaw_deg  # Yaw in degrees
        pitch = attitude.pitch_deg
        roll = attitude.roll_deg
        print(f"Yaw: {yaw:.2f} degrees, Pitch: {pitch:.2f} degrees, Roll: {roll:.2f} degrees")

if __name__ == "__main__":
    asyncio.run(run())
