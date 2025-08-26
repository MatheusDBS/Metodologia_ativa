import time

def main():
    start_time = time.time()
    for _ in range(50):
        buffer = [[0 for _ in range(4096)] for _ in range(4096)]
        for i in range(4096):
            for j in range(4096):
                buffer[i][j] = (i + j) % 256
    end_time = time.time()
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")

if __name__ == "__main__":
    main()
