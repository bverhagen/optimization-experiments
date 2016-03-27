#include "performanceUtils.h"

namespace performanceUtils {
    void forceUseOfVariableVoid(void* /*var*/)noexcept {
        ;
    }

	bool alwaysReturnFalse(void) noexcept {
		return false;
	}
}
