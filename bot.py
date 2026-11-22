import socket
from datetime import datetime

HOST = "BattlePlayzz.aternos.me"
PORT = 36551

def check_server():
    print("\n===== BATTLEPLAYZZ SMP =====")
    print("Time:", datetime.now())

    try:
        connection = socket.create_connection(
            (HOST, PORT), timeout=10
        )
        connection.close()

        print("Status: ONLINE")
        print("Server:", HOST)
        print("Port:", PORT)

    except OSError:
        print("Status: OFFLINE or UNREACHABLE")

    print("============================")

if __name__ == "__main__":
    check_server()
