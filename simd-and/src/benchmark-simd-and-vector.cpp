#include "benchmark-simd-and.h"

using std::size_t;

namespace SimdAnd {
	namespace Performance {
        static void SimdAndVector(benchmark::State& state) {
			const size_t nbOfElements = state.range_x() * sizeof(uint8_t) / sizeof(v4uint8_t);
			v4uint8_t input1[nbOfElements];
			v4uint8_t input2[nbOfElements];
			Common::randomInput((uint8_t*) input1, (uint8_t*) input2, state.range_x());

			v4uint8_t output[nbOfElements];
			while(state.KeepRunning()) {
				simdAnd(input1, input2, output, nbOfElements);
				if(unlikely(performanceUtils::alwaysReturnFalse())) {
					performanceUtils::forceUseOfVariable(output);
				}
			}
		}
		BENCHMARK(SimdAndVector)->Range(minVectorRange, maxRange);
    }
}
