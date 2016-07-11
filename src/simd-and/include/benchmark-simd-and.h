#ifndef __BENCHMARKSIMDAND_H__
#define __BENCHMARKSIMDAND_H__

#include "benchmark-macros.h"

#include "targetSpecific.h"
#include "performanceUtils.h"
#include "randomInput.h"
#include "simd-and.h"

namespace SimdAnd {
	namespace Performance {
		typedef uint8_t simdAnd_t;
		const size_t minRange = 1U << 4;
		const size_t minVectorRange = BIGGEST_ALIGNMENT;		// We need to be sure that minRage is bigger than the smallest vector size we use
		const size_t maxRange = minVectorRange << 16;

        template<typename T>
        class BenchmarkSimdAnd {
            public:
                typedef void(*simdAndCallBack)(const T* const, const T* const, T* const, size_t);

                template<simdAndCallBack F>
                static void run(benchmark::State& state) {
                    const size_t nbOfElements = state.range_x() * sizeof(uint8_t) / sizeof(T);
                    T input1[nbOfElements];
                    T input2[nbOfElements];
                    Common::randomInput(nbOfElements, input1, input2);

                    T output[nbOfElements];
                    while(state.KeepRunning()) {
                        F(input1, input2, output, nbOfElements);
                        performanceUtils::doNotOptimize(output);
                    }
                }
        };
    }
}

#endif
