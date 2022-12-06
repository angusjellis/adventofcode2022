def get_start_of_packet_marker(signal: str, num: int) -> int:
    i = 0
    while len(set(signal[:num])) != num:
        signal = signal[1:]
        i += 1
    return(i+num)
    

with open("./day6/input.txt", "r") as input_file:
    signal = input_file.read().strip()
    print(get_start_of_packet_marker(signal, 4))
    print(get_start_of_packet_marker(signal, 14))