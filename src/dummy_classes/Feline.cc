#include <iostream>

#include "Feline.h"

Feline::Feline(int number_of_legs) :
  number_of_legs(number_of_legs)
{}

void Feline::cry() {
  std::cout << "Meow" << std::endl;
}

int Feline::getNumberOfLegs() {
  return number_of_legs;
}

bool Feline::isScaredOf(Canine canine) {
  (void) canine;
  return true;
}

bool Feline::isScaredOf(Feline feline) {
  (void) feline;
  return false;
}
