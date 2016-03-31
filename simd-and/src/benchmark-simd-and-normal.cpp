#include "benchmark-simd-and.h"

namespace SimdAnd {
	namespace Performance {
		static void SimdAndNormal(benchmark::State& state) {
			const size_t nbOfElements = state.range_x();
			simdAnd_t input1[nbOfElements];
			simdAnd_t input2[nbOfElements];
			Common::randomInput(input1, input2, nbOfElements);

			uint8_t output[nbOfElements];
			while(state.KeepRunning()) {
				simdAnd(input1, input2, output, nbOfElements);
				if(unlikely(performanceUtils::alwaysReturnFalse())) {
					performanceUtils::forceUseOfVariable(output);
				}
			}
		}
		BENCHMARK(SimdAndNormal)->Range(minRange, maxRange);
    }
}

