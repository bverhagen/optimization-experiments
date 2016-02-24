#include "catch.hpp"

#include <cstdlib>
#include <vector>
#include <iostream>

#include "targetSpecific.h"
#include "randomInput.h"
#include "simd-and.h"

using std::size_t;
using std::vector;
using TargetSpecific::unsigned_register_t;

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
					simdAnd(input1, input2, actual_result, nbOfElements);	
					
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
					simdAnd(input1, input2, actual_result, nbOfElements);

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
					simdAnd(input1, input2, actual_result_normal, nbOfElements);
					
					test_type_t actual_result_force_normal[nbOfElements];
					simdAndForceNormal(input1, input2, actual_result_force_normal, nbOfElements);

					THEN("The outputs should be the same") {
						compareArrays(actual_result_force_normal, actual_result_normal, nbOfElements);
					}
				}
			}

			GIVEN("Two aligned inputs") {
				typedef uint8_t test_type_t;
				const size_t nbOfRealElements = 4096U;
				const size_t nbOfElements = nbOfRealElements * sizeof(test_type_t)/sizeof(v4uint8_t);

				v4uint8_t input1[nbOfElements];
				v4uint8_t input2[nbOfElements];
				Common::randomInput( (test_type_t*)(input1), (test_type_t*)(input2), nbOfRealElements);
			
				WHEN("We apply the inputs on different kinds of AND implementations") {
					test_type_t actual_result_normal[nbOfRealElements];
					simdAnd((test_type_t*) input1, (test_type_t*) input2, (test_type_t*) actual_result_normal, nbOfRealElements);

					v4uint8_t actual_result_vector[nbOfElements];
					simdAnd(input1, input2, actual_result_vector, nbOfElements);
					
					THEN("The outputs should be the same") {
						compareArrays((test_type_t*)(actual_result_vector), actual_result_normal, nbOfRealElements);
					}
				}
			}
		}
	}
}
