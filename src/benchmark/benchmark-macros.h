#ifndef __BENCHMARK_MACROS_H__
#define __BENCHMARK_MACROS_H__

#include "benchmark/benchmark.h"

#define TEMPLATED_BENCHMARK(T,S,N) \
    BENCHMARK_PRIVATE_DECLARE(S) =                               \
        (::benchmark::internal::RegisterBenchmarkInternal(       \
            new ::benchmark::internal::FunctionBenchmark(N, T<S>)))

#define TEMPLATED_BENCHMARK_UNNAMED(T,S) TEMPLATED_BENCHMARK_NAMED(T,S,#S)

#endif
