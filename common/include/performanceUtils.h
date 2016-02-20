#ifndef __COMMON_H__
#define __COMMON_H__

namespace performanceUtils
{
	template<typename T> 
	inline void forceUseOfVariable(T& var) {
		(void) var;	
	}
};

#endif
