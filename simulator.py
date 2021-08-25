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
behaviour_map_e1 = [
    "q0 b 0 d q1",
    "q1 b 1 d q0",
]
behaviour_map_e2 = [
    "q0 b 1 d q1",
    "q0 t 1 d q0",
    "q0 0 0 d q0",
    "q0 1 1 d q0",
    "q1 t 1 d q1",
    "q1 0 0 d q1",
    "q1 1 1 d q1",
    "q1 b 0 d q2",
    "q2 b b i q2",
    "q2 1 1 i q2",
    "q2 0 0 i q3",
    "q3 t t i q3",
    "q3 1 t d q4",
    "q4 t t d q4",
    "q4 0 0 d q4",
    "q4 1 1 d q4",
    "q4 b 1 d q2",
    "q3 b b d q0",
    "q3 0 0 d q0",
]

initial_state = 'q0'
program = 'bbbb'
behaviour_map = behaviour_map_e2

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