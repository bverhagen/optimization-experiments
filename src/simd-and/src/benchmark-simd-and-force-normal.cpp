#include "benchmark-simd-and.h"
#include "performanceUtils.h"

namespace SimdAnd {
    namespace Performance {
        static void SimdAndForceNormal(benchmark::State& state) {
            const size_t nbOfElements = state.range_x();
            simdAnd_t input1[nbOfElements];
            simdAnd_t input2[nbOfElements];
            Common::randomInput(input1, input2, nbOfElements);

            uint8_t output[nbOfElements];
            while(state.KeepRunning()) {
                simdAndForceNormal(input1, input2, output, nbOfElements);
                performanceUtils::doNotOptimize(output);
            }
        }
        BENCHMARK(SimdAndForceNormal)->Range(minRange, maxRange);
    }
}
