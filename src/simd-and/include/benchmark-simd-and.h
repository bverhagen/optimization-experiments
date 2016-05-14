#include "benchmark/benchmark.h"

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
    }
}
