program_1_1 = 'aaaaa'
program_1_2 = 'aaaba'

program_2_1 = '00011'
program_2_2 = '000101'

behaviour_map_1 = [
    "q0 a a d q0",
    "q0 b b d q1"
]

behaviour_map_2 = [
    "q0 0 x d q1",
    "q0 y y d q3",
    "q1 0 0 d q1",
    "q1 y y d q1",
    "q1 1 y i q2",
    "q2 0 0 i q2",
    "q2 y y i q2",
    "q2 x x d q0",
    "q3 y y d q3",
    "q3 b b d q4",
]

initial_state = 'q0'
program = program_2_2
behaviour_map = behaviour_map_2

def print_tape(tape, state, pos):
    l = min(tape.keys())
    r = max(tape.keys())
    output = []
    for i in range(l, r+1):
        output.append(tape[i])
    print((''.join([' ']*(pos-l)))+'v')
    print(''.join(output), state)

def simulate():
    pos = 0
    tape = {}
    state = initial_state
    visited_superstates = set()

    for i, c in enumerate(program):
        tape[i] = c

    behaviour = {}
    for s in behaviour_map:
        a = s.split()
        input_state = (a[0], a[1])
        action = (a[2], a[3], a[4])
        behaviour[input_state] = action

    print_tape(tape, state, pos)
    while True:
        input()
        read_val = 'b'
        if pos in tape.keys():
            read_val = tape[pos]

        input_state = (state, read_val)
        if input_state not in behaviour:
            print('No transfer function defined')
            break
        write_val, shift, next_state = behaviour[input_state]
        tape[pos] = write_val
        if shift == 'd':
            pos += 1
        elif shift == 'i':
            pos -= 1
        else:
            print('Invalid move command', shift)
            break
        state = next_state
        print_tape(tape, state, pos)
        
        superstate = (state, tuple(list(tape.items())), pos)
        if superstate in visited_superstates:
            print('Loop detected!')
            break
        visited_superstates.add(superstate)
         
if __name__ == '__main__':
    simulate()