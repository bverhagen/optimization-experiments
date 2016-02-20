#include "benchmark/benchmark.h"

#include "targetSpecific.h"
#include "performanceUtils.h"
#include "randomInput.h"
#include "simd-and.h"

namespace SimdAnd {
	namespace Performance {
		typedef uint8_t simdAnd_t;
		const unsigned int minRange = 1U << 3;		// We need to be sure that register_type_t/simdAnd_t >= minRange
		const unsigned int maxRange = 1U << 12;

		static void SimdAndNormal(benchmark::State& state) {
			const size_t nbOfElements = state.range_x();
			simdAnd_t input1[nbOfElements];
			simdAnd_t input2[nbOfElements];
			Common::randomInput(input1, input2, nbOfElements);

			uint8_t output[nbOfElements];
			while(state.KeepRunning()) {
				simdAndNormal(input1, input2, output, nbOfElements);
				performanceUtils::forceUseOfVariable(output[0]);
				performanceUtils::forceUseOfVariable(output[nbOfElements-1]);
			}
		}
		BENCHMARK(SimdAndNormal)->Range(minRange, maxRange);

		static void SimdAndForceRegisterSimd(benchmark::State& state) {
			const size_t nbOfElements = state.range_x();
			simdAnd_t input1[nbOfElements];
			simdAnd_t input2[nbOfElements];
			Common::randomInput(input1, input2, nbOfElements);

			uint8_t output[nbOfElements];
			while(state.KeepRunning()) {
			simdAndForceRegisterSimd<simdAnd_t, unsigned_register_t>(input1, input2, output, nbOfElements);
				performanceUtils::forceUseOfVariable(output[0]);
				performanceUtils::forceUseOfVariable(output[nbOfElements-1]);
			}
		}
		BENCHMARK(SimdAndForceRegisterSimd)->Range(minRange, maxRange);
	}
}

BENCHMARK_MAIN();
