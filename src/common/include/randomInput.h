#ifndef __RANDOM_INPUT_H__
#define __RANDOM_INPUT_H__

#include "randomInputImplementation.h"

namespace Common {
    template<typename T>
    inline void randomInput(T* const input, std::size_t nbOfElements) noexcept {
        Implementation::randomInputHelper<std::is_integral<T>::value, T>::generate(input, nbOfElements);
    }

    template<typename T>
    inline void randomInput(T* const input1, T* const input2, std::size_t nbOfElements) noexcept {
        randomInput(input1, nbOfElements);
        randomInput(input2, nbOfElements);
	}

}   // namespace Common

#endif
