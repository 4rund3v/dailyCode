"""
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”
"""

def read7(file_name):
    with open(file_name, 'r') as fp:
        chunk = fp.read(7)
        while chunk:
            yield chunk
            chunk = fp.read(7)


def readN(file_name, buffer_n):
    buffer = ""
    data = read7(file_name)
    temp = next(data)
    while temp:
        if buffer:
            temp = buffer+temp
            buffer = ''
        if  len(temp) < buffer_n:
            to_print = temp
            temp = next(data)
            if temp:
                if len(temp) > buffer_n - len(to_print):
                    to_print += temp[:buffer_n - len(to_print)]
                    buffer = temp[buffer_n - len(to_print)]
        print('$'+ to_print + '$')
        temp = next(data)
        # TODO , success when greater, when buffer small to handle

if __name__ == "__main__":
    file_name = "problem1.py"
    print(readN(file_name, 10))
    pass
