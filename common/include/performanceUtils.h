#ifndef __PERFORMANCEUTILS_H__
#define __PERFORMANCEUTILS_H__

#include <cstdint>

namespace performanceUtils
{
    void forceUseOfVariableVoid(void* var)noexcept;             // Force the fake use of the variable to be hidden in a separate compilation unit
	bool alwaysReturnFalse(void) noexcept;

	template<typename T> 
	void forceUseOfVariable(T& var) noexcept {
	    forceUseOfVariableVoid(static_cast<void*>(&var));       // static_cast is safe, since forceUseOfVariable will not do anything with it anyway.
	}

	template<typename T> 
	void forceUseOfVariable(T* var) noexcept {
	    forceUseOfVariableVoid(static_cast<void*>(var));        // static_cast is safe, since forceUseOfVariable will not do anything with it anyway.
	}
}

#endif
