import time

import async_IO
import sync_IO
import async_token_gen
import sync_token_gen


def do_tests(test, repeats, *arg):
    start_time = time.perf_counter_ns()
    for i in range(repeats):
        test(*arg)
    end_time = time.perf_counter_ns()
    return (end_time-start_time)/repeats


def link_tests():
    #print(f'Sync time {do_tests(sync_IO.test, 1)}')

    workers = 5
    #print(f'Async with {workers} max_workers time {do_tests(async_IO.test, 5, workers)}')

    workers = 10
    #print(f'Async with {workers} max_workers time {do_tests(async_IO.test, 5, workers)}')

    workers = 100
    #print(f'Async with {workers} max_workers time {do_tests(async_IO.test, 5, workers)}')


def token_test():
    #print(f'Sync time {do_tests(sync_token_gen.test, 1, 10)}')

    workers = 2
    #print(f'Async with {workers} max_workers time {do_tests(async_token_gen.test, 5, 10, workers)}')

    workers = 4
    print(f'Async with {workers} max_workers time {do_tests(async_token_gen.test, 5, 10, workers)}')

    workers = 5
    print(f'Async with {workers} max_workers time {do_tests(async_token_gen.test, 5, 10, workers)}')

    workers = 10
    print(f'Async with {workers} max_workers time {do_tests(async_token_gen.test, 5, 10, workers)}')

    workers = 61
    print(f'Async with {workers} max_workers time {do_tests(async_token_gen.test, 5, 10, workers)}')


if __name__ == '__main__':
    link_tests()
    token_test()
