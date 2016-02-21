#include "catch.hpp"

#include <cstdlib>
#include <vector>

#include "targetSpecific.h"
#include "randomInput.h"
#include "simd-and.h"

using std::size_t;
using std::vector;

namespace {
	template<typename T>
	void compareArrays(const T* const actual, const T* const correct, size_t nbOfElements) {
		for(size_t i = 0; i < nbOfElements; ++i) {
			REQUIRE(actual[i] == correct[i]);
		}
	}
}

namespace SimdAnd {
	namespace Test {
		SCENARIO("Test straightforward implementation with simple values", "[simple]") {
			GIVEN("Two inputs and their correct output") {
				typedef uint8_t test_type_t;
				const size_t nbOfElements = 4U;
				const test_type_t input1[] = { 0x01U, 0x03U, 0x03U, 0xFFU };
				const test_type_t input2[] = { 0x01U, 0x01U, 0x02U, 0xBCU };
			
				const test_type_t correct_result[] = { 0x01U, 0X01U, 0X02U, 0xBCU};

				WHEN("We apply the straightforward AND implementation on the inputs") {
					test_type_t actual_result[nbOfElements];
					simdAndNormal(input1, input2, actual_result, nbOfElements);	
					
					THEN("We should get the same output") {
						compareArrays(actual_result, correct_result, nbOfElements);
					}
				}
			}
			GIVEN("A random input and an input filled with all ones") {
				typedef uint8_t test_type_t;
				const size_t nbOfElements = 1024U;
				
				test_type_t input1[nbOfElements];
				Common::randomInput(input1, nbOfElements);
				test_type_t input2[nbOfElements];
				for(size_t i = 0; i < nbOfElements; ++i) {
					input2[i] = 0xFF;
				}

				WHEN("We apply the straightforward AND implementation on the inputs") {
					test_type_t actual_result[nbOfElements];
					simdAndNormal(input1, input2, actual_result, nbOfElements);

					THEN("We should get the same output as the random input") {
						compareArrays(actual_result, input1, nbOfElements);
					}
				}
			}
		}

		SCENARIO("Compare the output of different implementations with the same input", "[implementations]") {
			GIVEN("Two random inputs") {
				typedef uint8_t test_type_t;
				const size_t nbOfElements = 4096U;

				test_type_t input1[nbOfElements];
				test_type_t input2[nbOfElements];
				Common::randomInput(input1, input2, nbOfElements);
			
				WHEN("We apply the inputs on different kinds of AND implementations") {
					test_type_t actual_result_normal[nbOfElements];
					simdAndNormal(input1, input2, actual_result_normal, nbOfElements);
					
					test_type_t actual_result_force_simd[nbOfElements];
					simdAndForceRegisterSimd<test_type_t, unsigned_register_t>(input1, input2, actual_result_force_simd, nbOfElements);

					THEN("The outputs should be the same") {
						compareArrays(actual_result_force_simd, actual_result_normal, nbOfElements);
					}
				}
			}
		}
	}
}
