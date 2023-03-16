import numpy as np

EXAMPLE_START = 1
EXAMPLE_END = 100


class ExampleNum:
    counter = 0

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        self.counter += 1
        if EXAMPLE_START <= self.counter <= EXAMPLE_END:
            print(f'\nExample #{self.counter}:\n')
            return self._func(*args, **kwargs)


@ExampleNum
def sp_print(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == "__main__":
    sp_print(np.array(range(10), dtype='float32'))

    sp_print(np.array([range(i, i+3) for i in range(2, 8, 2)]))

    sp_print(np.zeros(10))

    sp_print(np.ones((3, 5)))

    sp_print(np.full((2, 3), 3.14))

    sp_print(np.arange(-3, 15, 3))

    sp_print(np.linspace(2, 5, 6))

    sp_print(np.random.random((4, 4)))

    sp_print(np.random.normal(0.5, 1, (4, 4)))

    array1 = np.random.randint(0, 100, (4, 4))
    sp_print(array1)

    sp_print(np.eye(4))

    sp_print(array1)
    array2 = array1[:2, 2:]
    sp_print(array2)
    sp_print(array1[:, 0])
    sp_print(array1[0, :])
    sp_print(array1[0])

    array2[0, 0] = 99
    sp_print(array1)

    array3 = array1[:2, 2:].copy()
    array3[0, 0] = 100
    sp_print(array3)
    sp_print(array1)

    sp_print(np.arange(1, 17).reshape((4, 4)))

    sp_print(np.arange(1, 5)[:, np.newaxis])

    array4 = np.arange(1, 9).reshape((2, 4))
    array5 = np.arange(9, 17).reshape((2, 4))
    sp_print(array4, array5)
    sp_print(np.concatenate([array4, array5]))
    sp_print(np.concatenate([array4, array5], axis=1))

    array6 = np.arange(17, 21)
    sp_print(array4)
    sp_print(array6)

    sp_print(np.vstack([array4, array6]))

    array7 = np.arange(30, 40).reshape((2, 5))
    sp_print(array4)
    sp_print(array7)
    sp_print(np.hstack([array4, array7]))