#include <iostream>

#include "benchmark/benchmark.h"

#include "targetSpecific.h"
#include "performanceUtils.h"
#include "randomInput.h"
#include "simd-and.h"

using TargetSpecific::unsigned_register_t;
using std::size_t;

namespace SimdAnd {
	namespace Performance {
		typedef uint8_t simdAnd_t;
		const size_t minRange = 1U << 4;
		const size_t minVectorRange = BIGGEST_ALIGNMENT;		// We need to be sure that minRage is bigger than the smallest vector size we use
		const size_t maxRange = minVectorRange << 16;

		static void SimdAndNormal(benchmark::State& state) {
			const size_t nbOfElements = state.range_x();
			simdAnd_t input1[nbOfElements];
			simdAnd_t input2[nbOfElements];
			Common::randomInput(input1, input2, nbOfElements);

			uint8_t output[nbOfElements];
			while(state.KeepRunning()) {
				simdAndNormal(input1, input2, output, nbOfElements);
				if(performanceUtils::alwaysReturnFalse()) {
					performanceUtils::forceUseOfVariable(output[0]);
					performanceUtils::forceUseOfVariable(output[nbOfElements-1]);
				}
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
				if(performanceUtils::alwaysReturnFalse()) {
					performanceUtils::forceUseOfVariable(output[0]);
					performanceUtils::forceUseOfVariable(output[nbOfElements-1]);
				}
			}
		}
		BENCHMARK(SimdAndForceRegisterSimd)->Range(minRange, maxRange);

		static void SimdAndVector(benchmark::State& state) {
			const size_t nbOfElements = state.range_x() * sizeof(uint8_t) / sizeof(v4uint8_t);
			v4uint8_t input1[nbOfElements];
			v4uint8_t input2[nbOfElements];
			Common::randomInput((uint8_t*) input1, (uint8_t*) input2, state.range_x());

			v4uint8_t output[nbOfElements];
			while(state.KeepRunning()) {
				simdAndVector(input1, input2, output, nbOfElements);

				if(performanceUtils::alwaysReturnFalse()) {
					performanceUtils::forceUseOfVariable(output[0]);
					performanceUtils::forceUseOfVariable(output[nbOfElements-1]);
				}
			}
		}
		BENCHMARK(SimdAndVector)->Range(minVectorRange, maxRange);

	}
}

BENCHMARK_MAIN();
