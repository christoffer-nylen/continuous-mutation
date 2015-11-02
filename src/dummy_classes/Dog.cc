#include <iostream>

#include "Dog.h"

Dog::Dog(int number_of_legs) :
  Canine(number_of_legs)
{}

void Dog::cry() {
  std::cout << "Woof Woof" << std::endl;
}

