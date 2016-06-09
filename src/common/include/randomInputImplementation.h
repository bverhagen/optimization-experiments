#ifndef __RANDOM_INPUT_IMPLEMENTATION_H__
#define __RANDOM_INPUT_IMPLEMENTATION_H__

#include <cstdlib>
#include <random>
#include <limits>

namespace Common {
namespace Implementation {
    template<bool isIntegralType, typename T>
    class randomInputHelper {
        public:
            static inline void generate(T* const input, std::size_t nbOfElements) noexcept {
                std::default_random_engine generator;
                std::uniform_int_distribution<T> distribution(0);

                for(std::size_t i = 0; i < nbOfElements; ++i) {
                    input[i] = distribution(generator);
                }
            }
    };

    // Partial specialization, required for non-integral types
    template<typename T>
    class randomInputHelper<false, T> {
        public:
            static inline void generate(T* const input, std::size_t nbOfElements) noexcept {
                randomInputHelper<true, uint8_t>::generate(reinterpret_cast<uint8_t*>(input), nbOfElements * sizeof(uint8_t)/sizeof(T));
            }
    };
}   // namespace Implementation
}   // namespace Common



#endif
