#include "benchmark-simd-and.h"
#include "performanceUtils.h"

namespace SimdAnd {
    namespace Performance {
        TEMPLATED_BENCHMARK(BenchmarkSimdAnd<simdAnd_t>::run, simdAnd, "Simdand::Normal")->Range(minRange, maxRange);
    }
}

