#include "benchmark-simd-and.h"
#include "performanceUtils.h"

namespace SimdAnd {
    namespace Performance {
        TEMPLATED_BENCHMARK(BenchmarkSimdAnd<simdAnd_t>::run, simdAndForceNormal, "Simdand::ForceNormal")->Range(minRange, maxRange);
    }
}
