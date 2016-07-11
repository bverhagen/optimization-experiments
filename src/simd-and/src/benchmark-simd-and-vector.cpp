#include "benchmark-simd-and.h"

#include <iostream>
#include "common/include/performanceUtils.h"

using std::size_t;

namespace SimdAnd {
    namespace Performance {
        TEMPLATED_BENCHMARK(BenchmarkSimdAnd<v4uint8_t>::run, simdAnd, "SimdAnd::vectorized")->Range(minVectorRange, maxRange);
    }   // namespace Performance
}   // namespace SimdAnd
