import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        # Broadcast the received message to all connected clients
        await asyncio.gather(
            *[client.send(message) for client in clients]
        )

async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("WebSocket server started...")
    await server.wait_closed()

clients = set()

if __name__ == "__main__":
    asyncio.run(main())
