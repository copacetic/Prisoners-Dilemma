import socket


COMMAND_SIZE = 1          # String length for a command
MAX_BACKLOG_LENGTH = 2    # Max clients to have backed up
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
RAT, SHUTUP = 0, 1
MAX_PENALTY = 10
MED_PENALTY = 3
MIN_PENALTY = 0


# given two play codes returns a tuple of outcomes
# for each player
def solve_outcome(move0_val, move1_val):
    if move0_val == RAT:
        if move1_val == RAT:
            return (MAX_PENALTY, MAX_PENALTY)
        else:
            return (MIN_PENALTY, MAX_PENALTY)
    else:
        if move1_val == RAT:
            return (MAX_PENALTY, MIN_PENALTY)
        else:
            return (MED_PENALTY, MED_PENALTY)

def disconnect_clients(clients):
    for client in clients:
        client.close()

if __name__ == "__main__":
    clients = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(MAX_BACKLOG_LENGTH)
    num_connected = 0          

    # Wait for two clients
    while num_connected != 2:
        conn, addr = s.accept()
        clients.append(conn)
        print 'Connected by', addr
        num_connected += 1

    client0 = clients[0]
    client1 = clients[1]

    # Take in their commands
    move0 = client0.recv(COMMAND_SIZE)
    move1 = client1.recv(COMMAND_SIZE)

    isValid = lambda action: not ((action > SHUTUP) and (action < RAT))
    
    # Sanity check commands
    #if (len(move0) != 1) or (len(move1) != 1):
    #    print("Invalid move size")
    #else:
    move0_val = int(move0[0])
    move1_val = int(move1[0])
    
    if (isValid(move0_val)) and (isValid(move1_val)):
        outcome = solve_outcome(move0_val, move1_val)
    
    print "Player 0 got ", outcome[0]
    print "Player 1 got ", outcome[1]
    client0.sendall(str(outcome))
    client1.sendall(str(outcome))

    disconnect_clients(clients)
    num_connected = 0
    s.close()
