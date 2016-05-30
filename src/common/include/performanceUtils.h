#ifndef __PERFORMANCEUTILS_H__
#define __PERFORMANCEUTILS_H__

#include <cstdint>
#include "benchmark/benchmark.h"

namespace performanceUtils
{
    bool alwaysReturnFalse(void) noexcept;

    template<typename T> 
    inline void doNotOptimize(T& var) noexcept {
        benchmark::DoNotOptimize(var);
    }

    // Override for arrays: does not compile with the above.
    template<typename T> 
    inline void doNotOptimize(T* var) noexcept {
        asm volatile("" : "+rm" (var));
    }
}

#endif
