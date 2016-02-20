#ifndef __COMMON_H__
#define __COMMON_H__

class Common
{
	public:
		template<typename T> static void forceUseOfVariable(T& var) {
			(void) var;	
		}
};

#endif
