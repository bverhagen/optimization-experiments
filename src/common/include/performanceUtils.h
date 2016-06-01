#ifndef __PERFORMANCEUTILS_H__
#define __PERFORMANCEUTILS_H__

#include <cstdint>
#include "benchmark/benchmark.h"

namespace performanceUtils
{

    void forceUseOfVariableVoid(void* var) noexcept;             // Force the fake use of the variable to be hidden in a separate compilation unit

    template<typename T> 
    inline void doNotOptimize(T& var) noexcept {
        benchmark::DoNotOptimize(var);
    }

    // Override for arrays: does not compile with the above.
    template<typename T> 
    inline void doNotOptimize(T* var) noexcept {
        // Implementation borrowed from benchmark and adapted apropriately
#if defined(__clang__) && defined(__GNUC__)
        asm volatile("" : "+m" (var));
#elif defined(__GNUC__)
        asm volatile("" : "+rm" (var));
#else
	    forceUseOfVariableVoid(static_cast<void*>(var));        // static_cast is safe, since forceUseOfVariable will not do anything with it anyway.
#endif
    }
}

#endif
