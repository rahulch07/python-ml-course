# from contextlib import contextmanager
# import time


# class CMF:

#     def __enter__(self):
#         print("Sarted")
#         self.start = time.perf_counter()
#         print(f"Started at: {time.perf_counter()}")
#         return self


#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"Total time taken: {time.perf_counter() - self.start}")
#         print("Ended")

#     # @contextmanager
#     # def timer():
#     #     start = time.perf_counter()
#     #     try:
#     #         yield
#     #     finally:
#     #         print(f"Total time taken: {time.perf_counter() - start}")

# with CMF() as obj:
#     print("Hello")
#     for _ in range(1, 10000000): ...


fileName = input("Enter file name: ") # should be at root(from where code is being run)

with open(fileName, "r+t") as file:
    while True:
        line = input("> ")
        if line.strip() == "": break
        file.write(line + "\n")

print("Reading File:")
with open(fileName, "rt") as file:
    for line in file:
        print(line, end="")
print()