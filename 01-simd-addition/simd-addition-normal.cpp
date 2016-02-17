#include <random>
#include <limits>
#include <stdint.h>
#include <iostream>

#include "benchmark/benchmark.h"

#include "common.h"

using std::uniform_int_distribution;
using std::default_random_engine;
using std::numeric_limits;

const unsigned int minRange = 2U << 1;
const unsigned int maxRange = 2U << 16;

namespace {
template<typename ActualType, typename SimdType>
void add(const ActualType* const input1, const ActualType* const input2, ActualType* const output, size_t actualSize) {
		const size_t nbOfSimdIterations = actualSize * sizeof(ActualType)/sizeof(SimdType);

		const SimdType* const simd_input1 = reinterpret_cast<const SimdType* const>(input1);
		const SimdType* const simd_input2 = reinterpret_cast<const SimdType* const>(input2);
		SimdType* const simd_output = reinterpret_cast<SimdType* const>(output);

		for(auto i = 0; i < nbOfSimdIterations; ++i) {
			simd_output[i] = simd_input1[i] + simd_input2[i];
		}
	}
}

static void SimdAdditionNormal(benchmark::State& state) {
	while(state.KeepRunning()) {
		state.PauseTiming();

		default_random_engine generator;
		uniform_int_distribution<int> distribution(0, numeric_limits<uint8_t>::max());
		const size_t nbOfElements = state.range_x();

		uint8_t input1[nbOfElements];
		for(auto& element : input1) {
			element = distribution(generator);
		}

		uint8_t input2[nbOfElements];
		for(auto& element : input2) {
			element = distribution(generator);
		}

		uint8_t output[nbOfElements];
		state.ResumeTiming();
		for(size_t i = 0; i < nbOfElements; ++i) {
			output[i] = input1[i] + input2[i];
		}
		state.PauseTiming();
		Common::forceUseOfVariable(output[0]);
		Common::forceUseOfVariable(output[nbOfElements-1]);
	}
}
BENCHMARK(SimdAdditionNormal)->Range(minRange, maxRange);

static void SimdAdditionForceSimd(benchmark::State& state) {
	while(state.KeepRunning()) {
		state.PauseTiming();
		default_random_engine generator;
		uniform_int_distribution<int> distribution(0, numeric_limits<uint8_t>::max());
		const size_t nbOfElements = state.range_x();

		uint8_t input1[nbOfElements];
		for(auto& element : input1) {
			element = distribution(generator);
		}

		uint8_t input2[nbOfElements];
		for(auto& element : input2) {
			element = distribution(generator);
		}

		uint8_t output[nbOfElements];
		state.ResumeTiming();
	
		add<uint8_t,uint32_t>(input1, input2, output, nbOfElements); 
		state.PauseTiming();

		Common::forceUseOfVariable(output[0]);
		Common::forceUseOfVariable(output[nbOfElements-1]);
	}
}
BENCHMARK(SimdAdditionForceSimd)->Range(minRange, maxRange);

BENCHMARK_MAIN();
