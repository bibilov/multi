import time

import ppe_token_generator_test
import sync_link_test, tpe_link_test
import sync_token_generator_test


def perform_test(test, repeats, *arg):
    start_time = time.perf_counter_ns()
    for i in range(repeats):
        test(*arg)
    end_time = time.perf_counter_ns()
    return (end_time-start_time)/repeats


def links_tests():
    print(f'Sync time {perform_test(sync_link_test.test, 1)}')

    workers = 5
    print(f'TPE with {workers} max_workers time {perform_test(tpe_link_test.test, 5, workers)}')

    workers = 10
    print(f'TPE with {workers} max_workers time {perform_test(tpe_link_test.test, 5, workers)}')

    workers = 100
    print(f'TPE with {workers} max_workers time {perform_test(tpe_link_test.test, 5, workers)}')


def tokens_tests():
    #print(f'Sync time {perform_test(sync_token_generator_test.test, 1, 10)}')

    workers = 2
    #print(f'TPE with {workers} max_workers time {perform_test(ppe_token_generator_test.test, 5, 10, workers)}')

    workers = 4
    #print(f'TPE with {workers} max_workers time {perform_test(ppe_token_generator_test.test, 5, 10, workers)}')

    workers = 5
    #print(f'TPE with {workers} max_workers time {perform_test(ppe_token_generator_test.test, 5, 10, workers)}')

    workers = 10
    #print(f'TPE with {workers} max_workers time {perform_test(ppe_token_generator_test.test, 5, 10, workers)}')

    workers = 61
    print(f'TPE with {workers} max_workers time {perform_test(ppe_token_generator_test.test, 1, 10, workers)}')

if __name__ == '__main__':
    tokens_tests()
