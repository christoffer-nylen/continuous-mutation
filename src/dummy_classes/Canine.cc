#include <iostream>

#include "Feline.h"

#include "Canine.h"

Canine::Canine(int number_of_legs) :
  number_of_legs(number_of_legs)
{}

void Canine::cry() {
  std::cout << "Woof" << std::endl;
}

int Canine::getNumberOfLegs() {
  return number_of_legs;
}

bool Canine::isScaredOf(Feline feline) {
  (void) feline;
  return false;
}

bool Canine::isScaredOf(Canine canine) {
  (void) canine;
  return false;
}
