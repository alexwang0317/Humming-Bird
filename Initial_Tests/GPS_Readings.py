import asyncio
from mavsdk import System

async def run():
    drone = System()

    # Connect to the drone via the specified serial port and baud rate.
    await drone.connect(system_address="serial:///dev/ttyS0:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    print("Fetching GPS data...")

    async for gps_info in drone.telemetry.gps_info():
        num_satellites = gps_info.num_satellites
        fix_type = gps_info.fix_type
        print(f"GPS: {num_satellites} satellites, Fix type: {fix_type}")

    async for position in drone.telemetry.position():
        latitude = position.latitude_deg
        longitude = position.longitude_deg
        absolute_altitude = position.absolute_altitude_m  # Altitude above mean sea level
        print(f"Latitude: {latitude:.6f}, Longitude: {longitude:.6f}, Altitude: {absolute_altitude:.2f} meters")

    async for ground_speed in drone.telemetry.ground_speed_ned():
        velocity_north = ground_speed.velocity_north_m_s  # Speed in the North direction (m/s)
        velocity_east = ground_speed.velocity_east_m_s    # Speed in the East direction (m/s)
        velocity_down = ground_speed.velocity_down_m_s    # Speed in the Down direction (m/s)
        ground_speed_total = (velocity_north**2 + velocity_east**2)**0.5  # Total ground speed
        print(f"Ground Speed: {ground_speed_total:.2f} m/s (N: {velocity_north:.2f}, E: {velocity_east:.2f}, D: {velocity_down:.2f})")

if __name__ == "__main__":
    asyncio.run(run())
