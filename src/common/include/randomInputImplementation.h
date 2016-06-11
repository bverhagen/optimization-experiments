#ifndef __RANDOM_INPUT_IMPLEMENTATION_H__
#define __RANDOM_INPUT_IMPLEMENTATION_H__

#include <cstdlib>
#include <random>
#include <limits>
#include <type_traits>

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

    template<typename T>
    void randomInput(T* const input, std::size_t nbOfElements) noexcept {
        randomInputHelper<std::is_integral<T>::value, T>::generate(input, nbOfElements);
    }

    // Metaprogramming to write multiple random inputs as consecutive calls for each input
    template<typename... T>
    class multipleRandomInputHelper {
        public:
            static inline void generate(std::size_t nbOfElements, T* const... inputs) noexcept {
                multipleRandomInputHelper<T...>::generate(nbOfElements, inputs...);
            }
    };

    template<typename T1, typename... T>
    class multipleRandomInputHelper<T1, T...> {
        public:
            static inline void generate(std::size_t nbOfElements, T1* const input1, T* const... inputs) noexcept {
                randomInput(input1, nbOfElements);
                multipleRandomInputHelper<T...>::generate(nbOfElements, inputs...);
            }
    };

    template<typename T1>
    class multipleRandomInputHelper<T1> {
        public:
            static inline void generate(std::size_t nbOfElements, T1* const input) noexcept {
                randomInput(input, nbOfElements);
            }
    };

}   // namespace Implementation
}   // namespace Common

#endif
