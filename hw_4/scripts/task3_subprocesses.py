import multiprocessing
import time
import codecs
import datetime


def process_a(input_queue, to_b_conn):
    while True:
        msg = input_queue.get()
        if msg == "STOP":
            to_b_conn.send(msg)
            break
        modified_msg = msg.lower()
        to_b_conn.send(modified_msg)
        time.sleep(5)

def process_b(from_a_conn, stop_signal_queue):
    while True:
        msg = from_a_conn.recv()
        if msg == "STOP":
            stop_signal_queue.put("STOP")
            break
        #Шифр цезаря?
        encoded_msg = codecs.encode(msg, 'rot_13')
        current_time = datetime.datetime.now()
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time_str}] Processed message: {encoded_msg}")

if __name__ == "__main__":
    input_queue = multiprocessing.Queue()
    stop_signal_queue = multiprocessing.Queue()
    a_to_b, b_to_a = multiprocessing.Pipe()

    p_a = multiprocessing.Process(target=process_a, args=(input_queue, a_to_b))
    p_b = multiprocessing.Process(target=process_b, args=(b_to_a, stop_signal_queue))
    p_a.start()
    p_b.start()

    try:
        while True:
            current_time = datetime.datetime.now()
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            user_input = input(f"[{time_str}] Enter a message (type 'exit' to stop): ")
            if user_input.lower() == 'exit':
                input_queue.put("STOP")
                break
            input_queue.put(user_input)

        stop_confirmation = stop_signal_queue.get()
        if stop_confirmation == "STOP":
            print("Shutting down...")
    finally:
        p_a.join()
        p_b.join()
