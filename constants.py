
algorithms = ["Deutsch-Josza","Bernstein-Vazirani"]

experiments = ["Bell State - Hello World", "Superposition with one Qubit", "Superposition with three Qubits", "Interference"]

acceptable_execution_inputs = ['0', '1', '2', '3']

acceptable_algorithm_inputs = ['0', '1']

acceptable_experiment_inputs = ['0', '1', '2', '3']

input_message_1 = "Choose an Algorithm: " \
                  "\n0 for Deutsch-Josza." \
                  "\n1 for Bernstein-Vazirani" \
                  "\nYour input:"

input_message_2 = "Enter:" \
                "\n0 for execution on the Local Device Simulator." \
                "\n1 for execution on the Qasm simulator." \
                "\n2 for execution on a real device." \
                "\n3 for execution on the local device and real device!" \
                "\nYour input:"
cards = ["H", "H", "X", "X", "CX", "SX", "SXDG"]

acceptable_choice_inputs = ["E", "A"]
