#include "benchmark-simd-and.h"

#include <iostream>
#include "common/include/performanceUtils.h"

using std::size_t;

namespace SimdAnd {
namespace Performance {
    static void SimdAndVector(benchmark::State& state) {
        const size_t nbOfElements = state.range_x() * sizeof(uint8_t) / sizeof(v4uint8_t);
        v4uint8_t input1[nbOfElements];
        v4uint8_t input2[nbOfElements];
        v4uint8_t output[nbOfElements];

        Common::randomInput(state.range_x(), input1, input2);

        while(state.KeepRunning()) {
            simdAnd(input1, input2, output, nbOfElements);
            performanceUtils::doNotOptimize(output);
        }
    }
    BENCHMARK(SimdAndVector)->Range(minVectorRange, maxRange);
}   // namespace Performance
}   // namespace SimdAnd
