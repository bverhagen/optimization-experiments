#ifndef __RANDOM_INPUT_H__
#define __RANDOM_INPUT_H__

#include "randomInputImplementation.h"

namespace Common {
    template<typename... T>
    void randomInput(std::size_t nbOfElements, T* const ... input) noexcept {
        Implementation::multipleRandomInputHelper<T...>::generate(nbOfElements, input...);
    }
}   // namespace Common

#endif
