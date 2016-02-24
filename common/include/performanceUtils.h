#ifndef __PERFORMANCEUTILS_H__
#define __PERFORMANCEUTILS_H__

namespace performanceUtils
{
	template<typename T> 
	inline void forceUseOfVariable(T& var) noexcept {
		(void) var;	
	}

	template<typename T> 
	inline void forceUseOfVariable(T* var) noexcept {
		(void) var;	
	}

	bool alwaysReturnFalse(void) noexcept;
}

#endif
